<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\Href;
use App\Models\MlModel;
use App\Models\ResourceStats;

class MlModelFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = MlModel::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'name' => $this->faker->name(),
            'description' => $this->faker->text(),
            'year' => $this->faker->numberBetween(-10000, 10000),
            'href_id' => Href::factory(),
            'resource_stats_id' => ResourceStats::factory(),
        ];
    }
}