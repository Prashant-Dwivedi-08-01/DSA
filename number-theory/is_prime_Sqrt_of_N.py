"""
The naïve way to do is very simple. We just check if the given number is divisible by any numbers in 
the range of 1 to n, and if only 1 and n are the numbers which divide n, then the given number n is a prime.

* BTTER: We only check the numbers in the range 1 to sqrt(n).
This optimization works because , factors come in pairs.
For example , for number 21 , if we know 3 is a factor than we know 7 is also a factor, as 3*7 = 21
Time: O(sqrt(N))

"""
def is_prime(n):
 
    if (n <= 1):
        return False
 
    for i in range(2, int(n**(0.5)+1)):
        if (n % i == 0):
            return False
 
    return True

def find_primes(n):

    primes = []
    if n < 2:
        return primes

    for i in range(2,int(n+1)):
        if is_prime(i):
            primes.append(i)

    return primes

"""
Sieve method to find all the primes in range of 1 to n ? O( n log (log n) )

LOGIC: https://medium.com/@harshitdaga7/sieve-of-eratosthenes-finding-prime-numbers-upto-n-4d1f9ccac953#:~:text=Sieve%20method%20to%20find%20all%20the%20primes%20in%20range%20of%201%20to%20n%20%3F%20O(%20n%20log%20(log%20n)
"""
def sieve_prime(n):


    is_prime = [True for i in range(int(n+1))]
    primes = []


    if n < 2 :
        return primes

    for i in range(2,int(n+1)):

        if is_prime[i]:
            j = 2
            while j*i <= n:
                is_prime[j*i] = False
                j+=1 

            primes.append(i)


    return primes
    
if __name__ == "__main__":
    print(is_prime(29))
    print(find_primes(50)) #* O(N*sqrt(N))