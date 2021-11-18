const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.


function parensValid(str) {
    open_paren = 0
    close_paren = 0
    for (var i=0; i< str.length; i++){
        if (str[i] == "(" ){
            open_paren += 1
        }
        else if (str[i] == ")"){
            close_paren+= 1
        }
        if (open_paren < close_paren){
            return false
        }
    }
    if (close_paren == open_paren){
        return true
    }
    else{
        return false
    }
}

console.log(parensValid(str3))

OR 

function parensValid(str) {
    // we can try to keep count of the number of opening parens as compared to closing parens
    freqTable = {};
    for (let i = 0; i<str.length; i++){
        char = str[i];
        if (freqTable['('] < freqTable[')']){ // checks to see if more closing parens are started compared to opening
        return false
        }
    if(char === '('){
        if(freqTable.hasOwnProperty('(')){
            freqTable['('] += 1;
        } else {
            freqTable['('] = 1;
        }
    } else if (char === ')') {
        if(freqTable.hasOwnProperty(')')){
          freqTable[')'] += 1;
        } else {
          freqTable[')'] = 1;
        }
      }
    } return freqTable['('] === freqTable[')'];
}

console.log(parensValid(str1))
console.log(parensValid(str2))
console.log(parensValid(str3))
console.log(parensValid(str4))




/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str4 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected4 = true;

const str5 = "D(i{a}l[ t]o)n{e";
const expected5 = false;

const str6 = "A(1)s[O (n]0{t) 0}k";
const expected6 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var openingBraceStack = []
    var opens = "({["
    var closeToOpen = {
        ")": "("
        "}" : "{"
        "]" : "["
    }
for (var i = 0; i < str.length; i++){
    var currentChar = str[i]
    //if statement checks is currentChar is an opening brace
    if (openingBraceStack.includes(currentChar)) //searching through string of opens for currentChar
    stack.push(currentChar)
    }
     //elseif statement checks is currentChar is an opening brace
    else if (current in closeToOpen){
        if (closeToOpen[currentChar] === openingBraceStack[openingBraceStack.length - 1]){
            stack.pop();
        }else{
            return false;
        }
}

return openingBraceStack.length === 0;
}

OR 

function make_sub(str, bracket, index){
    var result = ""
    for (var h = index + 1; h<str.length; h++){
        if (str[h] == bracket){
            return result
        }
        else{
            result +=str[h]
        }
    }
    return false
}
function bracesValid(str) {
    open_paren = 0
    open_bracket = 0
    open_curly = 0
    close_paren = 0
    close_bracket = 0
    close_curly = 0
    sub_string = ""
    for (var i = 0; i < str.length; i++){
        if (str[i] == "("){
            sub_string = make_sub(str,")", i)
        }
        else if(str[i] == "["){
            sub_string = make_sub(str,"]", i)
        }
        else if (str[i] == "{"){
            sub_string = make_sub(str,"}", i)
        }
    }
}