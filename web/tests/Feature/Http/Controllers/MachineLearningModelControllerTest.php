<?php

namespace Tests\Feature\Http\Controllers;

use App\Models\Link;
use App\Models\MachineLearningModel;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use JMac\Testing\Traits\AdditionalAssertions;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

/**
 * @see \App\Http\Controllers\MachineLearningModelController
 */
final class MachineLearningModelControllerTest extends TestCase
{
    use AdditionalAssertions, RefreshDatabase, WithFaker;

    #[Test]
    public function index_displays_view(): void
    {
        $machineLearningModels = MachineLearningModel::factory()->count(3)->create();

        $response = $this->get(route('machine-learning-model.index'));

        $response->assertOk();
        $response->assertViewIs('machineLearningModel.index');
        $response->assertViewHas('machineLearningModels');
    }


    #[Test]
    public function create_displays_view(): void
    {
        $response = $this->get(route('machine-learning-model.create'));

        $response->assertOk();
        $response->assertViewIs('machineLearningModel.create');
    }


    #[Test]
    public function store_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\MachineLearningModelController::class,
            'store',
            \App\Http\Requests\MachineLearningModelStoreRequest::class
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

        $response = $this->post(route('machine-learning-model.store'), [
            'short_name' => $short_name,
            'full_name' => $full_name,
            'description' => $description,
            'year' => $year,
            'link_id' => $link->id,
        ]);

        $machineLearningModels = MachineLearningModel::query()
            ->where('short_name', $short_name)
            ->where('full_name', $full_name)
            ->where('description', $description)
            ->where('year', $year)
            ->where('link_id', $link->id)
            ->get();
        $this->assertCount(1, $machineLearningModels);
        $machineLearningModel = $machineLearningModels->first();

        $response->assertRedirect(route('machine-learning-model.index'));
        $response->assertSessionHas('machineLearningModel.id', $machineLearningModel->id);
    }


    #[Test]
    public function show_displays_view(): void
    {
        $machineLearningModel = MachineLearningModel::factory()->create();

        $response = $this->get(route('machine-learning-model.show', $machineLearningModel));

        $response->assertOk();
        $response->assertViewIs('machineLearningModel.show');
        $response->assertViewHas('machineLearningModel');
    }


    #[Test]
    public function edit_displays_view(): void
    {
        $machineLearningModel = MachineLearningModel::factory()->create();

        $response = $this->get(route('machine-learning-model.edit', $machineLearningModel));

        $response->assertOk();
        $response->assertViewIs('machineLearningModel.edit');
        $response->assertViewHas('machineLearningModel');
    }


    #[Test]
    public function update_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\MachineLearningModelController::class,
            'update',
            \App\Http\Requests\MachineLearningModelUpdateRequest::class
        );
    }

    #[Test]
    public function update_redirects(): void
    {
        $machineLearningModel = MachineLearningModel::factory()->create();
        $short_name = $this->faker->word();
        $full_name = $this->faker->word();
        $description = $this->faker->text();
        $year = $this->faker->numberBetween(-10000, 10000);
        $link = Link::factory()->create();

        $response = $this->put(route('machine-learning-model.update', $machineLearningModel), [
            'short_name' => $short_name,
            'full_name' => $full_name,
            'description' => $description,
            'year' => $year,
            'link_id' => $link->id,
        ]);

        $machineLearningModel->refresh();

        $response->assertRedirect(route('machine-learning-model.index'));
        $response->assertSessionHas('machineLearningModel.id', $machineLearningModel->id);

        $this->assertEquals($short_name, $machineLearningModel->short_name);
        $this->assertEquals($full_name, $machineLearningModel->full_name);
        $this->assertEquals($description, $machineLearningModel->description);
        $this->assertEquals($year, $machineLearningModel->year);
        $this->assertEquals($link->id, $machineLearningModel->link_id);
    }


    #[Test]
    public function destroy_deletes_and_redirects(): void
    {
        $machineLearningModel = MachineLearningModel::factory()->create();

        $response = $this->delete(route('machine-learning-model.destroy', $machineLearningModel));

        $response->assertRedirect(route('machine-learning-model.index'));

        $this->assertModelMissing($machineLearningModel);
    }
}
