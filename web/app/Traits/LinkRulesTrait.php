<?php

namespace App\Traits;

trait LinkRulesTrait
{
    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public static function rules(): array
    {
        return [
            'email' => ['nullable', 'email'],
            'website' => ['nullable', 'url'],
            'github_url' => ['nullable', 'url'],
            'hugging_face_url' => ['nullable', 'url'],
            'papers_with_code_url' => ['nullable', 'url'],
            'paper_url' => ['nullable', 'url'],            
        ];
    }
}