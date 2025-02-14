export function countGs(str) {
    let countG = 0;
    for (let s = 0; s <= str.length; s++) {
        if (str[s] === 'G') {
            countG ++;
        }
    }
    return countG;
}