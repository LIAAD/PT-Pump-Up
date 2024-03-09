<?php

namespace App\Http\Controllers;

use App\Http\Requests\DatasetStoreRequest;
use App\Http\Requests\DatasetUpdateRequest;
use App\Models\Dataset;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class DatasetController extends Controller
{
    public function index(Request $request): View
    {
        $datasets = Dataset::all();

        return view('dataset.index', compact('datasets'));
    }

    public function create(Request $request): View
    {
        return view('dataset.create');
    }

    public function store(DatasetStoreRequest $request): RedirectResponse
    {
        $dataset = Dataset::create($request->validated());

        $request->session()->flash('dataset.id', $dataset->id);

        return redirect()->route('dataset.index');
    }

    public function show(Request $request, Dataset $dataset): View
    {
        return view('dataset.show', compact('dataset'));
    }

    public function edit(Request $request, Dataset $dataset): View
    {
        return view('dataset.edit', compact('dataset'));
    }

    public function update(DatasetUpdateRequest $request, Dataset $dataset): RedirectResponse
    {
        $dataset->update($request->validated());

        $request->session()->flash('dataset.id', $dataset->id);

        return redirect()->route('dataset.index');
    }

    public function destroy(Request $request, Dataset $dataset): RedirectResponse
    {
        $dataset->delete();

        return redirect()->route('dataset.index');
    }
}
