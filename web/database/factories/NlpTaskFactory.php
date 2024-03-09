<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\NlpTask;

class NlpTaskFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = NlpTask::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'short_name' => $this->faker->word(),
            'full_name' => $this->faker->word(),
            'description' => $this->faker->text(),
            'papers_with_code_ids' => '{}',
        ];
    }
}
