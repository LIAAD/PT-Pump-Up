<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;

class MachineLearningModelStoreRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            'short_name' => ['required', 'string'],
            'full_name' => ['nullable', 'string'],
            'description' => ['nullable', 'string'],
            'year' => ['required', 'integer'],
            'link' => ['required', 'array'],
            'link.website' => ['nullable', 'string'],
            'link.github_url' => ['nullable', 'string'],
            'link.hugging_face_url' => ['nullable', 'string'],
            'link.papers_with_code_url' => ['nullable', 'string'],
            'link.paper_url' => ['nullable', 'string'],
            'resource_stats' => ['required', 'array'],
            'resource_stats.off_the_shelf' => ['required', 'boolean'],
            'resource_stats.standard_format' => ['required', 'boolean'],
            'resource_stats.preservation_rating' => ['required', 'string', Rule::in(['low', 'medium', 'high'])],
            'nlp_task_ids' => ['required', 'array'],
            'nlp_task_ids.*' => ['integer', 'exists:nlp_tasks,id'],
        ];
    }
}
