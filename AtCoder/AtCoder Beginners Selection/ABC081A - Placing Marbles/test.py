import unittest
from unittest.mock import patch
import atcoder

#https://www.dropbox.com/sh/arnpe0ef5wds8cv/AAAk_SECQ2Nc6SVGii3rHX6Fa?dl=0

class TestStringMethods(unittest.TestCase):
    @patch('builtins.input',  lambda:'101')
    @patch('builtins.print')
    def test_Even(self,mock_print):
        atcoder.main()
        mock_print.assert_called_once_with(2)

    @patch('builtins.input',  lambda:'000')
    @patch('builtins.print')
    def test_Odd(self,mock_print):
        atcoder.main()
        mock_print.assert_called_once_with(0)


if __name__ == '__main__':
    unittest.main()