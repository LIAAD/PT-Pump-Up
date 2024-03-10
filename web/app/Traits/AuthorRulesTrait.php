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
            #TODO: Simplify Link Id is unlikely to be used
            'link_id' => ['required_without:link', 'nullable', 'integer', 'exists:links,id'],
            'link' => ['required_without:link_id', 'nullable', 'array'],
        ], $link_rules);
    }
}