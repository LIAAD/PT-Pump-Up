<?php

namespace Tests\Feature\Http\Controllers;

use App\Models\Dataset;
use App\Models\Link;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use JMac\Testing\Traits\AdditionalAssertions;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

/**
 * @see \App\Http\Controllers\DatasetController
 */
final class DatasetControllerTest extends TestCase
{
    use AdditionalAssertions, RefreshDatabase, WithFaker;

    #[Test]
    public function index_displays_view(): void
    {
        $datasets = Dataset::factory()->count(3)->create();

        $response = $this->get(route('dataset.index'));

        $response->assertOk();
        $response->assertViewIs('dataset.index');
        $response->assertViewHas('datasets');
    }


    #[Test]
    public function create_displays_view(): void
    {
        $response = $this->get(route('dataset.create'));

        $response->assertOk();
        $response->assertViewIs('dataset.create');
    }


    #[Test]
    public function store_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\DatasetController::class,
            'store',
            \App\Http\Requests\DatasetStoreRequest::class
        );
    }

    #[Test]
    public function store_saves_and_redirects(): void
    {
        $short_name = $this->faker->word();
        $full_name = $this->faker->word();
        $description = $this->faker->text();
        $year = $this->faker->numberBetween(-10000, 10000);
        $link = Link::factory()->create();

        $response = $this->post(route('dataset.store'), [
            'short_name' => $short_name,
            'full_name' => $full_name,
            'description' => $description,
            'year' => $year,
            'link_id' => $link->id,
        ]);

        $datasets = Dataset::query()
            ->where('short_name', $short_name)
            ->where('full_name', $full_name)
            ->where('description', $description)
            ->where('year', $year)
            ->where('link_id', $link->id)
            ->get();
        $this->assertCount(1, $datasets);
        $dataset = $datasets->first();

        $response->assertRedirect(route('dataset.index'));
        $response->assertSessionHas('dataset.id', $dataset->id);
    }


    #[Test]
    public function show_displays_view(): void
    {
        $dataset = Dataset::factory()->create();

        $response = $this->get(route('dataset.show', $dataset));

        $response->assertOk();
        $response->assertViewIs('dataset.show');
        $response->assertViewHas('dataset');
    }


    #[Test]
    public function edit_displays_view(): void
    {
        $dataset = Dataset::factory()->create();

        $response = $this->get(route('dataset.edit', $dataset));

        $response->assertOk();
        $response->assertViewIs('dataset.edit');
        $response->assertViewHas('dataset');
    }


    #[Test]
    public function update_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\DatasetController::class,
            'update',
            \App\Http\Requests\DatasetUpdateRequest::class
        );
    }

    #[Test]
    public function update_redirects(): void
    {
        $dataset = Dataset::factory()->create();
        $short_name = $this->faker->word();
        $full_name = $this->faker->word();
        $description = $this->faker->text();
        $year = $this->faker->numberBetween(-10000, 10000);
        $link = Link::factory()->create();

        $response = $this->put(route('dataset.update', $dataset), [
            'short_name' => $short_name,
            'full_name' => $full_name,
            'description' => $description,
            'year' => $year,
            'link_id' => $link->id,
        ]);

        $dataset->refresh();

        $response->assertRedirect(route('dataset.index'));
        $response->assertSessionHas('dataset.id', $dataset->id);

        $this->assertEquals($short_name, $dataset->short_name);
        $this->assertEquals($full_name, $dataset->full_name);
        $this->assertEquals($description, $dataset->description);
        $this->assertEquals($year, $dataset->year);
        $this->assertEquals($link->id, $dataset->link_id);
    }


    #[Test]
    public function destroy_deletes_and_redirects(): void
    {
        $dataset = Dataset::factory()->create();

        $response = $this->delete(route('dataset.destroy', $dataset));

        $response->assertRedirect(route('dataset.index'));

        $this->assertModelMissing($dataset);
    }
}
