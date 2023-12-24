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
        Schema::disableForeignKeyConstraints();

        Schema::create('ml_models', function (Blueprint $table) {
            $table->id();
            $table->longText('english_name');
            $table->longText('full_portuguese_name')->nullable();
            $table->longText('description');
            $table->integer('year');
            $table->string('architecture');
            $table->foreignId('href_id')->constrained()->cascadeOnDelete()->cascadeOnUpdate();
            $table->foreignId('resource_stats_id')->constrained('resource_stats')->cascadeOnDelete()->cascadeOnUpdate();
            $table->foreignId('add_by_id')->constrained('users')->cascadeOnDelete()->cascadeOnUpdate();
            $table->timestamps();
        });

        Schema::enableForeignKeyConstraints();
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('ml_models');
    }
};
