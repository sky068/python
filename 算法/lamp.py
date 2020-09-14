'''
有一百盏灯连成环，每盏灯都有开关两个状态，起始状态随机，
每改变其中一盏灯的状态则相邻两盏灯的状态也会改变，请设计一个算法点亮所有的灯
思路：
n只要满足(n - 1) % 3 == 0均可以用下面灯思路解答
先遍历一遍，按下所有状态为关闭的灯的右侧那个灯，则结果只会为全部点亮，有一盏为关闭，有两盏为关闭
如果为两盏关闭，则按下右侧那个关闭的灯，此时变成只有一盏关闭，然后从开启的灯每三个按中间的，转为全部关闭
最后循环按一遍，每盏灯的状态变化了三次则全部点亮
'''

from random import random

class Lamp(object):
    def __init__(self, num: int):
        self.lamps = []
        for i in range(num):
            self.lamps.append(True if random() < 0.5 else False)

    def __repr__(self):
        return ' '.join(str(item) for item in self.lamps)

    # 循环按一遍状态为关闭的灯的右边的灯
    def _turnLightSome(self):
        for i in range(len(self.lamps)):
            if not self.lamps[i]:
                self.lamps[i] = not self.lamps[i]
                next = (i + 1) % len(self.lamps)
                self.lamps[next] = not self.lamps[next]
                nextnext = (next + 1) % len(self.lamps)
                self.lamps[nextnext] = not self.lamps[nextnext]

    # 所有灯都是熄灭状态，循环按一遍全部打开
    def _turnOnAll(self):
        for i in range(len(self.lamps)):
            pre = (i - 1) if (i - 1) >= 0 else (len(self.lamps) - 1)
            next = (i + 1) % len(self.lamps)
            self.lamps[pre] = not self.lamps[pre]
            self.lamps[i] = not self.lamps[i]
            self.lamps[next] = not self.lamps[next]

    # 关闭所有的灯
    def _turnOffAll(self, offIndex):
        cur = offIndex + 1
        next = cur + 1
        nextnext = next + 1
        end = offIndex - 1 if offIndex - 1 >= 0 else len(self.lamps) - 1

        while cur != end and next != end and nextnext != end:
            next = (cur + 1) % len(self.lamps)
            nextnext = (next + 1) % len(self.lamps)
            self.lamps[cur] = not self.lamps[cur]
            self.lamps[next] = not self.lamps[next]
            self.lamps[nextnext] = not self.lamps[nextnext]
            cur = (cur + 3) % len(self.lamps)

    def turnLight(self):
        if len(self.lamps) < 3 or (len(self.lamps) - 1) % 3 != 0:
            print('灯的数量不满足条件(n > 3 and (n-1) % 3 == 0')
            return

        self._turnLightSome()

        # 查看开头两盏的状态
        if self.lamps[0] and self.lamps[1]:
            print('---全部已经打开.')
        elif not self.lamps[0] and not self.lamps[1]:
            print('---两盏为熄灭')
            # 两盏都是熄灭状态 按下右侧self.lamps[1]，转成只有1盏熄灭(此时lamps[0]和lamps[1]都是开启状态，只有lamps[2]是关闭状态)
            self.lamps[0] = not self.lamps[0]
            self.lamps[1] = not self.lamps[1]
            self.lamps[2] = not self.lamps[2]
            # 接下来从亮灯开始每3个按中间的，变成全部熄灭
            self._turnOffAll(2)
            self._turnOnAll()
        else:
            print('---只有一盏为熄灭')
            # 从亮灯开始每3个按中间的，变成全部熄灭
            closed = 0 if not self.lamps[0] else 1
            self._turnOffAll(closed)
            self._turnOnAll()

        print('全部灯已经打开.')

if __name__ == "__main__":
    lamp = Lamp(100)
    lamp.turnLight()
    print(lamp)

