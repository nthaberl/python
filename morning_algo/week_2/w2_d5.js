/* 
    Given a string that may have extra spaces at the start and the end,
    return a new string that has the extra spaces at the start and the end trimmed (removed)
    do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
 function trim(str) {
    startIn = 0
    EndIn = str.length
    for(var i = 0; i < str.length; i++){
        if (str[i] != " "){
            startIn = i
            break
        }
    }
    for(var i = str.length-1; i > -1; i--){
        if (str[i] != " "){
            EndIn = i
            break
        }
    }
return str.slice(startIn, EndIn+1)
}

console.log(trim(str1))

/*****************************************************************************/

/* 
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    Is there a quick way to determine if they aren't an anagram before spending more time?
    Given two strings
    return whether or not they are anagrams
*/

const strA1 = "yes";
const strB1 = "eys";
const expected1 = true;

const strA2 = "yes";
const strB2 = "eYs";
const expected2 = true;

const strA3 = "no";
const strB3 = "noo";
const expected3 = false;

const strA4 = "silent";
const strB4 = "listen";
const expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
 function frequencyTableBuilder(str) {
    var dict={}
    str = str.toLowerCase()
    for(var i=0; i<str.length; i++){
        if(! dict.hasOwnProperty(str[i])){
            dict[str[i]]=1
        }
        else{
            dict[str[i]]+=1
        }
    } return dict

}

function isAnagram(s1, s2) {
    
    s1Dict = frequencyTableBuilder(s1)
    s2Dict = frequencyTableBuilder(s2)
    s1Keys = Object.keys(s1Dict)
    for(var i = 0; i<s1Keys.length; i++){
        if(s1Dict[s1Keys[i]] != s2Dict[s1Keys[i]]){
            return false
        }
    }
    return  true

}

console.log(isAnagram(strA1, strB1))
console.log(isAnagram(strA2, strB2))
console.log(isAnagram(strA3, strB3))
console.log(isAnagram(strA4, strB4))