const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str) {
    //SETUP
//need a variable to hold the encoded string we build
//variable that stores current character in string
//variable to hold the count
    var newString = "";
    var count = 0;

//WORK
//loop through the string
    //compare the currCharVariable to the char at the current index of the string
    //if they are the same, increase the count of the count variable
    //compare the currCharVariable to the char at the current index in the string to see if it doesn't match
        //add the currChar and the count to the encoded string
        //reset the count
        //set the currCharVariable to the next letter
    for(var i =0; i <str.length; i++){
        if(str.charAt(i+1) == str.charAt(i)){ 
            count += 1;
        }
        else{
            count += 1;
            newString += str[i] + count.toString();
            count=0;
        }
    }
//RETURN
//compare the lengths of the endcoded string to the original
    //if the encoded is shorter, return encoded
    //if the encoded is not shorter, return the original
    if(newString.length == str.length || str.length == 1){
        return str;
    }
    else{
        return newString;
    }
}

console.log(encodeStr(str1))
console.log(encodeStr(str2))
console.log(encodeStr(str3))
console.log(encodeStr(str4))

const str5 = "a3b2c12d10"
const expected5 = "aaabbccccccccccccdddddddddd"


// FIX THIS CODE
function decodeStr(str) {
    //SETUP
    //decoded string variable
    var decoded = "";
    var numStr = "";
    var i = 0;

//WORK
//loop through the string
while (i < str.length) {
    //we want to grab the character at the current index
    var letter = str[i]
    numStr = "";

    //we can use a loop to add charcters to the decoded string the num amount of times
    // look ahead to find potentially multiple digits after letter
    while (i < str.length && !isNaN(parseInt(str[i]))){
        numStr += str[i];
        i++
    }
    decoded += letter.repeat(numStr);
}
return decoded
}

console.log(decodeStr(str5))