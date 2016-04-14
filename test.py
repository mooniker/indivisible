from indivisible import is_prime, get_how_many_prime_numbers

# # check some basic prime numbers
# assert is_prime(3) == True
# assert is_prime(4) == False
# assert is_prime(7) == True
# assert is_prime(9) == False
# assert is_prime(10) == False
# assert is_prime(11) == True
# assert is_prime(95) == False
# assert is_prime(101) == True
#
# first_168_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
#
# assert get_how_many_prime_numbers(168) == first_168_prime_numbers
#
# for i in range(1, 168 + 1):
#     assert get_how_many_prime_numbers(i) == first_168_prime_numbers[:i]
#
# print 'All passed.'

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
