<?php

namespace App\Http\Controllers;

use App\Http\Requests\MachineLearningModelStoreRequest;
use App\Http\Requests\MachineLearningModelUpdateRequest;
use App\Models\MachineLearningModel;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class MachineLearningModelController extends Controller
{
    public function index(Request $request): View
    {
        $machineLearningModels = MachineLearningModel::all();

        return view('machineLearningModel.index', compact('machineLearningModels'));
    }

    public function create(Request $request): View
    {
        return view('machineLearningModel.create');
    }

    public function store(MachineLearningModelStoreRequest $request): RedirectResponse
    {
        $machineLearningModel = MachineLearningModel::create($request->validated());

        $request->session()->flash('machineLearningModel.id', $machineLearningModel->id);

        return redirect()->route('machineLearningModel.index');
    }

    public function show(Request $request, MachineLearningModel $machineLearningModel): View
    {
        return view('machineLearningModel.show', compact('machineLearningModel'));
    }

    public function edit(Request $request, MachineLearningModel $machineLearningModel): View
    {
        return view('machineLearningModel.edit', compact('machineLearningModel'));
    }

    public function update(MachineLearningModelUpdateRequest $request, MachineLearningModel $machineLearningModel): RedirectResponse
    {
        $machineLearningModel->update($request->validated());

        $request->session()->flash('machineLearningModel.id', $machineLearningModel->id);

        return redirect()->route('machineLearningModel.index');
    }

    public function destroy(Request $request, MachineLearningModel $machineLearningModel): RedirectResponse
    {
        $machineLearningModel->delete();

        return redirect()->route('machineLearningModel.index');
    }
}
