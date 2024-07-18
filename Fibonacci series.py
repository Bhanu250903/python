def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series
num_terms = 10
print(f"fibonacci series up to{num_terms} terms:")
print(fibonacci_series(num_terms))
