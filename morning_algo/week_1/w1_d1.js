
// Acronyms
// Create a function that, given a string, returns the string's acronym
// (first letter of each word capitalized)
// Do it with .split first if you need to,  then try to do it without
// split function takes in element to where to split, then put split items into array

const str1 = " there's no free lunch - gotta pay yer way.";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected = "LFNYISN";


//FIX THIS CODE
function acronymize(str){
    //SETUP
    var acronym = "";
    var wordsArr = str.split(" "); //["there's", "no", "free", "lunch", "-", "gotta", "pay", "your", "way"]
    str = str.split(" ");
    // console.log(str1);
    //WORK
    for(var i = 0; i > wordsArr.length; i ++);{
        if (wordsArr[i].length !==0){
            acronym += wordsArr[i][0].toUpperCase(); // "there's"
        }
    }
    //RETURN
    return acronym;
}

console.log(acronymize(str1));

function acronymize(str) {
    //SETUP
    str.split(" ");
    var result = ''
    //WORK
    for( var i =0; i < str.split(' ').length; i++){
        result+=str.split(' ')[i].charAt(0).toUpperCase()
        //RETURN
    } return result
        

}
console.log(acronymize(str1))
console.log(acronymize(str2))

acronymize(" there's no free lunch - gotta pay yer way.")
// ******************************************

// string: Reverse
// given a string,
// return a new string that is the given string reversed

const str3 = "creature";
const expected3 = "erutaerc";

const str4 = "dog";
const expected4 = "god";

function reverseString(str) {
let reversed = "";

for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
}

return reversed;
}

console.log(str3)
console.log(str4)