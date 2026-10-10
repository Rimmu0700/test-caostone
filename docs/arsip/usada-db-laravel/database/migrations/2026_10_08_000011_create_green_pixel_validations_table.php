<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('green_pixel_validations', function (Blueprint $table) {
            $table->id('validation_id');
            $table->unsignedBigInteger('session_id')->unique(); // relasi 1:0..1
            $table->decimal('green_pixel_ratio', 5, 4);
            $table->decimal('threshold', 5, 4);
            $table->string('validation_status', 30);
            $table->timestamp('validated_at')->useCurrent();

            $table->foreign('session_id')->references('session_id')->on('identification_sessions')->cascadeOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('green_pixel_validations');
    }
};
