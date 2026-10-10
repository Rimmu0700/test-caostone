<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('identification_sessions', function (Blueprint $table) {
            $table->id('session_id');
            $table->unsignedBigInteger('user_id');
            $table->timestamp('captured_at')->nullable();
            $table->string('session_status', 30)->default('pending');
            $table->string('detection_status', 30)->default('pending');
            $table->boolean('photo_consent')->default(false);
            $table->timestamp('created_at')->useCurrent();

            $table->index(['user_id', 'created_at']);
            $table->index('session_status');
            $table->foreign('user_id')->references('user_id')->on('users')->cascadeOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('identification_sessions');
    }
};
