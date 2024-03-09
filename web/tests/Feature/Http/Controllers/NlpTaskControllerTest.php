<?php

namespace Tests\Feature\Http\Controllers;

use App\Models\NlpTask;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use JMac\Testing\Traits\AdditionalAssertions;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

/**
 * @see \App\Http\Controllers\NlpTaskController
 */
final class NlpTaskControllerTest extends TestCase
{
    use AdditionalAssertions, RefreshDatabase, WithFaker;

    #[Test]
    public function index_behaves_as_expected(): void
    {
        $nlpTasks = NlpTask::factory()->count(3)->create();

        $response = $this->get(route('nlp-task.index'));

        $response->assertOk();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function store_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\NlpTaskController::class,
            'store',
            \App\Http\Requests\NlpTaskStoreRequest::class
        );
    }

    #[Test]
    public function store_saves(): void
    {
        $short_name = $this->faker->word();
        $papers_with_code_ids = $this->faker->;

        $response = $this->post(route('nlp-task.store'), [
            'short_name' => $short_name,
            'papers_with_code_ids' => $papers_with_code_ids,
        ]);

        $nlpTasks = NlpTask::query()
            ->where('short_name', $short_name)
            ->where('papers_with_code_ids', $papers_with_code_ids)
            ->get();
        $this->assertCount(1, $nlpTasks);
        $nlpTask = $nlpTasks->first();

        $response->assertCreated();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function show_behaves_as_expected(): void
    {
        $nlpTask = NlpTask::factory()->create();

        $response = $this->get(route('nlp-task.show', $nlpTask));

        $response->assertOk();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function update_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\NlpTaskController::class,
            'update',
            \App\Http\Requests\NlpTaskUpdateRequest::class
        );
    }

    #[Test]
    public function update_behaves_as_expected(): void
    {
        $nlpTask = NlpTask::factory()->create();
        $short_name = $this->faker->word();
        $papers_with_code_ids = $this->faker->;

        $response = $this->put(route('nlp-task.update', $nlpTask), [
            'short_name' => $short_name,
            'papers_with_code_ids' => $papers_with_code_ids,
        ]);

        $nlpTask->refresh();

        $response->assertOk();
        $response->assertJsonStructure([]);

        $this->assertEquals($short_name, $nlpTask->short_name);
        $this->assertEquals($papers_with_code_ids, $nlpTask->papers_with_code_ids);
    }


    #[Test]
    public function destroy_deletes_and_responds_with(): void
    {
        $nlpTask = NlpTask::factory()->create();

        $response = $this->delete(route('nlp-task.destroy', $nlpTask));

        $response->assertNoContent();

        $this->assertModelMissing($nlpTask);
    }
}
