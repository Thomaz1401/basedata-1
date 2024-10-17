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
        Schema::create('basedata', function (Blueprint $table) {
            $table->id();
            $table->string('categories');
            $table->string('posts');
            $table->string('users');
            $table->string('images');
            $table->integer('post_tag');
            $table->integer('tags');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('basedata');
    }
};
