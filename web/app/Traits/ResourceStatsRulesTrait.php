<?php

namespace App\Traits;

trait ResourceStatsRulesTrait
{
    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public static function rules(): array
    {
        return [
            'preservation_rating' => ['required', 'string', 'in:low,medium,high'],
            'standard_format' => ['nullable', 'boolean'],
            'off_the_shelf'=> ['required', 'boolean'],
        ];
    }
}