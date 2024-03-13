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
        
        $ruben = new User([
            'name' => 'Rúben Almeida',
            'email' => 'ruben.f.almeida@inesctec.pt',
            'linkedin' => 'https://www.linkedin.com/in/almeida-ruben/',
            'github' => 'https://github.com/arubenruben',
            'huggingface' => 'https://huggingface.co/arubenruben',
            'password' => Factory::create()->password(),
            'role' => 'admin'
        ]);

        $ruben->photo()->associate(File::create([
            'path' => 'ruben.png'
        ]));

        $ruben->save();

        $sergio = new User([
            'name' => 'Sérgio Nunes',
            'email' => 'sergio.nunes@inesctec.pt',
            'password' => Factory::create()->password(),
            'role' => 'admin'
        ]);

        $sergio->photo()->associate(File::create([
            'path' => 'sergio.jpg'
        ]));

        $sergio->save();

        $alipio = new User([
            'name' => 'Alípio Jorge',
            'email' => 'alipio.jorge@inesctec.pt',
            'password' => Factory::create()->password(),
            'role' => 'admin'
        ]);

        $alipio->photo()->associate(File::create([
            'path' => 'alipio.png'
        ]));
        
        $alipio->save();

        $ricardo = new User([
            'name' => 'Ricardo Campos',
            'email' => 'ricardo.campos@inesctec.pt',
            'password' => Factory::create()->password(),
            'role' => 'admin'
        ]);

        $ricardo->photo()->associate(File::create([
            'path' => 'ricardo.jpg'
        ]));

        $ricardo->save();

        Publication::create([
            'bibtex' => '@article{de2023building,
                title={Building portuguese language resources for natural language processing tasks},
                author={de Almeida, Rúben Filipe Seabra},
                year={2023},
                note={Master Thesis},
              }'
            ]);
        
        Publication::create([
            'bibtex'=> '@article{almeida2024indexing,
                title={Indexing Portuguese NLP Resources with PT-Pump-Up},
                author={Almeida, R{\'u}ben and Campos, Ricardo and Jorge, Al{\'\i}pio and Nunes, S{\'e}rgio},
                journal={arXiv preprint arXiv:2401.15400},
                year={2024}
            }'
        ]);
    }
}
