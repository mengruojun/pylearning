import logging
import time
import sys
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def getPrimeNumber(limit=None):
    i = 2
    prime_list = [2]

    while True:
        i += 1
        if(limit != None and i > limit): break

        is_prime = True
        for prime in prime_list:
            if(i % prime ==0):
                """this is not a prmie, then continue"""
                is_prime = False
                break
        
        if(is_prime == False): continue
        else: 
            """not break, then it is a prime, add it to the prime_list"""
            prime_list.append(i)
    
    logging.debug(prime_list)
    return prime_list
    

if __name__ == '__main__':
    start = time.time()
    logging.info("Start")
    if(len(sys.argv) == 1): limit = 100
    else: 
        limit = int(sys.argv[1])

    prime_list = getPrimeNumber(limit)
    end = time.time()
    logging.info("End")
    logging.info("Finished in " + str(end - start) + " Seconds")
    logging.info("Max Prime in rang is " + str(prime_list[-1]))
