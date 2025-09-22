from colorama import init, Fore
from lib import find_coins_greedy, find_min_coins, print_task_header

init(autoreset=True)

print_task_header(1)
print(Fore.CYAN + "=== Greedy and dynamic programming algorithms comparison ===")

COINS = [50, 25, 10, 5, 2, 1]

test_amounts = [1, 3, 7, 14, 23, 30, 99, 100, 123, 256, 512]
for amount in test_amounts:
    greedy_result = find_coins_greedy(amount, COINS)
    min_coins_result = find_min_coins(amount, COINS)
    print(f"Amount: {amount}")
    print(f"  Greedy result: {greedy_result}")
    print(f"  Min coins result: {min_coins_result}")
