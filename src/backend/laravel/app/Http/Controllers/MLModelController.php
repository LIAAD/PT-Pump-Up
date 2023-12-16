<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreMLModelRequest;
use App\Http\Requests\UpdateMLModelRequest;
use App\Models\MLModel;
use App\Models\Author;
use App\Models\NLPTask;

class MLModelController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        # Retrieve all MLModels with their authors.
        $ml_models = MLModel::all();

        foreach ($ml_models as $ml_model) {
            $ml_model->authors = Author::whereIn('_id', $ml_model->author_ids)->get();
            $ml_model->nlp_tasks = NLPTask::whereIn('_id', $ml_model->n_l_p_task_ids)->get();
        }

        return $ml_models;
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreMLModelRequest $request)
    {
        $ml_model = new MLModel([
            'name' => $request->name,
            'description' => $request->description,
            'year' => $request->year,
        ]);

        $ml_model->authors()->attach(Author::whereIn('hrefs.email', $request->authors)->get());
        $ml_model->nlp_tasks()->attach(NLPTask::whereIn('acronym', $request->nlp_tasks)->get());

        $ml_model->hrefs = [
            'papers_with_code' => $request->hrefs['papers_with_code'] ?? null,
            'link_source' => $request->hrefs['link_source'] ?? null,
            'link_hf' => $request->hrefs['link_hf'] ?? null,
            'link_github' => $request->hrefs['link_github'] ?? null,
            'doi' => $request->hrefs['doi'] ?? null,
        ];

        $ml_model->model_stats = [
            'broken_link' => $request->model_stats['broken_link'],
            'author_response' => $request->model_stats['author_response'],
            'standard_format' => $request->model_stats['standard_format'],
            'backup' => $request->model_stats['backup'],
            'preservation_rating' => $request->model_stats['preservation_rating'],
            'off_the_shelf' => $request->model_stats['off_the_shelf'],
        ];

        $ml_model->saveOrFail();

        return response()->json([
            'message' => 'MLModel created successfully.',
            'data' => $ml_model,
        ], 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(MLModel $mLModel)
    {
        //
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
