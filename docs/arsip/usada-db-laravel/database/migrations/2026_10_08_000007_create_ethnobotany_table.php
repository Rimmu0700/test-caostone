<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('ethnobotany', function (Blueprint $table) {
            $table->increments('ethnobotany_id');
            $table->unsignedInteger('species_id')->unique(); // relasi 1:1 dengan species
            $table->text('traditional_benefits')->nullable();
            $table->text('plant_parts_used')->nullable();
            $table->text('usage_method')->nullable();
            $table->string('verification_status', 30)->default('pending');
            $table->unsignedBigInteger('verified_by')->nullable();
            $table->timestamp('verified_at')->nullable();
            $table->timestamp('updated_at')->useCurrent();

            $table->foreign('species_id')->references('species_id')->on('species')->cascadeOnDelete();
            $table->foreign('verified_by')->references('user_id')->on('users')->nullOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('ethnobotany');
    }
};
