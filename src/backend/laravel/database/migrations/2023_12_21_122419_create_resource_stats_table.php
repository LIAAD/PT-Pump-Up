<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('resource_stats', function (Blueprint $table) {
            $table->id();
            $table->boolean('broken_link');
            $table->boolean('author_response');
            $table->boolean('standard_format');
            $table->boolean('backup');
            $table->float('size_gb')->nullable();
            $table->string('preservation_rating')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('resource_stats');
    }
};
