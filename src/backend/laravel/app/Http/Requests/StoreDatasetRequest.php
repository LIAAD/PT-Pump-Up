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
            'english_name' => 'required|string',
            'full_portuguese_name' => 'nullable|string',
            'description' => 'required|string',
            'introduction_date' => 'required|date',

            'language_stats' => 'required|array',
            'language_stats.*.iso_code' => 'required|string|exists:languages,iso_code',


            'authors' => 'required|array',
            'authors.*.email' => 'required|email',


            'nlp_tasks' => 'required|array',
            'nlp_tasks.*.acronym' => 'required|string',

            'hrefs' => 'required|array',
            'hrefs.papers_with_code' => 'nullable|url',
            'hrefs.link_source' => 'nullable|url',
            'hrefs.link_hf' => 'nullable|url',
            'hrefs.link_github' => 'nullable|url',
            'hrefs.doi' => 'nullable|url',

            'resource_status' => 'required|array',
            'resource_status.broken_link' => 'required|boolean',
            'resource_status.author_response' => 'required|boolean',
            'resource_status.standard_format' => 'required|boolean',
            'resource_status.backup' => 'required|boolean',
            'resource_status.preservation_rating' => 'required|string',
            'resource_status.off_the_shelf' => 'required|boolean',

        ];
    }
}
