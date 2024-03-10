<?php

namespace App\Http\Controllers;

use App\Models\Dataset;
use Illuminate\Http\Request;
use App\Http\Requests\StoreDatasetRequest;
use Illuminate\Support\Facades\DB;
use App\Traits\StoreAuthorTrait;
use App\Traits\StoreLinkTrait;
use App\Traits\StoreResourceStatsTrait;
use App\Models\Author;
use App\Models\NlpTask;


class DatasetController extends Controller
{
    use StoreAuthorTrait;
    use StoreLinkTrait;
    use StoreResourceStatsTrait;
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Dataset::with(['authors', 'link', 'resourceStats', 'nlpTasks'])->get();
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreDatasetRequest $request)
    {
        $validated = $request->validated();
        
        DB::beginTransaction();
        
        try {            
            if($validated['authors']){
                foreach($validated['authors'] as $key => $author){
                    $response = StoreAuthorTrait::store($author);
                    #Load Authors object from json response
                    $authors[] = $response->original;            
                }                        
            }else{
                foreach($validated['author_ids'] as $key => $author_id){
                    $authors[] = Author::find($author_id);
                }
            }

            foreach($validated['nlp_task_ids'] as $key => $nlp_task_id){
                $nlp_tasks[] = NlpTask::find($nlp_task_id);
            }

            $link = StoreLinkTrait::store($validated);
            $validated['link_id'] = $link->id;

            $resource_stats = StoreResourceStatsTrait::store($validated);
            $validated['resource_stats_id'] = $resource_stats->id;
            
            $dataset = Dataset::create($validated);

            $dataset->authors()->saveMany($authors);
            
            $dataset->nlpTasks()->saveMany($nlp_tasks);
        
            DB::commit();

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

        abort(500);
    }

    /**
     * Display the specified resource.
     */
    public function show(Dataset $dataset)
    {
        //
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
