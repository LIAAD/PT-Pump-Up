<?php

namespace Tests\Feature\Http\Controllers;

use App\Models\Dataset;
use App\Models\MachineLearningModel;
use App\Models\Result;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use JMac\Testing\Traits\AdditionalAssertions;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

/**
 * @see \App\Http\Controllers\ResultController
 */
final class ResultControllerTest extends TestCase
{
    use AdditionalAssertions, RefreshDatabase, WithFaker;

    #[Test]
    public function index_behaves_as_expected(): void
    {
        $results = Result::factory()->count(3)->create();

        $response = $this->get(route('result.index'));

        $response->assertOk();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function store_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\ResultController::class,
            'store',
            \App\Http\Requests\ResultStoreRequest::class
        );
    }

    #[Test]
    public function store_saves(): void
    {
        $metric = $this->faker->word();
        $value = $this->faker->randomFloat(/** float_attributes **/);
        $machine_learning_model = MachineLearningModel::factory()->create();
        $train_dataset = Dataset::factory()->create();
        $validation_dataset = Dataset::factory()->create();
        $test_dataset = Dataset::factory()->create();

        $response = $this->post(route('result.store'), [
            'metric' => $metric,
            'value' => $value,
            'machine_learning_model_id' => $machine_learning_model->id,
            'train_dataset_id' => $train_dataset->id,
            'validation_dataset_id' => $validation_dataset->id,
            'test_dataset_id' => $test_dataset->id,
        ]);

        $results = Result::query()
            ->where('metric', $metric)
            ->where('value', $value)
            ->where('machine_learning_model_id', $machine_learning_model->id)
            ->where('train_dataset_id', $train_dataset->id)
            ->where('validation_dataset_id', $validation_dataset->id)
            ->where('test_dataset_id', $test_dataset->id)
            ->get();
        $this->assertCount(1, $results);
        $result = $results->first();

        $response->assertCreated();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function show_behaves_as_expected(): void
    {
        $result = Result::factory()->create();

        $response = $this->get(route('result.show', $result));

        $response->assertOk();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function update_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\ResultController::class,
            'update',
            \App\Http\Requests\ResultUpdateRequest::class
        );
    }

    #[Test]
    public function update_behaves_as_expected(): void
    {
        $result = Result::factory()->create();
        $metric = $this->faker->word();
        $value = $this->faker->randomFloat(/** float_attributes **/);
        $machine_learning_model = MachineLearningModel::factory()->create();
        $train_dataset = Dataset::factory()->create();
        $validation_dataset = Dataset::factory()->create();
        $test_dataset = Dataset::factory()->create();

        $response = $this->put(route('result.update', $result), [
            'metric' => $metric,
            'value' => $value,
            'machine_learning_model_id' => $machine_learning_model->id,
            'train_dataset_id' => $train_dataset->id,
            'validation_dataset_id' => $validation_dataset->id,
            'test_dataset_id' => $test_dataset->id,
        ]);

        $result->refresh();

        $response->assertOk();
        $response->assertJsonStructure([]);

        $this->assertEquals($metric, $result->metric);
        $this->assertEquals($value, $result->value);
        $this->assertEquals($machine_learning_model->id, $result->machine_learning_model_id);
        $this->assertEquals($train_dataset->id, $result->train_dataset_id);
        $this->assertEquals($validation_dataset->id, $result->validation_dataset_id);
        $this->assertEquals($test_dataset->id, $result->test_dataset_id);
    }


    #[Test]
    public function destroy_deletes_and_responds_with(): void
    {
        $result = Result::factory()->create();

        $response = $this->delete(route('result.destroy', $result));

        $response->assertNoContent();

        $this->assertModelMissing($result);
    }
}
