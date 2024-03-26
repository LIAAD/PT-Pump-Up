<?php

namespace App\Http\Controllers;

use App\Models\MachineLearningModel;
use App\Models\Author;
use App\Traits\StoreResourceTrait;
use App\Http\Requests\StoreMachineLearningModelRequest;
use Illuminate\Support\Facades\DB;
use App\Models\NlpTask;
use App\Models\Link;
use App\Models\ResourceStats;
use App\Models\Result;
use Inertia\Inertia;

use Illuminate\Http\Request;

class MachineLearningModelController extends Controller
{ 
    use StoreResourceTrait;
    /**
     * Display a listing of the resource.
     */
    public function index(Request $request)
    {
        $models = MachineLearningModel::with(['authors', 'link', 'resourceStats','nlpTasks', 'results'])->get();

        if($request->wantsJson() || $request->is('api/*'))
            return $models;

        $nlp_task_names = array();

        foreach ($models as $model) {
            foreach ($model->nlpTasks as $nlp_task) {
                array_push($nlp_task_names, $nlp_task->full_name ?? $nlp_task->short_name);
            }
        }
        
        return Inertia::render('Models/Index',[
            'models' => MachineLearningModel::with(['authors', 'link', 'resourceStats','nlpTasks', 'results'])->get(),
            'nlp_tasks' => collect($nlp_task_names)->unique()->values()->shuffle()->all(), 
        ]);
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreMachineLearningModelRequest $request)
    {
        
        DB::beginTransaction();
        
        $validated = $request->validated();

        try {
            
            $link = Link::create($validated['link']);            
            $resource_stats = ResourceStats::create($validated['resource_stats']);
            
            $machineLearningModel = MachineLearningModel::create([
                'short_name' => $validated['short_name'],
                'full_name' => $validated['full_name'],
                'description' => $validated['description'],
                'year' => $validated['year'],
                'link_id' => $link->id,
                'resource_stats_id' => $resource_stats->id,                         
            ]);

            
            foreach($validated['results'] as $result){
                
                $new_result = new Result([
                    'metric' => $result['metric'],
                    'value' => $result['value'],                    
                    'train_dataset_id' => $result['train_dataset']['id'],
                    'test_dataset_id' => $result['test_dataset']['id'],
                    'validation_dataset_id' => $result['validation_dataset']['id'] ?? null,
                    'machine_learning_model_id' => $machineLearningModel->id
                ]);
                                
                $new_result->save();
            }
                        
            
            foreach ($validated['authors'] as $value){
                $author = Author::join('links', 'authors.link_id', '=', 'links.id')
                    ->where('email', $value['link']['email'])
                    ->firstOrFail();

                $machineLearningModel->authors()->attach($author);
            }              
            
            foreach ($validated['nlp_tasks'] as $value){
                $nlp_task = NlpTask::where('short_name', $value['short_name'])->firstOrFail();
                $machineLearningModel->nlpTasks()->attach($nlp_task);
            }
                        
            $machineLearningModel->save();            
            
            DB::commit();
            
            return response()->json(MachineLearningModel::with(['authors', 'link', 'resourceStats', 'nlpTasks', 'results'])->findOrfail($machineLearningModel->id), 201);

        } catch (\Throwable $th) {
            DB::rollBack();
            throw $th;
        } catch (\Exception $e) {
            DB::rollBack();
            throw $e;
        }
        
        abort(500, 'An error occurred while creating the machine learning model');
    }

    /**
     * Display the specified resource.
     */
    public function show(MachineLearningModel $machineLearningModel)
    {
        abort(501, 'Not implemented');
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, MachineLearningModel $machineLearningModel)
    {
        abort(501, 'Not implemented');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(MachineLearningModel $machineLearningModel)
    {
        $machineLearningModel->delete();

        return response()->noContent();
    }
}
