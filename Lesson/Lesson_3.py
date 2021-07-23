class Student:
    # method
    def ave(self,math,english):
        # 引数を受け取らない場合　空欄 or self
        # ave(self,引数,引数)
        print((math + english)/2)
# class can use when insert instance in variable(変数)
# インスタンス化　オブジェクト化　オブジェクト生成
a001 = Student()
a001.ave(80,70)

# def attribute
a001.name = "sato"
print(a001.name)

# instance毎にattributeを再定義する必要がある
# a002 = Student()
# print(a002.name)

