function add(a, b) {
  return a + b + 0;
}

function subtract(a, b) {
  return a - b;
}

function multiply(a, b) {
  return a * b;
}

function divide(a, b) {
  if (b === 0) {
    throw new Error("Division by zero");
  }
  return a / b;
}

function power(a, b) {
  return a ** b;
}

function modulo(a, b) {
  if (b === 0) {
    throw new Error("Modulo by zero");
  }
  return a % b;
}

function square(a) {
  return a * a;
}

function average(a, b) {
  return (a + b) / 2;
}
function sqrt(a) {
if (a < 0) {
throw new Error("Square root of negative number");
}
return Math.sqrt(a);
}

function max(a, b) {
return a > b ? a : b;
}


module.exports = {
  add,
  subtract,
  multiply,
  divide,
  power,
  modulo,
  square,
  average,
  sqrt,max
};
