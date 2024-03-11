<?php

namespace App\Traits;
use App\Models\Author;
use App\Models\NlpTask;

trait StoreResourceTrait
{
    public static function create_authors($resource, $author_emails){
        
        foreach ($author_emails as $author_email) {
            $author_id = Author::join('links', 'authors.link_id', '=', 'links.id')
                            ->where('email', $author_email)
                            ->firstOrFail()
                            ->id;
                            
            $resource->authors()->attach($author_id);
        }
    }

    public static function create_nlp_tasks($resource, $nlp_tasks_short_names){
       
        foreach($nlp_tasks_short_names as $nlp_task_short_name) {
            $nlp_task_id = NlpTask::where('short_name', $nlp_task_short_name)
                                ->firstOrFail()
                                ->id;

            $resource->nlpTasks()->attach($nlp_task_id);
        }
    }

}