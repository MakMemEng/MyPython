# クラスから使える関数
class TaxCalc:
    @classmethod
    def class_method(cls, price):
        assert cls.__name__ == TaxCalc.__name__
        return int(price * 0.08)

    @staticmethod
    def static_method(price):
	        return int(price * 0.08)


print(TaxCalc.class_method(1000))
print(TaxCalc.static_method(1000))