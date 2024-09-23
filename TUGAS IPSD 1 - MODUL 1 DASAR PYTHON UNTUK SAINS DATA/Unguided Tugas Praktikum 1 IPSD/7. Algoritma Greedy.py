def minimum_coin_change(amount, coins):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        count = amount // coin
        result.extend([coin] * count)
        amount -= coin * count
    return result

# Contoh penggunaan
amount = 90
coins = [1, 5, 10, 25]
print(minimum_coin_change(amount, coins))