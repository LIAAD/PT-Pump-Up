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
        Schema::create('nlp_tasks', function (Blueprint $table) {
            $table->id();
            $table->string('short_name')->unique();
            $table->string('full_name')->nullable()->unique();
            $table->longText('description')->nullable();
            $table->string('standard_format');
            $table->json('papers_with_code_ids');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('nlp_tasks');
    }
};
