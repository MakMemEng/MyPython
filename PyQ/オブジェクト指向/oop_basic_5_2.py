# クリーンルームの統計量
class StatCount:
    pass
    def __init__(self):
        self._value = 0  # 現在値
        self._count = 0  # 代入回数
        self._sum = 0  # 合計

    def assign(self, value):
        self._value = value
        self._count += 1
        self._sum += value

    def value(self):
        """現在値"""
        return self._value

    def count(self):
        """代入回数"""
        return self._count

    def mean(self):
        """代入あたりの平均"""
        return self._sum / max(1, self._count)  # ゼロ割を避けるため

def do_test():
    i = StatCount()
    i.assign(10)
    i.assign(20)
    print(i.value())  # 20
    print(i.count())  # 2
    print(i.mean())  # 15.0


if __name__ == '__main__':
    do_test()
