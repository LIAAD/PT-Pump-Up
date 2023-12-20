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
        Schema::create('datasets', function (Blueprint $table) {
            $table->id();
            $table->longText('english_name');
            $table->longText('full_portuguese_name')->nullable();
            $table->longText('description');
            $table->integer('year');
            $table->string('status');
            $table->foreignId('href_id');
            $table->foreignId('resource_stats_id');
            $table->foreignId('introduced_by_id');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('datasets');
    }
};
