def big_number(N, M, K, store):
    store.sort(reverse=True)

    first = store[0]
    second = store[1]
    rs = 0

    while M > 0:
        for _ in range(K):
            if M == 0:
                break
            rs += first
            M -= 1
        if M == 0:
            break
        rs += second
        M -= 1

    return rs

N, M, K = map(int, input().split())
store = list(map(int, input().split()))

print(big_number(N, M, K, store))


"""
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count += m %(k+1)

result = 0
result += count * first
result += (m-count) * second
"""