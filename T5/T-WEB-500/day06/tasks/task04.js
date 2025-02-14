export function fizzBuzz(num) {
    let array = [];
    for (let n = 1; n <= num; n++) {
        let result = '';
        if (n % 3 === 0) {
            result += 'Fizz';
        }
  
        if (n % 5 === 0) {
            result += 'Buzz';
        }
        array.push(result || n);
    }
    console.log(array.join(', '));
}