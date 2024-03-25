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
        $datasets = Dataset::with(['authors', 'link', 'resourceStats', 'nlpTasks'])->get();

        # Test if the request is an API request
        if ($request->wantsJson() || $request->is('api/*'))
            return $datasets;
        
        $nlp_task_names = array();

        foreach ($datasets as $dataset) {
            foreach ($dataset->nlpTasks as $nlp_task) {
                array_push($nlp_task_names, $nlp_task->full_name ?? $nlp_task->short_name);
            }
        }        

        return Inertia::render('Datasets/Index',[
            'datasets' => Dataset::with(['authors', 'link', 'resourceStats', 'nlpTasks'])->get(),
            'nlp_tasks' => collect($nlp_task_names)->unique()->values()->shuffle()->all(), 
        ]);        
    }
    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreDatasetRequest $request)
    {
        DB::beginTransaction();

        $validated = $request->validated();
        try{

            $dataset = new Dataset([
                'short_name' => $validated['short_name'],
                'full_name' => $validated['full_name'],
                'description' => $validated['description'],
                'year' => $validated['year'],
            ]);

            if ($request->has('link')) {
                $link = Link::create($validated['link']);
                $dataset->link()->associate($link);
            }

            if ($request->has('resource_stats')) {
                $resource_stats = ResourceStats::create($validated['resource_stats']);
                $dataset->resourceStats()->associate($resource_stats);
            }

            $dataset->save();
            
            foreach ($validated['authors'] as $author) 
                $dataset->authors()->attach(Author::findOrFail($author['id']));
            
            foreach ($validated['nlp_tasks'] as $nlp_task)
                $dataset->nlpTasks()->attach(NlpTask::findOrFail($nlp_task['id']));
        
            DB::commit();

            return response()->json(Dataset::with(['authors', 'link', 'resourceStats', 'nlpTasks'])->findOrFail($dataset->id), 201);

        }catch(\Exception $e){
            DB::rollBack();
            throw $e;
        }catch(\Throwable $e){
            DB::rollBack();
            throw $e;
        }         

        return response()->json($e, 500);
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
