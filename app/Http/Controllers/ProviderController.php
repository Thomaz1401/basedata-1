<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ProviderController extends Controller
{
    public function index2(){ //$product=Product::find(2);
        $provider=Provider::all();
        return view('list', compact('products'));
     }
     
     public function create2 (){

        return view('create2');

    }
    public function store2(Request $request){
    
            $provider= new Product();
            $provider->name=$request->name;
            $provider->description=$request->description;
            $provider->price=$request->price;
            $provider->save();
            return $provider;
        }
}
