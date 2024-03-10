<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class AuthorResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'institution' => $this->institution,
            'link_id' => $this->link_id,
            'link' => LinkResource::make($this->whenLoaded('link')),
            'machineLearningModels' => MachineLearningModelCollection::make($this->whenLoaded('machineLearningModels')),
        ];
    }
}
