<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class MachineLearningModelStoreRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     */
    public function rules(): array
    {
        return [
            'short_name' => ['required', 'string'],
            'full_name' => ['required', 'string'],
            'description' => ['required', 'string'],
            'year' => ['required', 'integer'],
            'created_at' => ['required'],
            'updated_at' => ['required'],
            'link_id' => ['required', 'integer', 'exists:links,id'],
        ];
    }
}
