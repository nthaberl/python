
// Acronyms
// Create a function that, given a string, returns the string's acronym
// (first letter of each word capitalized)
// Do it with .split first if you need to,  then try to do it without
// split function takes in element to where to split, then put split items into array

const str1 = " there's no free lunch - gotta pay yer way.";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected = "LFNYISN";

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

acronymize(" there's no free lunch - gotta pay yer way.")
// ******************************************

// string: Reverse
// given a string,
// return a new string that is the given string reversed

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

function reverseString(str) {
let reversed = "";

for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
}

return reversed;
}