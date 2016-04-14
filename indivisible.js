
function isPrime(n) {
  // Check to make sure number isn't even and isn't less than 2.
  if (n % 2 === 0 && n > 2)
    return false
  // Check to see if every odd number from 3 to one greater than
  // the square root of n evenly divide into n. If any of them
  // do so, return False.
  for (var i = 3; i < Math.ceil(Math.sqrt(n)); i += 2) {
    if (n % i === 0)
      return false;
  } // Otherwise
  return true;
}

function getHowManyPrimeNumbers(n) {
  var i = 2;
  var results = [];
  while (true) {
    if (isPrime(i))
      results.push(i);
    if (results.length >= n)
      return results;
    i++;
  }
}
