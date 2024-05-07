def change_money(money):
    change = [500, 100, 50, 10]
    cnt = 0
    for coin in change:
        cnt += money // coin
        money %= coin
    return cnt


money = int(input())
print(change_money(money))