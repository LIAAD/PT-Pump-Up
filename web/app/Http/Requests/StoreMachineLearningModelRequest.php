<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use App\Traits\LinkRulesTrait;
use App\Traits\ResourceStatsRulesTrait;
use App\Traits\ResultsRulesTrait;


class StoreMachineLearningModelRequest extends FormRequest
{
    use LinkRulesTrait;
    use ResourceStatsRulesTrait;
    use ResultsRulesTrait;
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
        
        foreach (ResultsRulesTrait::rules() as $key => $value) {
            $result_rules['results.*' . $key] = $value;
            unset($result_rules[$key]);
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
            'results' => ['nullable', 'array'],
            
            'author_emails' => ['required', 'nullable', 'array'],
            'author_emails.*' => ['required', 'email', 'exists:links,email'],

            'nlp_tasks_short_names' => ['required', 'array'],
            'nlp_tasks_short_names.*' => ['required', 'string', 'exists:nlp_tasks,short_name'],

        ], $link_rules, $resource_stats_rules, $result_rules);    
    }
}
