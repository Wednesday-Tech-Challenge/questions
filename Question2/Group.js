// Your code goes here

function pal(str){
        var re = /[\W_]/g;
        var lowRegStr = str.toLowerCase().replace(re, '');
        var reverseStr = lowRegStr.split('').reverse().join(''); 
        return reverseStr === lowRegStr;
     
}




// Test Cases
pal ("mom");


