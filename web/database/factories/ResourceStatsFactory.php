<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\ResourceStats;

class ResourceStatsFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = ResourceStats::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'preservation_rating' => $this->faker->word(),
            'standard_format' => $this->faker->boolean(),
            'off_the_shelf' => $this->faker->boolean(),
        ];
    }
}
