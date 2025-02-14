export function arrayFiltering(array, test) {
    const filteredArray = [];
    for (let i = 0; i < array.length; i++) {
        if (test(array[i])) {
            filteredArray.push(array[i]);
        }
    }
    return filteredArray;
}