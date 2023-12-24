<?php

namespace App\Http\Controllers;

use App\Models\Author;
use App\Models\Dataset;
use App\Models\MlModel;
use App\Models\NlpTask;
use App\Models\Team;
use Inertia\Inertia;

class HomepageController extends Controller
{
    public function index()
    {
        return Inertia::render('Homepage', [
            'num_datasets' => Dataset::count(),
            'num_models' => MlModel::count(),
            'num_authors' => Author::count(),
            'nlp_tasks' => NlpTask::count(),
            'team' => Team::with(['href', 'publications'])->get(),
            'publications' => []
        ]);
    }
}
