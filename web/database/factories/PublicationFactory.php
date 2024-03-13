<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\Publication;

class PublicationFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Publication::class;

    /**
     * Define the model's default state.
     */
    public function definition(): array
    {
        return [
            'bibtex' => $this->faker->text(),
        ];
    }
}
