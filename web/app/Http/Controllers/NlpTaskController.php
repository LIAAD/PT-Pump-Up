<?php

namespace App\Http\Controllers;

use App\Models\NlpTask;
use Illuminate\Http\Request;

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
    public function store(Request $request)
    {
        abort(501, 'Not Implemented');
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
