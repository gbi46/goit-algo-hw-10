from colorama import init, Fore

import numpy as np

def find_coins_greedy(amount, coins=None):
    """Greedy change-making algorithm. Returns a dict {denomination: count}."""
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")

    coins = tuple(sorted(coins, reverse=True))
    
    result = {}
    remaining = amount
    for c in coins:
        k, remaining = divmod(remaining, c)
        if k:
            result[c] = k
        if remaining == 0:
            break
    return dict(sorted(result.items()))

def find_min_coins(amount, coins=None):
    """Dynamic programming (minimum number of coins). Returns a dict {denomination: count}."""
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    if amount == 0:
        return {}
    INF = 10**18
    dp = [0] + [INF] * amount
    last = [-1] * (amount + 1)
    for i in range(1, amount + 1):
        best = INF
        best_coin = -1
        for c in coins:
            if i - c >= 0 and dp[i - c] + 1 < best:
                best = dp[i - c] + 1
                best_coin = c
        dp[i] = best
        last[i] = best_coin
    if dp[amount] >= INF:
        raise ValueError("Cannot form the amount with given coins")
    res = {}
    x = amount
    while x > 0:
        c = last[x]
        if c == -1:
            raise RuntimeError("Solution reconstruction failed")
        res[c] = res.get(c, 0) + 1
        x -= c
    return dict(sorted(res.items(), key=lambda kv: kv[0]))

def monte_carlo_integration(func, a, b, num_samples=100000):
    """
    Monte Carlo integration method

    Parameters:
    func : callable
        The function to integrate. It should take a single argument.
    a : float
        The start of the integration interval.
    b : float
        The end of the integration interval.
    num_samples : int
        The number of random samples to use for the estimation.

    Returns:
    float
        Approximate value of the integral.
    """

    # Generate x random points in the interval [a, b]
    x_random = np.random.uniform(a, b, num_samples)

    # Evaluate the function at x_random points
    y_random = func(x_random)

    # Compute the approximate integral using the average value
    integral_estimate = (b - a) * np.mean(y_random)
    return integral_estimate

init(autoreset=True)

def print_task_header(task_number: int):
    print(Fore.GREEN + "=========================")

    for i in range(6):
        if i == 3:
            print(Fore.GREEN + "=" + Fore.YELLOW + " " * 8 + f"Task {task_number}" + Fore.GREEN + " " * 9 + "=")
        else:
            print(Fore.GREEN + "=                       =")
    print(Fore.GREEN + "=========================")
