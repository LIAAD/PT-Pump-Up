<?php

namespace Database\Seeders;

// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\User;
use Faker\Factory;
use App\Models\File;
use App\Models\Publication;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {        
        $this->call([
            NlpTaskSeeder::class,
            PublicationSeeder::class,
            TeamSeeder::class,
        ]);
    }
}
