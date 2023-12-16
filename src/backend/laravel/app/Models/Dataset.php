<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use MongoDB\Laravel\Eloquent\Model;
use App\Models\Helpers\LanguageStats;
use App\Models\Author;
use App\Models\NLPTask;
use App\Models\Helpers\HRefs;
use App\Models\Helpers\ResourceStatus;


class Dataset extends Model
{
    use HasFactory;

    # The attributes that are mass assignable.
    protected $fillable = [
        '_id',
        'english_name',
        'full_portuguese_name',
        'description',
        'introduction_date',
    ];

    # One Dataset has many LanguageStats.
    public function language_stats()
    {
        return $this->hasMany(LanguageStats::class);
    }

    # One Dataset has many Authors.
    public function authors()
    {
        return $this->hasMany(Author::class);
    }

    # One Dataset has many NLPTasks.
    public function nlp_tasks()
    {
        return $this->hasMany(NLPTask::class);
    }

    # One Dataset has one HRefs.
    public function hrefs()
    {
        return $this->hasOne(HRefs::class);
    }

    # One Dataset has one ResourceStatus.
    public function resource_status()
    {
        return $this->hasOne(ResourceStatus::class);
    }
}
