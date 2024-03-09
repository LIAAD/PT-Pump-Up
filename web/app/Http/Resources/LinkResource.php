<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class LinkResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'email' => $this->email,
            'website' => $this->website,
            'github_url' => $this->github_url,
            'hugging_face_url' => $this->hugging_face_url,
            'papers_with_code_url' => $this->papers_with_code_url,
            'paper_url' => $this->paper_url,
        ];
    }
}
