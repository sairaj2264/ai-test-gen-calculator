const calc = require("../src/calculator");

test("adds two numbers", () => {
  expect(calc.add(2, 3)).toBe(5);
});
