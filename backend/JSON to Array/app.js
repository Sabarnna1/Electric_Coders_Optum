//const { response } = require('express');
//const express=require('express');
//const app=express();
//const fetch=require('node-fetch');
//import fetch from 'cross-fetch';
import fetch from 'node-fetch';
import express from 'express';
const app=express();


// const userAction = async () => {
// const response = await fetch('https://optum-analysis.herokuapp.com/immunizer');
// const myJson = await response.json();
// const data=JSON.parse(myJson);

// console.log(data);
// }

let x=[];
let y=[];

fetch('https://optum-analysis.herokuapp.com/immunizer')
//use require link with the endpoints like allergies,medicine etc
.then(response=>{
    //console.log(response.json());
    return response.json();
}).then(data=>{
   // console.log(data.immunizations);
   return JSON.parse(JSON.stringify(data));
})
.then(data=>{
    //console.log(Array.isArray(data.immunizations));
    data.immunizations.forEach(element => {
        x.push(element.count);
        y.push(element.immunizer);
    });
    console.log(x);
    console.log(y);
    //console.log(data);
}).catch(err=>{
    console.log(err);
})

app.listen(3000,()=>{
    console.log("Listing on port 3000");
})
