<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('classification_results', function (Blueprint $table) {
            $table->id('classification_id');
            $table->unsignedBigInteger('session_id')->unique(); // relasi 1:0..1 sesuai ERD
            $table->unsignedInteger('species_id');
            $table->decimal('confidence_score', 5, 4);
            $table->string('result_status', 30);
            $table->string('model_name', 100);
            $table->string('model_version', 50);
            $table->timestamp('classified_at')->useCurrent();

            $table->index('species_id');
            $table->foreign('session_id')->references('session_id')->on('identification_sessions')->cascadeOnDelete();
            $table->foreign('species_id')->references('species_id')->on('species')->restrictOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('classification_results');
    }
};
