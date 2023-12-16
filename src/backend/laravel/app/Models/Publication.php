<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use MongoDB\Laravel\Eloquent\Model;
use App\Models\Conference;


class Publication extends Model
{
    use HasFactory;

    # The attributes that are mass assignable.
    protected $fillable = [];

    # One publication belongs to many authors.
    public function authors()
    {
        return $this->belongsToMany(Author::class);
    }

    # One publication belongs to One MLModel or Dataset.
    public function ml_model()
    {
        return $this->belongsTo(MLModel::class);
    }

    # One publication belongs to One MLModel or Dataset.
    public function dataset()
    {
        return $this->belongsTo(Dataset::class);
    }

    # One publication belongs to many NLPTasks.
    public function nlp_tasks()
    {
        return $this->belongsToMany(NLPTask::class);
    }

    # One publication belongs to one Conference.
    public function conference()
    {
        return $this->belongsTo(Conference::class);
    }
}
