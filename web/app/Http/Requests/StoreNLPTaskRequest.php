<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StoreNLPTaskRequest extends FormRequest
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
            'short_name' => ['required', 'string']
            #'short_name' => ['required', 'string'],
            #'full_name' => ['nullable', 'string'],
            #'description' => ['nullable', 'string'],
            #'standard_format' => ['required', 'string'],
            #'papers_with_code_id' => ['nullable', 'integer'],
            #'link' => ['nullable', 'array'],
            #'link.papers_with_code' => ['nullable', 'string'],
        ];
    }
}
