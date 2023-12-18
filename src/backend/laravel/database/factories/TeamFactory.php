<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\Href;
use App\Models\Team;

class TeamFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Team::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'img' => $this->faker->word(),
            'name' => $this->faker->name(),
            'title' => $this->faker->sentence(4),
            'affiliation' => $this->faker->text(),
            'href_id' => Href::factory(),
        ];
    }
}
