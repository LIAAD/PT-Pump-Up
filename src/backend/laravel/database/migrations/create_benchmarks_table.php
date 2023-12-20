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
        Schema::create('benchmarks', function (Blueprint $table) {
            $table->id();
            $table->longText('metric');
            $table->float('performance');
            $table->foreignId('ml_model_id');
            $table->foreignId('train_dataset_id')->references('id')->on('datasets');
            $table->foreignId('validation_dataset_id')->references('id')->on('datasets');
            $table->foreignId('test_dataset_id')->references('id')->on('datasets');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('benchmarks');
    }
};
