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
        Schema::create('machine_learning_models', function (Blueprint $table) {
            $table->id();
            $table->string('short_name');
            $table->string('full_name');
            $table->longText('description');
            $table->integer('year');
            $table->foreignId('link_id');
            $table->foreignId('resource_stats_id');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('machine_learning_models');
    }
};
