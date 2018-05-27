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
    
    print(prime_list)
    

if __name__ == '__main__':
    getPrimeNumber(1000000)