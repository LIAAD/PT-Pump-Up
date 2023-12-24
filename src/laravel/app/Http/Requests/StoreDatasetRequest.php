<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Support\Facades\Auth;

class StoreDatasetRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return Auth::check();
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            'english_name' => 'required|string|unique:datasets,english_name',
            'full_portuguese_name' => 'nullable|string|unique:datasets,full_portuguese_name',
            'description' => 'required|string',
            'year' => 'numeric|integer',

            'language_stats' => 'required|array',
            'language_stats.*' => 'required|string|exists:languages,iso_code',


            'authors' => 'required|array',
            'authors.*' => 'required|email',


            'nlp_tasks' => 'required|array',
            'nlp_tasks.*' => 'required|string',
            
            #TODO: Change from hrefs to href
            
            'hrefs' => 'required|array',
            'hrefs.link_papers_with_code' => 'nullable|url',
            'hrefs.link_source' => 'nullable|url',
            'hrefs.link_hf' => 'nullable|url',
            'hrefs.link_github' => 'nullable|url',
            'hrefs.doi' => 'nullable|url',

            'dataset_stats' => 'required|array',
            'dataset_stats.broken_link' => 'required|boolean',
            'dataset_stats.author_response' => 'required|boolean',
            'dataset_stats.standard_format' => 'required|boolean',
            'dataset_stats.backup' => 'required|boolean',
            'dataset_stats.preservation_rating' => 'nullable|string',
            'dataset_stats.off_the_shelf' => 'required|boolean',

            #TODO: Add Publication validation


        ];
    }
}
