# クリーンルームの時間統計量
from oop_basic_5_2 import StatCount


class StatTime(StatCount):
    pass
    Time = 0 #時刻
    
    def __init__(self):
        super().__init__() # StatCountの初期化処理
        self._initime = StatTime.Time # 作成時の時刻
        self._pretime = 0  # 前回代入時の時刻
        
    def assign(self, value):
        t = StatTime.Time - self._pretime # 前回からの時間
        self._pretime = StatTime.Time # 時刻を更新
        s = self._sum + self._value * t # 合計面積
        super().assign(value) # StatCountの代入処理
        self._sum = s # _sumは再設定
        
    def mean(self):
        """時間で見た平均"""
        t = StatTime.Time - self._pretime # 前回からの時間
        s = self._sum + self._value * t # 合計面積
        return s / (StatTime.Time - self._initime)


def do_test():
    StatTime.Time = 9
    t = StatTime()
    t.assign(1)
    StatTime.Time = 11
    t.assign(4)
    print(t.mean())  # 1.0
    StatTime.Time = 12
    print(t.mean())  # 2.0


if __name__ == '__main__':
    do_test()
