import math

def fermat_factorization(n):
    if n <= 0:
        return "Input must be a positive integer"
    if n % 2 == 0:
        return [2, n // 2]

    a = math.isqrt(n)
    if a * a < n:
        a += 1

    b2 = a * a - n
    while not is_perfect_square(b2):
        a += 1
        b2 = a * a - n

    b = int(math.isqrt(b2))
    return [a - b, a + b]

def is_perfect_square(k):
    root = math.isqrt(k)
    return root * root == k

def main():
    try:
        n = int(input("Enter an odd number to factorize: "))
        factors = fermat_factorization(n)
        print(f"Factors of {n} are: {factors}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
