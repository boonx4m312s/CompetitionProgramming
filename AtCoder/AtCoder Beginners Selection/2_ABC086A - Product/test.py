import unittest
from unittest.mock import patch
import atcoder

# https://qiita.com/utgwkk/items/2a5d0d75a36949e1dddc

class TestStringMethods(unittest.TestCase):
    @patch('builtins.input',  lambda:'2 2')
    @patch('builtins.print')
    def test_Even(self,mock_print):
        atcoder.main()
        mock_print.assert_called_once_with('Even')

    @patch('builtins.input',  lambda:'1 3')
    @patch('builtins.print')
    def test_Odd(self,mock_print):
        atcoder.main()
        mock_print.assert_called_once_with('Odd')


if __name__ == '__main__':
    unittest.main()