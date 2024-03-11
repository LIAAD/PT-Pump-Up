<?php

namespace App\Traits;


trait AuthorRulesTrait
{
    use LinkRulesTrait;
    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public static function rules(): array
    {
        foreach(LinkRulesTrait::rules() as $key => $value){
            $link_rules['link.' . $key] = $value;
            unset($link_rules[$key]);
        }

        return array_merge([
            'name' => ['required', 'string'],
            'institution' => ['required', 'string'],
            'link' => ['required', 'array'],
        ], $link_rules);
    }
}