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
            'full_portuguese_name' => 'required|string',
            'description' => 'required|string',
            'introduction_date' => 'required|string',

            'language_stats' => 'required|array',
            'language_stats.*.language_id' => 'required|int|exists:languages,_id',


            'authors' => 'required|array',
            'authors.*.author_id' => 'required|int|exists:authors,_id',


            'nlp_tasks' => 'required|array',
            'nlp_tasks.*.nlp_task_id' => 'required|int',
            'nlp_tasks.*.nlp_task_name' => 'required|string',
            'nlp_tasks.*.nlp_task_acronym' => 'required|string',
            'nlp_tasks.*.nlp_task_papers_with_code_ids' => 'required|array',
            'nlp_tasks.*.nlp_task_papers_with_code_ids.*' => 'required|int',
            'hrefs' => 'required|json',
            'hrefs.papers_with_code' => 'required|string',


        ];
    }
}
