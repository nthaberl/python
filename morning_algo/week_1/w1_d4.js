    /* 
    String: Is Palindrome
    Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards

    Do not ignore spaces, punctuation and capitalization
    */

    const str1 = "a x a";
    const expected1 = true;

    const str2 = "racecar";
    const expected2 = true;

    const str3 = "Dud";r
    const expected3 = false;

    const str4 = "oho!"; 
    const expected4 = false;

    /**
     * Determines if the given str is a palindrome (same forwards and backwards).
     * - Time: O(?).
     * - Space: O(?).
     * @param {string} str
     * @returns {boolean} Whether the given str is a palindrome or not.
     */
    function isPalindrome(str) {
        for (var i = 0; i <= Math.floor(str.length/2); i++){ //math.floor for shits and giggles
            console.log(str[i]);
                if(str[i] != str[str.length - 1 - i]){
                    return false;
                }
            }
        return true;
        }

    console.log(isPalindrome (str1))
    console.log(isPalindrome (str2))
    console.log(isPalindrome (str3))
    console.log(isPalindrome (str4))
    /*****************************************************************************/

    /* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
    */

    // const str1 = "what up, daddy-o?";
    // const expected1 = "dad";

    // const str2 = "uh, not much";
    // const expected2 = "u";

    // const str3 = "Yikes! my favorite racecar erupted!";
    // const expected3 = "e racecar e";

    // const str4 = "a1001x20002y5677765z";
    // const expected4 = "5677765";

    // const str5 = "a1001x20002y567765z";
    // const expected5 = "567765";

    /**
     * Finds the longest palindromic substring in the given string.
     * - Time: O(?).
     * - Space: O(?).
     * @param {string} str
     * @returns {string} The longest palindromic substring from the given string.
     */
    function longestPalindromicSubstring(str) {
    var substring = "";
    // Loop through the string
        // Loop through the rest of the string to grab all possible sub strings
        // isPalirome(subStr) to check if the sub string is a palindrome
            // if true, if its the longest panlindrome
            for (var i = 0; i <= str.length; i++){
                if(str[i] != str[str.length - 1 - i]){
                    return false;
                }
                else{
                    return true;
                }
            }
    // RETURN
    }