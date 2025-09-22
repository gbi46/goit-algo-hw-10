from colorama import init, Fore

def find_coins_greedy(amount, coins=[]):
    """Greedy change-making algorithm. Returns a dict {denomination: count}."""
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    
    result = {}
    remaining = amount
    for c in sorted(coins, reverse=True):
        if remaining == 0:
            break
        k = remaining // c
        if k > 0:
            result[c] = k
            remaining -= k * c
    return dict(sorted(result.items(), key=lambda kv: kv[0]))

def find_min_coins(amount, coins=[]):
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

init(autoreset=True)

def print_task_header(task_number: int):
    print(Fore.GREEN + "=========================")

    for i in range(6):
        if i == 3:
            print(Fore.GREEN + "=" + Fore.YELLOW + " " * 8 + f"Task {task_number}" + Fore.GREEN + " " * 9 + "=")
        else:
            print(Fore.GREEN + "=                       =")
    print(Fore.GREEN + "=========================")
