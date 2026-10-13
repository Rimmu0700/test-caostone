<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('feedback_corrections', function (Blueprint $table) {
            $table->id('feedback_id');
            $table->unsignedBigInteger('classification_id');
            $table->unsignedBigInteger('curator_id');
            $table->unsignedInteger('corrected_species_id');
            $table->text('correction_note')->nullable();
            $table->timestamp('created_at')->useCurrent();

            $table->index('classification_id');
            $table->foreign('classification_id')->references('classification_id')->on('classification_results')->cascadeOnDelete();
            $table->foreign('curator_id')->references('user_id')->on('users')->restrictOnDelete();
            $table->foreign('corrected_species_id')->references('species_id')->on('species')->restrictOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('feedback_corrections');
    }
};
