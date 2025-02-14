function range(start, end, step) {
    if (step === undefined) {
        step = 1;
    }
    var array = [];
    if (step >0) {
        for (var n = start; n <= end; n += step) {
            array.push(n)
        }
    } else {
        for (var n = start; n >= end; n += step) {
            array.push(n)
        }
    }
    return array;
}
module.exports.range = range;