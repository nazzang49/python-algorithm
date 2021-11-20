from bisect import bisect_left # binary search module

numbers = [2, 7, 11, 15]
target = 9

for k, v in enumerate(numbers): # sum of two numbers
    expected = target - v
    i = bisect_left(numbers, expected, lo=k + 1) # lo = low / hi = high (default => len(numbers))
    if i < len(numbers) and numbers[i] == expected:
        print(k + 1, i + 1)