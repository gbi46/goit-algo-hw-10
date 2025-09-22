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
