# コンストラクタはインスタンス化するときに自動的に実行されるメソッド
# コンストラクタは初期メソッドという

class Student:

    # コンストラクタ
    def __init__(self):

        # attribute
        self.name = "" 
        # selfにインスタンスが代入される

# 引数のselfにa001が代入
# self.nameがa001.name
    # method
    def ave(self,math,english):
        print((math + english)/2)

a001 = Student()
# def attribute
a001.name = "sato"
print(a001.name)

# instance毎にattributeを再定義する必要がある
a002 = Student()
a002.name = "tanaka"
print(a002.name)

