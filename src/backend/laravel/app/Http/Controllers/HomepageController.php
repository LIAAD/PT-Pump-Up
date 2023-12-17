<?php

namespace App\Http\Controllers;

use App\Models\Author;
use App\Models\Dataset;
use App\Models\MLModel;
use App\Models\NLPTask;
use App\Models\Publication;
use Inertia\Inertia;

class HomepageController extends Controller
{
    public function index()
    {

        $team =  [
            [
                'img' => 'https://text2story.inesctec.pt/img/ruben_almeida.png',
                'name' => 'Rúben Almeida',
                'title' => 'NLP Researcher',
                'affiliation' => 'INESC Tec',
                'linkedin' => 'https://www.linkedin.com/in/almeida-ruben',
                'github' => "https://github.com/arubenruben",
                "email" => "ruben.f.almeida@inesctec.pt"
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

        return Inertia::render('Homepage', [
            'num_datasets' => Dataset::count(),
            'num_models' => MLModel::count(),
            'num_authors' => Author::count(),
            'nlp_tasks' => NLPTask::count(),
            'team' => $team,           
            'publications' => []
        ]);
    }
}
