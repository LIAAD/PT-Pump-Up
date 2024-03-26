<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\Dataset;
use App\Models\MachineLearningModel;
use App\Models\Result;

class ResultFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Result::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'metric' => $this->faker->word(),
            'value' => $this->faker->randomFloat(0, 0, 9999999999.),
            'machine_learning_model_id' => MachineLearningModel::factory(),
            'train_dataset_id' => Dataset::factory(),
            'validation_dataset_id' => Dataset::factory(),
            'test_dataset_id' => Dataset::factory(),
        ];
    }
}
