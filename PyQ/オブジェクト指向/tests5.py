import unittest


class Test1(unittest.TestCase):
    def test_it(self):
        from testfixtures import OutputCapture
        with OutputCapture() as output:
            import oop_basic_5_1  # noqa
        self.assertEqual(output.captured, """\
3
2
""", '結果が異なっています')


class Test2(unittest.TestCase):
    def test_it(self):
        try:
            from oop_basic_5_2 import do_test
            from testfixtures import OutputCapture
            with OutputCapture() as output:
                do_test()
            self.assertEqual(output.captured, """\
20
2
15.0
""", '結果が異なっています')
        except ImportError as e:
            self.fail(f'do_testを作成してください。\n{e}')


class Test3(unittest.TestCase):
    def test_it(self):
        try:
            from oop_basic_5_3 import do_test
            from testfixtures import OutputCapture
            with OutputCapture() as output:
                do_test()
            self.assertEqual(output.captured, """\
1.0
2.0
""", '結果が異なっています')
        except ImportError as e:
            self.fail(f'do_testを作成してください。\n{e}')


class Test4(unittest.TestCase):
    def test_it(self):
        try:
            from oop_basic_5_4 import simulate
            from testfixtures import OutputCapture
            with OutputCapture() as output:
                simulate()
            self.assertEqual(output.captured, """\
エアシャワーの利用人数の回数平均 2.0
工場内の人数の時間平均 3.0
""", '結果が異なっています')
        except ImportError as e:
            self.fail(f'simulateを作成してください。\n{e}')
