<?php

namespace Database\Seeders;

use App\Models\Href;
use App\Models\Team;
use App\Models\User;
use Faker\Factory;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class TeamSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $members = [
            [
                'img' => 'https://text2story.inesctec.pt/img/ruben_almeida.png',
                'name' => 'Rúben Almeida',
                'title' => 'NLP Researcher',
                'affiliation' => 'INESC Tec',
                'linkedin' => 'https://www.linkedin.com/in/almeida-ruben',
                'github' => "https://github.com/arubenruben",
                "email" => "ruben.f.almeida@inesctec.pt",
                'publication' => [
                    [
                        'title' => "Building Portuguese Language Resources for Natural Language Processing Tasks",
                        'year' => 2023,
                        'link_source' => "https://repositorio-aberto.up.pt/handle/10216/152584",
                        'bibtex' => "
                        @article{de2023building,
                            title={Building Portuguese Language Resources for Natural Language Processing Tasks},
                            author={de Almeida, R{\'u}ben Filipe Seabra},
                            year={2023}
                          }
                        "
                    ]
                ]
            ],
            [
                'img' => 'https://raw.githubusercontent.com/LIAAD/PT-Pump-Up/main/src/frontend/src/assets/images/RC5.png',
                'name' => 'Ricardo Campos',
                'title' => 'Coordinator',
                'affiliation' => 'INESC Tec',
                "email" => "ricardo.campos@inesctec.pt"
            ],
            [
                'img' => 'https://text2story.inesctec.pt/img/alipio.png',
                'name' => 'Alípio Jorge',
                'title' => 'Co-Coordinator',
                'affiliation' => 'INESC Tec',
                "email" => "amjorge@fc.up.pt"
            ],
            [
                'img' => 'https://text2story.inesctec.pt/img/sergio.jpg',
                'name' => 'Sérgio Nunes',
                'title' => 'Co-Coordinator',
                'affiliation' => 'INESC Tec',
                "email" => "ssn@fe.up.pt"
            ]
        ];

        foreach ($members as $member) {

            $team = new Team([
                'img' => $member['img'],
                'name' => $member['name'],
                'title' => $member['title'],
                'affiliation' => $member['affiliation'],
            ]);

            $team->user()->associate(User::create([
                'name' => $member['name'],
                'email' => $member['email'],
                # Fake password
                'password' => Factory::create()->password()
            ]));

            $team->href()->associate(Href::create([
                'linkedin' => $member['linkedin'] ?? null,
                'github' => $member['github'] ?? null,
                'email' => $member['email'] ?? null,
            ]));

            $team->save();

            if ($member['publication'] ?? null) {
                foreach ($member['publication'] as $publication) {
                    $team->publications()->create([
                        'title' => $publication['title'],
                        'year' => $publication['year'],
                        'bibtex' => $publication['bibtex'] ?? null,
                        'href_id' => Href::create([
                            'link_source' => $publication['link_source']
                        ])->id
                    ]);
                }
            }
        }
    }
}
