<?php

namespace App\Http\Controllers;

use App\Invoice;
use App\Models\UserModel;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Maatwebsite\Excel\Facades\Excel;
use Rap2hpoutre\FastExcel\FastExcel;

class ExcelController extends Controller
{
     public function import(Request $request)
    {
        $request->validate([
            'excelFile' => 'required|mimes:xlsx|max:10240',  // Adjust the max file size as needed
        ]);

        $file = $request->file('excelFile');
        $name = $request->input('nama');
        $nim = $request->input('nim');
        $akdm_stat = $request->input('akdm_stat');

        // Process the file and import data
        $users = (new FastExcel)->import($file, function ($line) {
            return UserModel::create([
                'ta' => $line['ta'],
                'kdmk' => $line['kdmk'],
                'id_jadwal' => $line['id_jadwal'],
                'nim' => $line['nim'],
                'sts' => $line['sts'],
                'sks' => $line['sks'],
            ]);
        });

        DB::table('test_2023_11_11_2')->insert([
                'nim' => $name,
                'nama' => $nim,
                'akdm_stat' => $akdm_stat,

        ]);

        return redirect()->back()->with('success', 'Data imported successfully!');
    }

    public function index(){
        return view('search');
    }

    function fetch(Request $request)
{
    if ($request->get('query')) {
        $query = $request->get('query');
        $data = DB::table('dataexcel')
            ->where('nim', 'LIKE', "%{$query}%")
            ->get();
        $output = '<ul class="dropdown-menu" style="display:block; position:relative;width:100%;">';
        foreach ($data as $row) {
            $output .= '
                <li><a class="dropdown-item" href="#">' . $row->nim . '</a></li>
                ';
        }
        $output .= '</ul>';
        echo $output;
    }
}


}
