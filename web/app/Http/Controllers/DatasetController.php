<?php

namespace App\Http\Controllers;

use App\Models\Dataset;
use Illuminate\Http\Request;
use App\Http\Requests\StoreDatasetRequest;
use Illuminate\Support\Facades\DB;
use App\Traits\StoreResourceTrait;
use App\Models\Author;
use App\Models\NlpTask;
use App\Models\Link;
use App\Models\ResourceStats;
use Inertia\Inertia;


class DatasetController extends Controller
{
    use StoreResourceTrait;
    /**
     * Display a listing of the resource.
     */
    public function index(Request $request)
    {   
        # Test if the request is an API request
        if ($request->wantsJson() || $request->is('api/*'))
            return Dataset::with(['authors', 'link', 'resourceStats', 'nlpTasks'])->get();
        
        return Inertia::render('Datasets/Index',[
            'datasets' => Dataset::with(['authors', 'link', 'resourceStats', 'nlpTasks'])->get()
        ]);        
    }
    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreDatasetRequest $request)
    {
        DB::beginTransaction();

        $validated = $request->validated();
        
        try {          
            $link = Link::create($validated['link']);        
            $validated['link_id'] = $link->id;

            $resource_stats = ResourceStats::create($validated['resource_stats']);
            $validated['resource_stats_id'] = $resource_stats->id;
            
            $dataset = Dataset::create($validated);

            StoreResourceTrait::create_authors($dataset, $validated['author_emails']);
            StoreResourceTrait::create_nlp_tasks($dataset, $validated['nlp_tasks_short_names']);
            
            $dataset->save();
        
            DB::commit();

            $dataset = Dataset::with(['authors', 'link', 'resourceStats', 'nlpTasks'])
                            ->where('id', $dataset->id)
                            ->first();

            return response()->json($dataset, 201);

        }
        catch (\Throwable $th) {
            DB::rollBack();
            throw $th;
        }
        catch (\Exception $e) {
            DB::rollBack();
            throw $e;
        }

        abort(500, 'An error occurred while trying to store the dataset');
    }

    /**
     * Display the specified resource.
     */
    public function show(Dataset $dataset)
    {
        return $dataset;
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Dataset $dataset)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Dataset $dataset)
    {
        $dataset->delete();

        return response()->noContent();
    }
}
