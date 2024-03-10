<?php

namespace Tests\Feature\Http\Controllers;

use App\Models\ResourceStat;
use App\Models\ResourceStats;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use JMac\Testing\Traits\AdditionalAssertions;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

/**
 * @see \App\Http\Controllers\ResourceStatsController
 */
final class ResourceStatsControllerTest extends TestCase
{
    use AdditionalAssertions, RefreshDatabase, WithFaker;

    #[Test]
    public function index_behaves_as_expected(): void
    {
        $resourceStats = ResourceStats::factory()->count(3)->create();

        $response = $this->get(route('resource-stat.index'));

        $response->assertOk();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function store_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\ResourceStatsController::class,
            'store',
            \App\Http\Requests\ResourceStatsStoreRequest::class
        );
    }

    #[Test]
    public function store_saves(): void
    {
        $preservation_rating = $this->faker->word();
        $standard_format = $this->faker->boolean();
        $off_the_shelf = $this->faker->boolean();

        $response = $this->post(route('resource-stat.store'), [
            'preservation_rating' => $preservation_rating,
            'standard_format' => $standard_format,
            'off_the_shelf' => $off_the_shelf,
        ]);

        $resourceStats = ResourceStat::query()
            ->where('preservation_rating', $preservation_rating)
            ->where('standard_format', $standard_format)
            ->where('off_the_shelf', $off_the_shelf)
            ->get();
        $this->assertCount(1, $resourceStats);
        $resourceStat = $resourceStats->first();

        $response->assertCreated();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function show_behaves_as_expected(): void
    {
        $resourceStat = ResourceStats::factory()->create();

        $response = $this->get(route('resource-stat.show', $resourceStat));

        $response->assertOk();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function update_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\ResourceStatsController::class,
            'update',
            \App\Http\Requests\ResourceStatsUpdateRequest::class
        );
    }

    #[Test]
    public function update_behaves_as_expected(): void
    {
        $resourceStat = ResourceStats::factory()->create();
        $preservation_rating = $this->faker->word();
        $standard_format = $this->faker->boolean();
        $off_the_shelf = $this->faker->boolean();

        $response = $this->put(route('resource-stat.update', $resourceStat), [
            'preservation_rating' => $preservation_rating,
            'standard_format' => $standard_format,
            'off_the_shelf' => $off_the_shelf,
        ]);

        $resourceStat->refresh();

        $response->assertOk();
        $response->assertJsonStructure([]);

        $this->assertEquals($preservation_rating, $resourceStat->preservation_rating);
        $this->assertEquals($standard_format, $resourceStat->standard_format);
        $this->assertEquals($off_the_shelf, $resourceStat->off_the_shelf);
    }


    #[Test]
    public function destroy_deletes_and_responds_with(): void
    {
        $resourceStat = ResourceStats::factory()->create();
        $resourceStat = ResourceStat::factory()->create();

        $response = $this->delete(route('resource-stat.destroy', $resourceStat));

        $response->assertNoContent();

        $this->assertModelMissing($resourceStat);
    }
}
