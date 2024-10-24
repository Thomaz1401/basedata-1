<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Product;

class ProductController extends Controller
{
    public function index(){ //$product=Product::find(2);
        $products=Product::all();
        return view('list', compact('products'));
     }

    public function create (){

        return view('create');

    }
    public function store(Request $request){
    
            
            $product= new Product();
            $product->name=$request->name;
            $product->description=$request->description;
            $product->price=$request->price;
            $product->save();
            return $product;
        }
}
