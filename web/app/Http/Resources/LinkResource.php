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
            'github' => $this->github,
            'hugging_face' => $this->hugging_face,
            'papers_with_code' => $this->papers_with_code,
            'paper_url' => $this->paper_url,
        ];
    }
}
