import unittest
import main


class TestHooksBalance(unittest.TestCase):

    def test_hooks_balance(self):
        self.assertEqual(main.hooks_balance('((()))'), 'Hooks is balanced')
        self.assertEqual(main.hooks_balance('{[()]}'), 'Hooks is balanced')
        self.assertEqual(main.hooks_balance('(()]}'), 'Hooks is not balanced')
        self.assertEqual(main.hooks_balance('(()]'), 'Hooks is not balanced')
        self.assertEqual(main.hooks_balance('(((('), 'Hooks is not balanced')
        self.assertEqual(main.hooks_balance(']]]]'), 'Hooks is not balanced')
        self.assertEqual(main.hooks_balance(''), 'String is empty')

    def test_hooks_balance_with_letters(self):
        self.assertEqual(main.hooks_balance('(((abc)))'), 'Hooks is balanced')
        self.assertEqual(main.hooks_balance('(a(b(c)))'), 'Hooks is balanced')
        self.assertEqual(main.hooks_balance('{[(abc)]}'), 'Hooks is balanced')
        self.assertEqual(main.hooks_balance('{[(a)b]c}'), 'Hooks is balanced')
        self.assertEqual(main.hooks_balance('((((abc'), 'Hooks is not balanced')
        self.assertEqual(main.hooks_balance(']]]]abc'), 'Hooks is not balanced')
        self.assertEqual(main.hooks_balance('abc'), 'Hooks is balanced')


if __name__ == '__main__':
    unittest.main()
