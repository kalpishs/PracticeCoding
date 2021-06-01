def maxSum(a):
    n = len(a)
    if n == 1:
        return a[0]
    sum1 = 0
    flag = 0

    for i in range(n):
        if i == 0 and a[i] < 0:
            sum1 += a[i]
            flag = 1
            continue
        if flag == 0:
            sum1 = sum1 + a[i]
            if i+1 < n and a[i+1] < 0:
                flag = 1
                continue
        if flag == 1:
            sum1 = sum1 - a[i]
            if i+1 < n and a[i+1] > 0:
                flag = 0
                continue
    return sum1


if __name__ == "__main__":
    # The intial array, -1 is for
    # 1 base indexing
    a = [-7 ,3 ,-3 ,1 ,-8]
    print(maxSum(a))