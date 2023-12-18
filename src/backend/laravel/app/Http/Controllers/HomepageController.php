<?php

namespace App\Http\Controllers;

use App\Models\Author;
use App\Models\Dataset;
use App\Models\MLModel;
use App\Models\NLPTask;
use App\Models\Publication;
use App\Models\Team;
use Inertia\Inertia;

class HomepageController extends Controller
{
    public function index()
    {
        return Inertia::render('Homepage', [
            'num_datasets' => Dataset::count(),
            'num_models' => MLModel::count(),
            'num_authors' => Author::count(),
            'nlp_tasks' => NLPTask::count(),
            'team' => Team::with(['href', 'publications'])->get(),
            'publications' => []
        ]);
    }
}
