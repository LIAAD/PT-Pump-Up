<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Inertia\Inertia;
use App\Models\Dataset;
use App\Models\MachineLearningModel;
use App\Models\Author;
use App\Models\NlpTask;
use App\Models\User;
use App\Models\Publication;


class HomepageController extends Controller
{
    public function index()
    {
        return Inertia::render('Homepage',[
            'num_datasets' => Dataset::count(),
            'num_models' => MachineLearningModel::count(),
            'num_authors' => Author::count(),
            'num_nlp_tasks'=> NlpTask::count(),
            'admins' => User::with('photo')->where('role', 'admin')->get(),
            'publications' => Publication::all(),
        ]);
    }
}
