<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('images', function (Blueprint $table) {
            $table->id('image_id');
            $table->unsignedBigInteger('session_id');
            $table->string('image_type', 30);
            $table->string('storage_url', 500);
            $table->string('file_format', 20);
            $table->unsignedBigInteger('file_size')->nullable(); // bytes
            $table->timestamp('uploaded_at')->useCurrent();

            $table->index('session_id');
            $table->foreign('session_id')->references('session_id')->on('identification_sessions')->cascadeOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('images');
    }
};
