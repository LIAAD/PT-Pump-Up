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
            'train_dataset_id' => ['required', 'integer', 'exists:datasets,id'],
            'validation_dataset_id' => ['nullable', 'integer', 'exists:datasets,id'],
            'test_dataset_id' => ['nullable', 'integer', 'exists:datasets,id'],
        ];
    }
}