//define 
var edit = document.getElementsByClassName("btn_edit")[0];
//
var cmpt = document.getElementsByClassName("btn_cpt")[0];

var elete = document.getElementsByClassName("btn_delete")[0];

edit.onclick = function(){
    edit.style.display ="none";
    elete.style.display ="none";
    cmpt.style.backgroundColor ="hsl(123, 69%, 41%)";
}

//
//define 
var edit = document.getElementsById("edit")[1];
//
var cmpt = document.getElementsById("cpt")[1];

var elete = document.getElementsById("delete")[1];

edit.onclick = function(){
    edit.style.display ="none";
    elete.style.display ="none";
    cmpt.style.backgroundColor ="hsl(123, 69%, 41%)";
}