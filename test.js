var indivisible = require('./indivisible');
var assert = require('assert');

var fs = require('fs');

fs.readFile('./prime_numbers.csv', 'utf-8', function(err, data) {
  if (err) throw err;
  else {
    // Parse all the comma-separated numbers into an array of integers
    var fileContents = (data.toString('utf-8')).split(',');
    var primeNumbers = fileContents.map(function(num) {
      return parseInt(num.trim());
    });
    // make sure we loaded something from the file
    assert.equal(primeNumbers.length > 0, true);
    // run tests with these numbers
    runTests(primeNumbers);
  }
});

function runTests(numbers) {

  var numbersMin = numbers[0];
  var numbersMax = numbers[numbers.length - 1];

  console.log('Testing all integers from', numbersMin, 'to', numbersMax, 'against list of prime numbers from Wikipedia.');

  for (var i = 2; i <= numbersMax; i++) {
    if (numbers.indexOf(i) >= 0)
      assert.equal(indivisible.isPrime(i), true);
    else assert.equal(indivisible.isPrime(i), false);
  }

  console.log('OK!');

  console.log('Testing queries for n number of prime numbers, n =', numbersMin, 'to n =', numbersMax + '.');

  for (var j = 1; j <= numbers.length; j++) {
    // get i number of prime numbers
    var gottenPrimeNumbers = indivisible.getHowManyPrimeNumbers(j);
    // make sure the prime numbers we got are the same as an equivalent subset of the reference prime numbers
    assert.deepEqual(gottenPrimeNumbers, numbers.slice(0, j));
    // make sure the number of prime numbers we got is the same as the number requested
    assert.deepEqual(gottenPrimeNumbers.length, j);
  }

  console.log('OK!');

  console.log('Done. All korrect!');

}
