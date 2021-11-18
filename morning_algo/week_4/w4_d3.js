/*
Recursive Binary Search
Input: SORTED array of ints, int value
Output: bool representing if value is found
Recursively search to find if the value exists, do not loop over every element.
Approach:
Take the middle item and compare it to the given value.
Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */

//Nate's Method
 function binarySearch(sortedNums, searchNum, i = Math.floor(sortedNums.length/2)) {
  if(sortedNums[i]==searchNum){
      return true
  }
  else if( sortedNums.length == 0){
      return false
  }
  else if (sortedNums[i] > searchNum){
      return binarySearch(sortedNums.slice(0, i), searchNum)
  }
  else if (sortedNums[i] < searchNum){
      return binarySearch(sortedNums.slice(i+1,sortedNums.length), searchNum)

  }
}
console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))



function binarySearch(sortedNums, searchNum, leftIdx = 0, rightIdx = sortedNums.length -1) {
  if (leftIdx > rightIdx){
    return false;
  }
  var midIdx = Math.floor((rightIdx + leftIdx)/2);

  if (sortedNums[midIdx] === searchNum){
    return true;
  }
  if (searchNum < sortedNums [midIdx]){
    return binarySearch(sortedNums, searchNum, leftIdx, midIdx - 1); //looks to the left
  } else {
    return binarySearch(sortedNums, searchNum, midIdx +1, rightIdx); //looks to the right
  }
}

/*****************************************************************************/

/* 
  Recursively reverse a string
  helpful methods:
  str.slice(beginIndex[, endIndex])
  returns a new string from beginIndex to endIndex exclusive
*/

const str4 = "abc";
const expected4 = "cba";

const str5 = "";
const expected5 = "";

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
function reverseStr(str) {
if (str === ""){
  return ""
}
else{
  return reverseStr(str.substr(1)) + str.charAt(0);
}
}

console.log(reverseStr(str4))
console.log(reverseStr(str5))