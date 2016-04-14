from indivisible import is_prime, get_how_many_prime_numbers

# Get Wikipedia-sourced/copy-pasted prime numbers against which to test
with open('prime_numbers.csv', 'r') as f:
    read_data = f.read()

# make sure we closed that file
assert(f.closed)

prime_numbers = [] # container for the prime numbers parsed from the file

# parse and push the numbers into the list container
for s in read_data.split(','):
    prime_numbers.append(int(s))

# make sure we loaded something from the file
assert len(prime_numbers) > 0

numbers_min = min(prime_numbers)
numbers_max = max(prime_numbers)

print 'Testing all integers from %d to %d against list of prime numbers from Wikipedia.' % (numbers_min, numbers_max)

for i in range(2, numbers_max):
    if i in prime_numbers:
        assert is_prime(i)
    else:
        assert not is_prime(i)

print 'OK!'

print 'Testing queries for n number of prime numbers, n = %d to n = %d.' % (numbers_min, numbers_max)

for i in range(1, len(prime_numbers) + 1):
    # get i number of prime numbers
    gotten_prime_numbers = get_how_many_prime_numbers(i)
    # make sure the prime numbers we got are the same as an equivalent subset of the reference prime numbers
    assert gotten_prime_numbers == prime_numbers[:i]
    # make sure the number of prime numbers we got is the same as the number requested
    assert len(gotten_prime_numbers) == i

print 'OK!'

print 'Done. All korrect!'
