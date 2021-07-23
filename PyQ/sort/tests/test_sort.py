from importlib import import_module
import unittest

from testfixtures import OutputCapture


class SortTestCase(unittest.TestCase):

    def test_seat(self):
        answer = ['1A 山田', '1B 神木', '1C 中村',
                  '2A 佐藤', '2B 田中', '2C 山崎',
                  '3A 高橋', '3B 渋谷', '3C 北村']

        with OutputCapture() as output:
            import_module('seat')
            result = output.captured
            result = result.strip()
            result_list = result.split('\n')

        self.assertEqual(answer, result_list)

    def test_employee_sorted(self):
        answer = ['0023_中村', '0044_吉田', '0056_田中', '0092_林',
                  '0345_高橋', '0566_井上', '0633_斎藤', '0719_小林', '0721_木村',
                  '0783_山田', '0901_清水', '0988_加藤', '1001_山田',
                  '1011_佐藤', '1021_山口', '1031_松本', '1033_山本',
                  '1055_鈴木', '1145_伊藤', '1224_佐々木', '1910_渡辺']

        with OutputCapture() as output:
            import_module('employee_sorted')
            result = output.captured
            result = result.strip()
            result_list = result.split('\n')

        self.assertEqual(answer, result_list)