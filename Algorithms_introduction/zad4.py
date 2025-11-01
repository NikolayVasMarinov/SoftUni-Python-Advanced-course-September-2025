def choose_coins(coins, target) -> str:
    coins.sort(reverse=True)
    used_coins: dict[int, int] = {}

    i: int = 0
    while target != 0 and i < len(coins):
        ct = target // coins[i]
        target %= coins[i]

        if ct > 0:
            used_coins[coins[i]] = ct

        i += 1

    if target != 0:
        return "Error"

    result = f"Number of coins to take: {sum(used_coins.values())}"

    for coin, count in used_coins.items():
        result += f"\n{count} coin(s) with value {coin}"

    return result

coins_list: list[int] = list(map(int, input().split(", ")))
desired_sum: int = int(input())

print(choose_coins(coins_list, desired_sum))