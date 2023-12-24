<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreNLPTaskRequest;
use App\Http\Requests\UpdateNLPTaskRequest;
use App\Models\NlpTask;

class NLPTaskController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
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
    public function store(StoreNLPTaskRequest $request)
    {
        $nlp_task = NlpTask::create([
            'name' => $request->name,
            'acronym' => $request->acronym,
            'papers_with_code_ids' => $request->papers_with_code_ids,
        ]);

        return response()->json([
            'message' => 'NLP Task created successfully.',
            'nlp_task' => $nlp_task,
        ], 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(NlpTask $nLPTask)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(NlpTask $nLPTask)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateNLPTaskRequest $request, NlpTask $nLPTask)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(NlpTask $nLPTask)
    {
        //
    }
}
