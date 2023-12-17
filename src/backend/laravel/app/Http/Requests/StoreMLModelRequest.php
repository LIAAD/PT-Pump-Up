<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Support\Facades\Auth;

class StoreMLModelRequest extends FormRequest
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
            'name' => 'required|string|unique:ml_models',
            'description' => 'required|string',
            'year' => 'required|integer',
            'authors' => 'required|array',
            'authors.*' => 'required|email',
            'hrefs' => 'required|array',
            'hrefs.papers_with_code' => 'nullable|url',
            'hrefs.link_source' => 'nullable|url',
            'hrefs.link_hf' => 'nullable|url',
            'hrefs.link_github' => 'nullable|url',
            'hrefs.doi' => 'nullable|url',

            'model_stats' => 'required|array',
            'model_stats.broken_link' => 'required|boolean',
            'model_stats.author_response' => 'required|boolean',
            'model_stats.standard_format' => 'required|boolean',
            'model_stats.backup' => 'required|boolean',
            'model_stats.preservation_rating' => 'required|string',
            'model_stats.off_the_shelf' => 'required|boolean',

            'model_stats' => 'required|array',
            'model_stats.architecture' => 'required|string',
            'model_stats.size_in_mb' => 'nullable|numeric',

            #TODO: Add Benchmark validation
            #TODO: Add License validation

            #TODO: Add publication validation

            'nlp_tasks' => 'required|array',
            'nlp_tasks.*' => 'required|string',
        ];
    }
}
