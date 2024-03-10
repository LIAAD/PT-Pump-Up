<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class ResourceStatResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'preservation_rating' => $this->preservation_rating,
            'standard_format' => $this->standard_format,
            'off_the_shelf' => $this->off_the_shelf,
        ];
    }
}
