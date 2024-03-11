<?php

namespace App\Http\Controllers;

use App\Models\Dataset;
use Illuminate\Http\Request;
use App\Http\Requests\StoreDatasetRequest;
use Illuminate\Support\Facades\DB;
use App\Traits\StoreLinkTrait;
use App\Traits\StoreResourceStatsTrait;
use App\Models\Author;
use App\Models\NlpTask;


class DatasetController extends Controller
{
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
        DB::beginTransaction();

        $validated = $request->validated();
        
        try {
          
            $link = StoreLinkTrait::store($validated);        
            validated['link_id'] = $link->id;

            $resource_stats = StoreResourceStatsTrait::store($validated);
            $validated['resource_stats_id'] = $resource_stats->id;
            
            $dataset = Dataset::create($validated);
            
            foreach ($validated['author_emails'] as $author_email) {
                $authors[] = Author::with('link')
                                ->where('email', $author_email)
                                ->firstOrFail();
            }

            foreach($validated['nlp_tasks_short_names'] as $nlp_task_short_name) {
                $nlp_tasks[] = NlpTask::where('short_name', $nlp_task_short_name)
                                    ->firstOrFail();
            }

            $dataset->authors()->saveMany($authors);
            
            $dataset->nlpTasks()->saveMany($nlp_tasks);
        
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
