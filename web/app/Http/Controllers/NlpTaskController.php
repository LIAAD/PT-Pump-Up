<?php

namespace App\Http\Controllers;

use App\Models\NlpTask;
use App\Models\Link;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;
use App\Http\Requests\StoreNLPTaskRequest;

class NLPTaskController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return NlpTask::all();
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreNLPTaskRequest $request)
    {        
        $request->validated();
        
        DB::beginTransaction();
        
        try {                        
            $nlp_task = new NlpTask([
                'short_name' => $request->short_name,
                'full_name' => $request->full_name,
                'description' => $request->description,
                'standard_format' => $request->standard_format,
                'papers_with_code_id' => $request->papers_with_code_id,            
            ]);
            
            $link = Link::create([
                'papers_with_code_url' => $request->link['papers_with_code_url'],
            ]);

            $nlp_task['link_id'] = $link->id;

            $nlp_task->save();

            DB::commit();
            
            return response()->json(NlpTask::with('link')->findOrFail($nlp_task->id), 201);        
        
        } catch (\Throwable $th) {
            DB::rollBack();
            throw $th;
        } catch (\Exception $e) {
            DB::rollBack();
            throw $e;
        }

        return response()->json($e, 500);                     
    }

    /**
     * Display the specified resource.
     */
    public function show(NlpTask $nlpTask)
    {
        abort(501, 'Not Implemented');
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, NlpTask $nlpTask)
    {
        abort(501, 'Not Implemented');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(NlpTask $nlpTask)
    {
        $nlpTask->delete();

        return response()->noContent();
    }
}
