<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use App\Traits\AuthorRulesTrait;
use App\Traits\LinkRulesTrait;
use App\Traits\ResourceStatsRulesTrait;


class StoreMachineLearningModelRequest extends FormRequest
{
    use AuthorRulesTrait;
    use LinkRulesTrait;
    use ResourceStatsRulesTrait;

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
        
        foreach (AuthorRulesTrait::rules() as $key => $value) {
            $author_rules['authors.*' . $key] = $value;
            unset($author_rules[$key]);
        }

        foreach (LinkRulesTrait::rules() as $key => $value) {
            $link_rules['link.' . $key] = $value;
            unset($link_rules[$key]);
        }

        foreach (ResourceStatsRulesTrait::rules() as $key => $value) {
            $resource_stats_rules['resource_stats.' . $key] = $value;
            unset($resource_stats_rules[$key]);
        }


        return array_merge([
            'short_name' => ['required', 'string'],
            'full_name' => ['nullable', 'string'],
            'description' => ['nullable', 'string'],
            'year' => ['required', 'integer'],
            
            'link' => ['required', 'array'],
            'resource_stats' => ['required', 'array'],
            
            'authors' => ['required_without:author_ids', 'nullable', 'array'],
            'author_ids' => ['required_without:authors', 'nullable', 'array'],
            'author_ids.*' => ['required', 'integer', 'exists:authors,id'],

            'nlp_task_ids' => ['required', 'array'],
            'nlp_task_ids.*' => ['required', 'integer', 'exists:nlp_tasks,id'],

        ], $author_rules, $link_rules, $resource_stats_rules);    
    }
}
