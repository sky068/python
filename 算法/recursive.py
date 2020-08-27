# 递归

'''
假如这里有 n 个台阶，每次你可以跨 1 个台阶或者 2 个台阶，
请问走这 n 个台阶有多少种走法？
如果有 7 个台阶，你可以 2，2，2，1 这样子上去，也可以 1，2，1，1，2 这样子上去，
总之走法有很多，那如何用编程求得总共有多少种走法呢？
'''

def f1(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f1(n-1) + f1(n-2)

hasSolvedList = {}
def f2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in hasSolvedList:
        return hasSolvedList.get(n)
    ret = f2(n-1) + f2(n-2)
    hasSolvedList[n] = ret
    return ret

# 改非递归
def f3(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    ret = 0
    pre = 2
    prepre = 1
    for i in range(3, n+1):
        ret = pre + prepre
        prepre = pre
        pre = ret
    return ret

if __name__ == "__main__":
    print(f1(30))
    print(f1(1))
    print(f1(2))
    print('-----')
    print(f2(30))
    print(f2(1))
    print(f2(2))
    print('-----')
    print(f3(30))
    print(f3(1))
    print(f3(2))