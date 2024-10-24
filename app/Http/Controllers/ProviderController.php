<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ProviderController extends Controller
{
    public function index1(){ //$product=Product::find(2);
        $provider=Product::all();
        return view('product.list', compact('products'));
     }
     
     public function create (){

        return view('create');

    }
    public function store(Request $request){
    
            return $request;
            $provider= new Product();
            $provider->name=$request->name;
            $provider->description=$request->description;
            $provider->price=$request->price;
            $provider->save();
            return $provider;
        }
}
