# クリーンルームの人数計測
class RoomCounter:
    pass
    def __init__(self):
        self._num_air = 0
        self._num_room = 0

    def room_in(self, num):
        """エアシャワーにnum人入る"""
        self._num_air = num
        self._num_room += num

    def room_out(self):
        """工場から1人出る"""
        self._num_room -= 1

    def num_air(self):
        """エアシャワーの人数"""
        return self._num_air

    def num_room(self):
        """工場内の人数"""
        return self._num_room


rc = RoomCounter()
rc.room_in(3)
rc.room_out()
print(rc.num_air())
print(rc.num_room())
