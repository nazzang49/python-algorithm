n = int(input())

# map(function, list) => element of list converted through function
k_list = list(map(int, input().split()))
print(f'{min(k_list)} {max(k_list)}')