<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\NlpTask;
use App\Models\Link;
use File;

class NLPTaskSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $json_file = File::get("database/data/nlp_tasks.json");

        foreach (json_decode($json_file) as $nlp_task ){
            $nlp_task = new NlpTask([
                'short_name' => $nlp_task->short_name,
                'full_name' => $nlp_task->full_name,
                'description' => $nlp_task->description,
                'standard_format' => $nlp_task->standard_format,
                'papers_with_code_id' => $nlp_task->papers_with_code_id,                
            ]);

            $link = Link::create([
                'papers_with_code_url' => $nlp_task->papers_with_code_url,
            ]);

            $nlp_task->link()->associate($link);

            $nlp_task->save();            
        }
    }
}