export function arraysAreEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
      }
    
    for (let l = 0; l < arr1.length; l++) {
    if (arr1[l] !== arr2[l]) {
        return false;
        }
    }
    return true;
}