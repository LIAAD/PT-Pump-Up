<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\Dataset;
use App\Models\Href;
use App\Models\ResourceStats;
use App\Models\User;

class DatasetFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Dataset::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'english_name' => $this->faker->text(),
            'full_portuguese_name' => $this->faker->text(),
            'description' => $this->faker->text(),
            'year' => $this->faker->numberBetween(-10000, 10000),
            'href_id' => Href::factory(),
            'resource_stats_id' => ResourceStats::factory(),
            'add_by_id' => User::factory(),
        ];
    }
}
