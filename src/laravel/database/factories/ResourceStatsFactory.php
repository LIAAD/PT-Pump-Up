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
            'broken_link' => $this->faker->boolean(),
            'author_response' => $this->faker->boolean(),
            'standard_format' => $this->faker->boolean(),
            'backup' => $this->faker->boolean(),
            'size_gb' => $this->faker->randomFloat(0, 0, 9999999999.),
            'preservation_rating' => $this->faker->word(),
            'state' => $this->faker->word(),
        ];
    }
}
