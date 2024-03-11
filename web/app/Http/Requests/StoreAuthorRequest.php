<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use App\Traits\LinkRulesTrait;

class StoreAuthorRequest extends FormRequest
{
    use LinkRulesTrait;

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
