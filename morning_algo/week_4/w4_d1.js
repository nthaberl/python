/* 
    Recursion --> calling a function that calls on itself

    Base case --> function does not make a recursive call
    Recursive case --> function makes a recursive call

    Head recursion --> recursive call takes place at the top of the function
        f(3) = 
            f(2) =
                f(1) =
                    f(0) = "Liftoff"
                1
            2
        3

    Tail recursion --> recursive call takes place at the bottom of the function
        f(3) = 3
            f(2) = 2
                f(1) = 1
                    f(0) = "liftoff"

*/

// function fun (){
//     console.log("call to function")
//     fun()
// }

// fun()

// function countdown(num){
//     if (num == 0){
//         //BASE CASE
//         console.log("Liftoff")
//     }
//     else{
//         //RECURSIVE CASE
//         console.log(num)
//         countdown(num - 1)
//     }
// }

// countdown (10)

/* 
    Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums1) {
    if (nums1.length == 0){
        return 0;
    }
    else{
        return nums1[0] + sumArr(nums1.slice(1));
    }
}

console.log(sumArr(nums1))

/*****************************************************************************/

/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num2 = 5;
const expected2 = 15;
// Explanation: (1+2+3+4+5)

const num3 = 2.5;
const expected3 = 3;
// Explanation: (1+2)

const num4 = -1;
const expected4 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function recursiveSigma(num) {
    num = Math.floor(num)
    if (num <= 0){
        console.log(0)
        return 0
    }
    else{
        // console.log (`${num} + recursiveSigma(${num - 1}) = `)
        return num + recursiveSigma(num - 1)
    }
}
console.log(recursiveSigma(num2))
console.log(recursiveSigma(num3))
console.log(recursiveSigma(num4))
