<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreMLModelRequest;
use App\Http\Requests\UpdateMLModelRequest;
use App\Models\MLModel;
use App\Models\Author;
use App\Models\NLPTask;
use Inertia\Inertia;
use App\Models\Dataset;
use App\Models\Href;
use App\Models\ResourceStats;
use App\Models\Benchmark;

class MLModelController extends Controller
{

    public function index_web()
    {
        return Inertia::render(
            'MLModels/Index',
            ['ml_models' => MLModel::with(['authors', 'nlpTasks', 'href', 'resourceStats'])->get()]
        );
    }

    /**
     * Display a listing of the resource.
     */
    public function index_api()
    {
        return MLModel::with(['authors', 'nlpTasks'])->get();
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return Inertia::render('MLModels/Create', [
            'nlp_tasks' => NLPTask::all(),
            'authors' => Author::with('href')->get(),
            'datasets' => Dataset::all(),
        ]);
    }

    public function store_web(StoreMLModelRequest $request)
    {
        $response = $this->store_api($request);

        return Inertia::render('MLModels/Show', ['ml_model' => $response->original['ml_model']]);
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store_api(StoreMLModelRequest $request)
    {
        $ml_model = new MLModel([
            'english_name' => $request->english_name,
            'full_portuguese_name' => $request->full_portuguese_name,
            'description' => $request->description,
            'year' => $request->year,
            'architecture' => $request->architecture,
        ]);

        $ml_model->href()->associate(Href::create([
            'papers_with_code' => $request->hrefs['papers_with_code'] ?? null,
            'link_source' => $request->hrefs['link_source'] ?? null,
            'link_hf' => $request->hrefs['link_hf'] ?? null,
            'link_github' => $request->hrefs['link_github'] ?? null,
            'doi' => $request->hrefs['doi'] ?? null,
        ]));

        $ml_model->resourceStats()->associate(ResourceStats::create([
            'broken_link' => $request->model_stats['broken_link'],
            'author_response' => $request->model_stats['author_response'],
            'standard_format' => $request->model_stats['standard_format'],
            'backup' => $request->model_stats['backup'],
            'preservation_rating' => $request->model_stats['preservation_rating'] ?? null,
            'off_the_shelf' => $request->model_stats['off_the_shelf'],
        ]));

        $ml_model->saveOrFail();

        $emails = $request->authors;

        $authors = Author::whereHas('href', function ($query) use ($emails) {
            $query->whereIn('email', $emails);
        })->get();

        $ml_model->authors()->attach($authors);

        $ml_model->nlpTasks()->attach(NLPTask::whereIn('acronym', $request->nlp_tasks)->get());

        foreach ($request->benchmarks as $benchmark) {
            $ml_model->benchmarks->add(Benchmark::create([
                'ml_model_id' => $ml_model->id,
                'train_dataset_id' => $benchmark['train_dataset'],
                'validation_dataset_id' => $benchmark['validation_dataset'],
                'test_dataset_id' => $benchmark['test_dataset'],
                'metric' => $benchmark['metric'],
                'performance' => $benchmark['performance'],
            ]));
        }

        $ml_model->saveOrFail();

        return response()->json([
            'message' => 'MLModel created successfully.',
            'ml_model' => $ml_model,
        ], 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(MlModel $mLModel)
    {
        return Inertia::render('MLModels/Show', ['ml_model' => $mLModel]);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(MLModel $mLModel)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateMLModelRequest $request, MLModel $mLModel)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(MLModel $mLModel)
    {
        //
    }
}
