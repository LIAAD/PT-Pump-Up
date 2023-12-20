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
        Schema::create('hrefs', function (Blueprint $table) {
            $table->id();
            $table->string('email')->nullable();
            $table->string('website')->nullable();
            $table->string('orcid')->nullable();
            $table->string('github')->nullable();
            $table->string('twitter')->nullable();
            $table->string('google_scholar')->nullable();
            $table->string('linkedin')->nullable();
            $table->string('link_source')->nullable();
            $table->string('link_hf')->nullable();
            $table->string('link_papers_with_code')->nullable();
            $table->string('doi')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('hrefs');
    }
};
