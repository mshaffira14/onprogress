<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Rap2hpoutre\FastExcel\FastExcel;
use App\User;

class UserModel extends Model
{
    use HasFactory;
    protected $table = 'dataexcel';
    // protected $fillable = ['ta,kdmk,sks,nim,sts'];
    protected $guarded = ['created_at', 'updated_at'];
        public $timestamps = false;

}

?>