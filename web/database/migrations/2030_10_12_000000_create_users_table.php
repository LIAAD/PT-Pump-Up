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
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->string('linkedin')->nullable();
            $table->string('github')->nullable();
            $table->string('huggingface')->nullable();
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            #Role only can be user, moderator, or admin
            $table->string('role')->default('user')->constraint(['user', 'moderator', 'admin']);
            $table->foreignId('photo_id')->nullable()->constrained(table: 'files');
            $table->rememberToken();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('users');
    }
};
