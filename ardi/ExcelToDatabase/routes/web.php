<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ExcelController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::post('/xlsx' ,[ExcelController::class, 'import'])->name('import');
Route::get('/autocomplete', [ExcelController::class, 'index']);
Route::post('/autocomplete/fetch', [ExcelController::class, 'fetch'])->name('autocomplete.fetch');
