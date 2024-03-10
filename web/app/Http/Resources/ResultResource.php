<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class ResultResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'metric' => $this->metric,
            'value' => $this->value,
            'machine_learning_model_id' => $this->machine_learning_model_id,
            'train_dataset_id' => $this->train_dataset_id,
            'validation_dataset_id' => $this->validation_dataset_id,
            'test_dataset_id' => $this->test_dataset_id,
        ];
    }
}
