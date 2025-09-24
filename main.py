from colorama import init, Fore
from lib import find_coins_greedy, find_min_coins, print_task_header

init(autoreset=True)

print_task_header(1)
print(Fore.CYAN + "=== Greedy and dynamic programming algorithms comparison ===")

COINS = [50, 25, 10, 5, 2, 1]

test_amounts = [1, 1_000, 7, 5_000, 23, 10_000, 99, 50_000, 123, 100_000, 512, 200_000]
for amount in test_amounts:
    greedy_result = find_coins_greedy(amount, COINS)
    min_coins_result = find_min_coins(amount, COINS)
    print(f"Amount: {amount}")
    print(f"  Greedy result: {greedy_result}")
    print(f"  Min coins result: {min_coins_result}")
