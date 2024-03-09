<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\Link;

class LinkFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Link::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'email' => $this->faker->safeEmail(),
            'website' => $this->faker->word(),
            'github' => $this->faker->word(),
            'hugging_face' => $this->faker->word(),
            'papers_with_code' => $this->faker->word(),
            'paper_url' => $this->faker->word(),
        ];
    }
}
