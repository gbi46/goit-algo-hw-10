from colorama import init, Fore
from lib import find_coins_greedy, find_min_coins, monte_carlo_integration, print_task_header

import scipy.integrate as spi
import time

init(autoreset=True)

print_task_header(1)
print(Fore.CYAN + "=== Greedy and dynamic programming algorithms comparison ===")

COINS = [50, 25, 10, 5, 2, 1]

test_amounts = [1, 1_000, 7, 5_000, 23, 10_000, 99, 50_000, 123, 100_000, 512, 200_000]
for amount in test_amounts:
    start_greedy_time = time.perf_counter()

    greedy_result = find_coins_greedy(amount, COINS)
    end_greedy_time = time.perf_counter() - start_greedy_time

    start_dynamic_time = time.perf_counter()
    min_coins_result = find_min_coins(amount, COINS)
    end_dynamic_time = time.perf_counter() - start_dynamic_time

    print(f"Amount: {amount}")
    print(f"  Greedy result: {greedy_result}, time: {end_greedy_time:.10f} sec")
    print(f"  Min coins result: {min_coins_result}, time: {end_dynamic_time:.10f} sec")

print_task_header(2)
print(Fore.CYAN + "=== Monte Carlo integration ===")

# Example function to integrate
def func(x):
    return x ** 2

# Integration limits
a, b = 0, 2

# Monte Carlo integration
result_mc = monte_carlo_integration(func, a, b)
print(f"Monte Carlo integration result of x^2 from {a} to {b}: {result_mc}")

# Exact integration using quad
result_exact, error = spi.quad(func, a, b)
print(f"Quad result:", result_exact, "with error estimate:", error)

# Compare results
print(f"Difference between Monte Carlo and Quad: {abs(result_mc - result_exact)}")
