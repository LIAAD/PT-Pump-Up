<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreDatasetRequest;
use App\Http\Requests\UpdateDatasetRequest;
use App\Models\Dataset;
use App\Models\Language;
use App\Models\NLPTask;
use App\Models\Author;
use App\Models\ResourceStats;
use Inertia\Inertia;
use App\Models\Href;

class DatasetController extends Controller
{

    public function index_web()
    {
        return Inertia::render('Datasets/Index', [
            'datasets' => Dataset::with(['authors', 'nlpTasks', 'href', 'resourceStats'])->get(),
            'authors' => Author::all(),
            'nlp_tasks' => NLPTask::all(),
        ]);
    }
    /**
     * Display a listing of the resource. For the API.
     * 
     */
    public function index_api()
    {
        return Dataset::with(['authors', 'nlpTasks'])->get();
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return Inertia::render('Datasets/Create', [
            'languages' => Language::all(),
            'nlp_tasks' => NLPTask::all(),
            'authors' => Author::with('href')->get(),
        ]);
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

        # Create the HRefs for the dataset.
        $dataset->href()->associate(Href::create([
            'papers_with_code' => $request->hrefs['papers_with_code'] ?? null,
            'link_source' => $request->hrefs['link_source'] ?? null,
            'link_hf' => $request->hrefs['link_hf'] ?? null,
            'link_github' => $request->hrefs['link_github'] ?? null,
            'doi' => $request->hrefs['doi'] ?? null,
        ]));

        # Create the ResourceStatus for the dataset.
        $dataset->resourceStats()->associate(ResourceStats::create([
            'broken_link' => $request->dataset_stats['broken_link'],
            'author_response' => $request->dataset_stats['author_response'],
            'standard_format' => $request->dataset_stats['standard_format'],
            'backup' => $request->dataset_stats['backup'],
            'preservation_rating' => $request->dataset_stats['preservation_rating'] ?? null,
            'off_the_shelf' => $request->dataset_stats['off_the_shelf'],
        ]));

        $dataset->saveOrFail();

        $emails = $request->authors;

        $authors = Author::whereHas('href', function ($query) use ($emails) {
            $query->whereIn('email', $emails);
        })->get();

        $dataset->authors()->attach($authors);

        $dataset->nlpTasks()->attach(NLPTask::whereIn('acronym', $request->nlp_tasks)->get());

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
