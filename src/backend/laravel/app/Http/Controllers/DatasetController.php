<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreDatasetRequest;
use App\Http\Requests\UpdateDatasetRequest;
use App\Models\Dataset;
use App\Models\Language;
use App\Models\NLPTask;

class DatasetController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Dataset::all();
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
    public function store(StoreDatasetRequest $request)
    {
        $dataset = new Dataset([
            'english_name' => $request->english_name,
            'full_portuguese_name' => $request->full_portuguese_name,
            'description' => $request->description,
            'introduction_date' => $request->introduction_date,
        ]);

        # Create the LanguageStats for the dataset.
        foreach ($request->language_stats as $language_stat) {
            if ($dataset->language_stats === null) {
                $dataset->language_stats = [];
            }

            $dataset->language_stats[] = [
                'iso_code' => $language_stat['iso_code'],
            ];
        }

        # Create the Authors for the dataset.
        foreach ($request->authors as $author) {
            $dataset->authors()->create([
                'email' => $author['email'],
            ]);
        }

        # Create the NLPTasks for the dataset.
        foreach ($request->nlp_tasks as $nlp_task)
            $dataset->nlp_tasks()->save(NLPTask::where('acronym', $nlp_task['acronym'])->first());


        # Create the HRefs for the dataset.
        $dataset->hrefs = [
            'papers_with_code' => $request->hrefs['papers_with_code'] ?? null,
            'link_source' => $request->hrefs['link_source'] ?? null,
            'link_hf' => $request->hrefs['link_hf'] ?? null,
            'link_github' => $request->hrefs['link_github'] ?? null,
            'doi' => $request->hrefs['doi'] ?? null,
        ];

        # Create the ResourceStatus for the dataset.
        $dataset->resource_status = [
            'broken_link' => $request->resource_status['broken_link'],
            'author_response' => $request->resource_status['author_response'],
            'standard_format' => $request->resource_status['standard_format'],
            'backup' => $request->resource_status['backup'],
            'preservation_rating' => $request->resource_status['preservation_rating'],
            'off_the_shelf' => $request->resource_status['off_the_shelf'],
        ];

        $dataset->saveOrFail();

        return response()->json([
            'message' => 'Dataset created successfully.',
            'dataset' => $dataset,
        ], 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(Dataset $dataset)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Dataset $dataset)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateDatasetRequest $request, Dataset $dataset)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Dataset $dataset)
    {
        //
    }
}
