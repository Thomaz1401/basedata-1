<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('j_a_t_s');
    }
public function up()
{
    Schema::create('JATS', function (Blueprint $table) {
        $table->id();
        $table->string('name');
        $table->string('email');
        $table->string('phone');
        $table->string('service_type');
        $table->string('vehicle');
        $table->text('details')->nullable();
        $table->timestamps();
    });
}

};
