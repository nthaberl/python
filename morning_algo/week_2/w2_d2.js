// given a string return a new string with the duplicates excluded
//Bonus: keep only the last instance of each character

const str1 = "abcABC";
const expected = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "abcafaqabcazzAABB";
const expected = "abcfqzAB";

function Dedupe(str){
    //need to track what letters have already been seen
    freqTable = {}
    for(var i = 0; i < str.length; i++){
        var char = str[i]
        if(freqTable.hasOwnProperty(char)){
            freqTable[char] += 1
        }
        else{
            freqTable = 1
        }
    }
    return Object.keys(freqTable).join("")
}

console.log(Dedupe(str1))
//OR
// if(!freqTable.hasOwnProperty(char)){
//     freqTable[char] = True
// }
//OR
// returnStr += char
//OR
function stringDedupe(str) {
    var dic = {}
    var result = ""

    for (var i=0; i<str.length; i++ ){
        if (str[i] in dic) {
            continue

        }
        else {
            dic[str[i]] = 1 
            result += str[i]
        }
        
    }
return result

  // We need to track what letters have been seen already
}

//given a string containing space separated by wprds
//reverse each word in the string
//if you need to, use .split to start, then try without

const str4 = "hello";
const expected4 = "olleh";

const str5 = "hello world";
const expected5 = "olleh dlrow";

const str6 = "abc def ghi";
const expected6 = "cba fed ihg";

function flipword(str){
    var result = ""
    for (var i = str.length-1; i>-1; i--){
            result += str[i]
    }
    return result
}

function reverseWords(str) {
    var myArr = str.split(" ");
    var result =  ""
    for (var i = 0; i<myArr.length-1; i++){
        result += flipword(myArr[i])
        result += " "
    }
    result += flipword(myArr[myArr.length-1])
    return result 
}

console.log(reverseWords(str4))
console.log(reverseWords(str5))
console.log(reverseWords(str6))