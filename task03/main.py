import timeit
from tabulate import tabulate
from boyer_moore import boyer_moore
from kmp import kmp_search
from rabin_karp import rabin_karp

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=100)

if __name__ == "__main__":
    text1 = read_file('article_1.txt')
    text2 = read_file('article_2.txt')

    # Define patterns for testing
    patterns = {
        "existing": "алгоритм",
        "non_existing": "вимишленийпідрядок"
    }

    results = []

    # Measure the performance for each pattern and each text
    for pattern_type, pattern in patterns.items():
        for i, text in enumerate([text1, text2], 1):
            bm_time = measure_time(boyer_moore, text, pattern)
            kmp_time = measure_time(kmp_search, text, pattern)
            rk_time = measure_time(rabin_karp, text, pattern)

            results.append((f"Article {i} - {pattern_type}", bm_time, kmp_time, rk_time))

    # Prepare the results for tabulation
    table = []
    headers = ["Test Case", "Boyer-Moore (s)", "KMP (s)", "Rabin-Karp (s)"]

    for result in results:
        article, bm_time, kmp_time, rk_time = result
        table.append([article, f"{bm_time:.6f}", f"{kmp_time:.6f}", f"{rk_time:.6f}"])

    # Print the results
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))