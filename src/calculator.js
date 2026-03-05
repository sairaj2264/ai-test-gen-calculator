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

module.exports = {
  add,
  subtract,
  multiply,
  divide,
  power,
  modulo,
};
function power(a, b) {
  return a ** b;
}

function power(a, b) {
  return a ** b;
}

module.exports = {
  add,
  subtract,
  multiply,
  divide,
  power,
};

function modulo(a, b) {
  if (b === 0) {
    throw new Error("Modulo by zero");
  }
  return a % b;
}
