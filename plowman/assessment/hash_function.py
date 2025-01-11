def sieve(limit):

    if limit < 2:

        return []

    if limit == 2:

        return [False, True]

    if limit == 3:

        return [False, True, True]



    #BEFORE: res = [False]
    res = [False] * (limit + 1)

    if limit >= 2:

        res[2] = True

    if limit >= 3:

        res[3] = True



    for i in range(4, limit + 1):

        res[i] = False



    i = 1

    while i <= limit:

        j = 1

        while j <= limit:



            n = (4 * i * i) + (j * j)

            if (n <= limit and (n % 12 == 1 or

                                n % 12 == 5)):

                res[n] ^= True



            n = (3 * i * i) + (j * j)

            if n <= limit and n % 12 == 7:

                res[n] ^= True



            n = (3 * i * i) - (j * j)

            if (i > j and n <= limit and

                    n % 12 == 11):

                res[n] ^= True

            j += 1

        i += 1



    r = 5

    while r * r <= limit:

        if res[r]:

            for i in range(r * r, limit + 1, r * r):

                res[i] = False



        r += 1

    #ADDED
    primes = []
    for a in range(0, limit + 1):
        if res[a]:
            primes.append(a)

    return primes



def pick_prime(primes, min_size=1000):

    """returns a suitable prime to use as modulus"""

    for prime in primes:

        if prime >= min_size:

            return prime

    # if no prime large enough exists, use last one on list

    return primes[-1]



def hash(string, modulus):

    hash_value = 0
    p, m = 31, modulus
    length = len(string)
    p_pow = 1
    for i in range(length):
        hash_value = (hash_value + (1 + ord(string[i]) - ord('a')) * p_pow) % m
        p_pow = (p_pow * p) % m

    return hash_value


if __name__ == '__main__':

    # generate primes list to use as modulus

    primes = sieve(1000) # modify limit based on your needs
    print(primes)
    print(primes[-1])


    modulus = pick_prime(primes, 100)


    test_array = ["alpha","beta","gamma","delta","epsilon"]



    for string in test_array:

        hash_value = hash(string, modulus)

        print(f"Hash of {string} is {hash_value}")
