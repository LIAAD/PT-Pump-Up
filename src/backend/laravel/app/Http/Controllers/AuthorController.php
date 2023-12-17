<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreAuthorRequest;
use App\Http\Requests\UpdateAuthorRequest;
use App\Models\Author;

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
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreAuthorRequest $request)
    {
        $author = Author::create([
            'name' => $request->name,
            'affiliation' => $request->affiliation,
        ]);

        # Create the HRefs for the author.
        $author->hrefs = [
            'email' => $request->hrefs['email'],
            'website' => $request->hrefs['website'] ?? null,
            'orcid' => $request->hrefs['orcid'] ?? null,
            'github' => $request->hrefs['github'] ?? null,
            'twitter' => $request->hrefs['twitter'] ?? null,
            'googleScholar' => $request->hrefs['googleScholar'] ?? null,
            'linkedin' => $request->hrefs['linkedin'] ?? null,
        ];

        $author->save();

        return response()->json([
            'message' => 'Author created successfully.',
            'author' => $author,
        ], 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(Author $author)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Author $author)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateAuthorRequest $request, Author $author)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Author $author)
    {
        //
    }
}
