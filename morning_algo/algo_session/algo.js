//Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
//Can you help him to find out, how many cakes he could bake considering his recipes?

//Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). 
//For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
//Ingredients that are not present in the objects, can be considered as 0.

function cakes(recipe, available) {
    // SETUP
    let minCount = Infinity;
    
    // WORK
    // Loop through the recipe
    for (const ingredient in recipe) {
      // check if the ingredient is in the pantry
    if (available.hasOwnProperty(ingredient)) {
        // how many recipe measures of the ingredient are available
        let count = Math.floor(available[ingredient] / recipe[ingredient]);

        // if the count is 0, then we dont have enough of the ingredient
        // so we exit early
        if (count < 1) return 0;

        // if the count is less than minCount, then reassign minCount
        if (count < minCount) minCount = count;
    } 
      // if the ingredient is NOT in the pantry, the return 0, meaning we cannot make the recipe
    else {
        return 0
    }
    }

    // RETURN
    return minCount
}

  // must return 2
console.log(cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})); 
  // must return 0
console.log(cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})); 