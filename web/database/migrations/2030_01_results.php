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
        Schema::dropIfExists('results');
        
        Schema::create('results', function (Blueprint $table) {
            $table->id();
            $table->string('metric');
            $table->float('value');
            $table->foreignId('machine_learning_model_id');
            $table->foreignId('train_dataset_id');
            $table->foreignId('validation_dataset_id')->constrained('datasets')->nullable();
            $table->foreignId('test_dataset_id');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('results');
    }
};
