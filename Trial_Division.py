import math

def trial_division(n):
    if n <= 1:
        return []
    
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors

def main():
    try:
        n = int(input("Enter an integer to factor: "))
        factors = trial_division(n)
        print(f"Prime factors of {n} are: {factors}")
    except ValueError:
        print(" Please enter a valid integer.")

if __name__ == "__main__":
    main()
