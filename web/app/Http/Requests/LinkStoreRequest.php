<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class LinkStoreRequest extends FormRequest
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
            'email' => ['nullable', 'email'],
            'website' => ['nullable', 'string'],
            'github' => ['nullable', 'string'],
            'hugging_face' => ['nullable', 'string'],
            'papers_with_code' => ['nullable', 'string'],
            'paper_url' => ['nullable', 'string'],
        ];
    }
}
