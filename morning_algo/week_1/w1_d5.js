/* 
Zip Arrays into Map


Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = [
    "favorite_food",
    "favorite_beverage",
    "favorite_song",
    "favorite_animal",
];
const vals2 = ["chicken", "pink lemonade", "national anthem", "dog"];
const expected2 = {
    favorite_food: "chicken",
    favorite_beverage: "pink lemonade",
    favorite_song: "national anthem",
    favorite_animal: "dog",
};

/**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */
function zipArraysIntoMap(keys, values) {
    // SETUP
    var dic = {};
    // WORK
    // loop thru both at the same time
    for (var i = 0; i < keys.length; i++) {
      // key1 index will be key val1 will be the value
dic[keys[i]] = values[i];
    }
    // RESULT
    return dic;
}

console.log(zipArraysIntoMap(keys1, vals1))
console.log(zipArraysIntoMap(keys2, vals2))

/*****************************************************************************/

/* 
    Invert Hash
    A hash table / hash map is an obj / dictionary
    Given an object / dict,
    return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
  */

const obj3 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected3 = { Zaphod: "name", high: "charm", dicey: "morals" };

/**
   * Inverts the given object's key value pairs so that the original values
   * become the keys and the original keys become the values.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Object<string, string>} obj An object with string keys and string values.
   * @return The given object with key value pairs inverted.
   */
function invertObj(obj) {
    // SETUP
    var inverted = {};

    // WORK
    // loop through the object
    for (var key in obj) {
    var value = obj[key];

    inverted[value] = key;
    }

    // RETURN
    return inverted;
}

console.log(invertObj(obj3))