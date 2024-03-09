<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class NlpTaskUpdateRequest extends FormRequest
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
     */
    public function rules(): array
    {
        return [
            'short_name' => ['required', 'string'],
            'full_name' => ['nullable', 'string'],
            'description' => ['nullable', 'string'],
            'papers_with_code_ids' => ['required', 'json'],
        ];
    }
}
