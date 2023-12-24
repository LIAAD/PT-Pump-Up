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

        Schema::create('benchmarks', function (Blueprint $table) {
            $table->id();
            $table->longText('metric');
            $table->float('performance');
            $table->foreignId('ml_model_id')->constrained()->cascadeOnDelete()->cascadeOnUpdate();
            $table->foreignId('train_dataset_id')->references('id')->on('datasets')->constrained()->cascadeOnDelete()->cascadeOnUpdate();
            $table->foreignId('validation_dataset_id')->nullable()->references('id')->on('datasets')->constrained()->cascadeOnDelete()->cascadeOnUpdate();
            $table->foreignId('test_dataset_id')->references('id')->on('datasets')->constrained()->cascadeOnDelete()->cascadeOnUpdate();
            $table->timestamps();
        });

        Schema::enableForeignKeyConstraints();
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('benchmarks');
    }
};
