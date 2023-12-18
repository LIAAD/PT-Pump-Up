<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\Href;

class HrefFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Href::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'email' => $this->faker->safeEmail(),
            'website' => $this->faker->word(),
            'orcid' => $this->faker->word(),
            'github' => $this->faker->word(),
            'twitter' => $this->faker->word(),
            'google_scholar' => $this->faker->word(),
            'linkedin' => $this->faker->word(),
            'link_source' => $this->faker->word(),
            'link_hf' => $this->faker->word(),
            'doi' => $this->faker->word(),
        ];
    }
}
