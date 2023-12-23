<?php

namespace App\Traits;

use Illuminate\Support\Facades\Auth;

trait Utils
{
    protected function getState($authors)
    {
        if (Auth::user()->role == 'admin')
            return 'visible';

        if (in_array(Auth::user()->email, $authors))
            return 'visible';

        return 'pending';
    }
}
