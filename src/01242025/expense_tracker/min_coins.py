from collections import defaultdict


def how_many_ways(m, coins):
    memo = defaultdict(int)
    memo[0] = 1
    for coin in coins:
        for i in range(coin, m + 1):
            memo[i] += memo[i - coin]
    return memo[m]


memo = {}


def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def minimum_coins_botton_up(m, coins):
    memo = {}
    memo[0] = 0
    for i in range(1, m + 1):
        for coin in coins:
            if coin <= i:
                memo[i] = min_ignore_none(memo[i], memo[i - coin] + 1)
    return memo[m]


def minimum_coins(m, coins):
    if m in memo:
        return memo[m]

    if m <= 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = minimum_coins(m - coin, coins)
            if subproblem < 0:
                continue
            answer = min_ignore_none(answer, subproblem + 1)
    memo[m] = answer
    return answer


print(minimum_coins(150, [1, 4, 5]))

## Time complity O(M*K)
