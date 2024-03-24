<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Publication;
use File;

class PublicationSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $json_file = File::get("database/data/publications.json");

        foreach (json_decode($json_file) as $publication){
            Publication::create([
                'bibtex' => $publication->bibtex
            ]);
        }
    }
}
