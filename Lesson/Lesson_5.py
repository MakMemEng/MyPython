# attribute はinstance化と同時に代入することができる
class Student:
    
    def __init__(self,name):
        self.name = name 
        # 第2引数のnameを初期化メソッド内のnameが受け、self.nameに代入

    def ave(self,math,english):
        print((math + english)/2)

a001 = Student("sato")
print(a001.name)

a002 = Student("tanaka")
print(a002.name)

