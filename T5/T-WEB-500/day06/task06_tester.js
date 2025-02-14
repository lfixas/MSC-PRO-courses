import { objectsDeeplyEqual } from './tasks/task06.js';
const obj = { here: { is: "an" }, object: 2 };
console.log(objectsDeeplyEqual(obj, obj));
console.log(objectsDeeplyEqual(obj, { here: 1, object: 2 }));
console.log(objectsDeeplyEqual(obj, { here: { is: "an" }, object: 2 }));