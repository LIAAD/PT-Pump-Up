<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreDatasetRequest;
use App\Http\Requests\UpdateDatasetRequest;
use App\Models\Dataset;
use App\Models\Language;
use App\Models\NLPTask;
use App\Models\Author;
use Inertia\Inertia;

class DatasetController extends Controller
{

    public function index_web()
    {
        return Inertia::render('Datasets/Index', [
            'datasets' => Dataset::with(['authors', 'nlp_tasks'])->get(),
        ]);
    }
    /**
     * Display a listing of the resource. For the API.
     * 
     */
    public function index_api()
    {
        return Dataset::with(['authors', 'nlp_tasks'])->get();
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
            'year' => $request->year,
        ]);

        # Create the LanguageStats for the dataset.
        $dataset->language_stats = $request->language_stats;

        $dataset->authors()->attach(Author::whereIn('hrefs.email', $request->authors)->get());
        $dataset->nlp_tasks()->attach(NLPTask::whereIn('acronym', $request->nlp_tasks)->get());

        # Create the HRefs for the dataset.
        $dataset->hrefs = [
            'papers_with_code' => $request->hrefs['papers_with_code'] ?? null,
            'link_source' => $request->hrefs['link_source'] ?? null,
            'link_hf' => $request->hrefs['link_hf'] ?? null,
            'link_github' => $request->hrefs['link_github'] ?? null,
            'doi' => $request->hrefs['doi'] ?? null,
        ];

        # Create the ResourceStatus for the dataset.
        $dataset->dataset_stats = [
            'broken_link' => $request->dataset_stats['broken_link'],
            'author_response' => $request->dataset_stats['author_response'],
            'standard_format' => $request->dataset_stats['standard_format'],
            'backup' => $request->dataset_stats['backup'],
            'preservation_rating' => $request->dataset_stats['preservation_rating'],
            'off_the_shelf' => $request->dataset_stats['off_the_shelf'],
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
