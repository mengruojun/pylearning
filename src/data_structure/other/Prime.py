"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> get_prime_number()
97
"""
import logging
import time
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


def get_prime_number(cap=100):

    i = 2
    prime_list = [2]

    while True:
        i += 1
        if cap is not None and i > cap:
            break

        is_prime = True
        for prime in prime_list:
            if i % prime == 0:
                """this is not a prime, then continue"""
                is_prime = False
                break

        if not is_prime:
            continue
        else:
            """not break, then it is a prime, add it to the prime_list"""
            prime_list.append(i)

    logging.debug(prime_list)
    max_prime = prime_list[-1]
    return max_prime


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    start = time.time()
    logging.info("Start")
    if len(sys.argv) == 1:
        limit = 100
    else:
        limit = int(sys.argv[1])
    logging.info("Max Prime in rang is " + str(get_prime_number(limit)))
    end = time.time()
    logging.info("End")
    logging.info("Finished in " + str(end - start) + " Seconds")

