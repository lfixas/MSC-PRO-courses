export function objectsDeeplyEqual(cmp1, cmp2) {
    if (cmp1 === cmp2) { // "returns true only if: they have the same value ;" => true
        return true;
    }
    if (typeof cmp1 !== 'object' || typeof cmp2 !== 'object' || cmp1 === null || cmp2 === null) { // If either value is not an object, they are objects => false
        return false;
    }
    var keys1 = Object.keys(cmp1);
    var keys2 = Object.keys(cmp2);
    if (keys1.length !== keys2.length) { // Check if they have the same number of keys ("here", "object", then "is")
        return false;
    }
    for (var k = 0; k < keys1.length; k++) { // Check if all keys in cmp1 exist in cmp2 and have deeply equal values
        var key = keys1[k];
        if (!cmp2.hasOwnProperty(key) || !objectsDeeplyEqual(cmp1[key], cmp2[key])) { // "whose values are also equal when compared with a recursive call to objectsDeeplyEqual"
            return false;
        }
    }
    return true; // ALl conditions pass
}