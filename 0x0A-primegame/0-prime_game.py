#!/usr/bin/python3

def sieve(n):
    """Generate list of primes up to n using the Sieve of Eratosthenes"""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes


def isWinner(x, nums):
    """Determine the winner of the Prime Game"""
    if not nums or x < 1:
        return None

    # Max n in nums to precompute primes up to that number
    max_n = max(nums)

    # Precompute primes up to max_n
    primes = sieve(max_n)

    # Calculate the number of primes up to each n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Maria's and Ben's win count
    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
