<?php

namespace App\Http\Controllers;

use App\Models\Author;
use Illuminate\Http\Request;
use App\Http\Requests\StoreAuthorRequest;
use App\Models\Link;    

class AuthorController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Author::all();
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreAuthorRequest $request)
    {
        $validated = $request->validated();

        $existing_authors = Author::join('links', 'authors.link_id', '=', 'links.id')->where('email', $validated['link']['email'])->get();

        if($existing_authors->isNotEmpty())        
            return response()->json($existing_authors, 409);
        

        $link = Link::create($validated['link']);

        $validated['link_id'] = $link->id;
        
        $author = Author::create($validated);

        return response()->json(Author::with('link')->findOrFail($author->id), 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(Author $author)
    {
        return $author;
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Author $author)
    {
        abort(501, 'Not implemented');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Author $author)
    {
        $author->delete();

        return response()->noContent();
    }
}
