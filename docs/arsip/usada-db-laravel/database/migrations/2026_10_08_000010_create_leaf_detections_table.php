<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('leaf_detections', function (Blueprint $table) {
            $table->id('detection_id');
            $table->unsignedBigInteger('session_id');
            $table->decimal('confidence', 5, 4);
            $table->decimal('bbox_x', 10, 4);
            $table->decimal('bbox_y', 10, 4);
            $table->decimal('bbox_width', 10, 4);
            $table->decimal('bbox_height', 10, 4);
            $table->string('detection_status', 30);
            $table->string('crop_image_url', 500)->nullable();
            $table->timestamp('detected_at')->useCurrent();

            $table->index('session_id');
            $table->foreign('session_id')->references('session_id')->on('identification_sessions')->cascadeOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('leaf_detections');
    }
};
