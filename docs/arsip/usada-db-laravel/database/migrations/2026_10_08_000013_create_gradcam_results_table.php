<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('gradcam_results', function (Blueprint $table) {
            $table->id('gradcam_id');
            $table->unsignedBigInteger('classification_id')->unique(); // relasi 1:0..1
            $table->string('heatmap_url', 500);
            $table->timestamp('generated_at')->useCurrent();

            $table->foreign('classification_id')->references('classification_id')->on('classification_results')->cascadeOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('gradcam_results');
    }
};
