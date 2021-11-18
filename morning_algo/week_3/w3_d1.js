/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visited indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */
function socialDistancingEnforcer(queue) {
    var counter = 0
    for(var i = 0; i < queue.length; i++){
        if (counter === 6){
            break;
        }
        if(queue[i] == 1){
            counter = 0
        }
        if(queue[i] == 0){
            counter += 1
        }
        console.log(counter)
    }
    if (counter < 6) {
        return false
    }
    else{
        return true
    }
}

console.log(socialDistancingEnforcer(queue1))
console.log(socialDistancingEnforcer(queue2))

/*****************************************************************************/

/* 
Balance Index
Here, a balance point is ON an index, not between indices.
Return the balance index where sums are equal on either side
// (exclude its own value).

// Return -1 if none exist.

// */

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function sumfunction(start, stop, array){
    var sum = 0
    for(var i = start; i<stop +1; i++){
        sum += array[i]
    }
    return sum
}
function balanceIndex(nums) {
    for(var i = 1; i<nums.length-1; i++){
        if(sumfunction(0,i-1,nums)== sumfunction(i+1,nums.length-1,nums)){
            return i
        }
    }
    return -1
}

console.log(balanceIndex(nums1))
console.log(balanceIndex(nums2))