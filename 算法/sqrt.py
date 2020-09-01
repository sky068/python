# 求平方根，保留s位小数 二分查找，数值大了计算很慢
def sqrt(n, s):
    low = 0
    hight = n
    f = 1/pow(10, s)
    while low <= hight:
        mid = (low + hight) / 2
        t = mid * mid 
        if abs(t-n) <= f:
            return round(mid, s)
        elif t < n:
            low = mid 
        else:
            hight = mid

# 牛顿弦切法 速度非常快
def sqrt2(n, s):
    f = 1 / pow(10, s)
    xini = n / 2
    while xini*xini - n > f:
        # xini = (n + xini * xini)/2/xini
        xini = (xini + n/xini) / 2

    return round(xini, s)

from datetime import datetime
start = datetime.now().timestamp()*1000000
if __name__ == "__main__":
    n = 9999801919
    print(sqrt2(n, 6))
    print(datetime.now().timestamp()*1000000 - start)
    # print(sqrt(n, 6))


