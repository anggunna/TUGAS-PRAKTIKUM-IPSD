def is_prime(n): 
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_pattern(n):
    primes = []
    num = 2
    while len(primes)< n * (n + 1) // 2 :
        if is_prime(num):
            primes.append(num)
        num +=1
    
    result = []
    for i in range(n):
        row = primes[:i+1]
        result.append(row)
        primes = primes[i+1:]
    return result

# Contoh penggunaan
n = 4
pattern = generate_pattern(n)
for row in pattern:
    print(' '.join(map(str, row)))