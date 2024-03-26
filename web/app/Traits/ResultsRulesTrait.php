<?php

namespace App\Traits;

trait ResultsRulesTrait
{
    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public static function rules(): array
    {
        return [
            'metric' => ['required', 'string'],
            'value' => ['required', 'numeric'],
            
            'train_dataset'=> ['required', 'array'],
            'validation_dataset'=> ['nullable', 'array'],
            'test_dataset'=> ['required', 'array'],
            
            'train_dataset.id' => ['required', 'integer', 'exists:datasets,id'],
            'validation_dataset.id' => ['required', 'integer', 'exists:datasets,id'],
            'test_dataset.id' => ['required', 'integer', 'exists:datasets,id'],
        ];
    }
}