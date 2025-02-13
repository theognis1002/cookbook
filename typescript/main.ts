const nested: number[][] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

const flattenedArray = nested.flat();
console.log(flattenedArray);  // [1, 2, 3, 4, 5, 6, 7, 8, 9]

const flattenedArray2 = nested.reduce((acc, curr) => {
    return acc.concat(curr);
}, []);
console.log(flattenedArray2);  // [1, 2, 3, 4, 5, 6, 7, 8, 9]

const flattenedArray3 = nested.flatMap((item) => item);
console.log(flattenedArray3);  // [1, 2, 3, 4, 5, 6, 7, 8, 9]
