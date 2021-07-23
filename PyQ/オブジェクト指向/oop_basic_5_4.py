# クリーンルームの統計量
from oop_basic_5_2 import StatCount
from oop_basic_5_3 import StatTime


class RoomCounter:
    def __init__(self):
        self._num_air = StatCount()
        self._num_room = StatTime()

    def room_in(self, num):
        """エアシャワーにnum人入る"""
        self._num_air.assign(num)
        self._num_room.assign(self._num_room.value() + num)

    def room_out(self):
        """工場から1人出る"""
        self._num_room.assign(self._num_room.value() - 1)
        
    def show_mean(self):
        """エアシャワーと工場内の平均表示"""
        print('エアシャワーの利用人数の回数平均', self._num_air.mean())
        print('工場内の人数の時間平均', self._num_room.mean())


def simulate():
    StatTime.Time = 9
    rc = RoomCounter()
    rc.room_in(4)  # 9時に4人入る
    StatTime.Time = 12
    for _ in range(4):
        rc.room_out()  # 12時に4人出る
    rc.room_in(1)  # 12時に1人入る
    StatTime.Time = 13
    rc.room_in(1)  # 13時に1人入る
    StatTime.Time = 14
    rc.show_mean()  # 14時の統計量


simulate()
