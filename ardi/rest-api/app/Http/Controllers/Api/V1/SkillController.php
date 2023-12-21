<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Resources\V1\SkillCollection;
use App\Http\Resources\V1\SkillResource;
use App\Models\Skills;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\Http\Requests\StoreSkillRequest;

class SkillController extends Controller
{
    public function index(){
        return new SkillCollection(Skills::paginate(10));
    }

    public function show(Skills $skill){
        return new SkillResource($skill);
    }

    public function destroy(Skills $skill){
        $skill->delete();
        return response()->json('data berhasil dihapus');
    }


    public function store(StoreSkillRequest $request){
        Skills::create($request->validated());
        return response()->json('skill created');
    }

    public function update(StoreSkillRequest $request,Skills $skill){
        $skill->update($request->validated());
        return response()->json('skill updated');
    }
}
