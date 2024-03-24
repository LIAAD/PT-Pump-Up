<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\User;
use Faker\Factory;
use File as LaravelFile;
use App\Models\File as PTPumpUpFile;

class TeamSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $json_file = LaravelFile::get("database/data/team.json");
        
        foreach (json_decode($json_file) as $user){
            
            $elem = new User([
                'name' => $user->name,
                'email' => $user->email,
                'linkedin' => $user->linkedin ?? null,
                'github' => $user->github ?? null,
                'huggingface' => $user->huggingface ?? null,
                'password' => $user->password ?? Factory::create()->password(),
                'role' => $user->role ?? 'admin'
            ]);

            $elem->photo()->associate(PTPumpUpFile::create([
                'path' => $user->photo,
            ]));
                        
            $elem->save();                        
        }
    }
}
