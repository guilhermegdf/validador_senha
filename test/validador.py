from main.function import validacao
import unittest


class ValidadorTest(unittest.TestCase):
    def test(self):
        self.assertEqual(validacao(''), False)
        self.assertEqual(validacao('aa'), False)
        self.assertEqual(validacao('ab'), False)
        self.assertEqual(validacao('AAAbbbCc'), False)
        self.assertEqual(validacao('AbTp9!foo'), False)
        self.assertEqual(validacao('AbTp9!foA'), False)
        self.assertEqual(validacao('AbTp9 fok'), False)
        self.assertEqual(validacao('AbTp9!fok'), True)


if __name__ == '__main__':
    unittest.main()
