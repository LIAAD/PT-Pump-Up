<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Support\Facades\Auth;

class StoreAuthorRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return Auth::check();
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            'name' => 'required|string',
            'affiliation' => 'required|string',
            'hrefs' => 'required|array',
            'hrefs.email' => 'required|email|unique:authors,email',
            'hrefs.website' => 'nullable|url',
            'hrefs.orcid' => 'nullable|url',
            'hrefs.github' => 'nullable|url',
            'hrefs.twitter' => 'nullable|url',
            'hrefs.googleScholar' => 'nullable|url',
            'hrefs.linkedin' => 'nullable|url',
        ];
    }
}
