import unittest
from unittest.mock import patch
from io import StringIO
import P2_L2  # use the real module name / file (hypotenuse script)


def fake_input(prompt=""):
    print(prompt, end="", flush=True)
    return fake_input.side_effects.pop(0)

class TestHypotenuseIO(unittest.TestCase):
    def test_1(self):
        fake_input.side_effects = ["8","3","12", "1"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L2.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Pizza Order-\n"
                                "How many adults? How many slices will an adult eat? How many children? How many slice will a child eat? \n"
                                "You need to order 3 pizzas.\n")

    def test_2(self):
        fake_input.side_effects = ["7","4","11", "2"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L2.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Pizza Order-\n"
                                "How many adults? How many slices will an adult eat? How many children? How many slice will a child eat? \n"
                                "You need to order 5 pizzas.\n")

    def test_3(self):
        fake_input.side_effects = ["19","2","3", "2"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L2.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Pizza Order-\n"
                                "How many adults? How many slices will an adult eat? How many children? How many slice will a child eat? \n"
                                "You need to order 4 pizzas.\n")

    def test_4(self):
        fake_input.side_effects = ["7","6","44", "3"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L2.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Pizza Order-\n"
                                "How many adults? How many slices will an adult eat? How many children? How many slice will a child eat? \n"
                                "You need to order 15 pizzas.\n")

    def test_5(self):
        fake_input.side_effects = ["158","2","77", "1"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L2.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Pizza Order-\n"
                                "How many adults? How many slices will an adult eat? How many children? How many slice will a child eat? \n"
                                "You need to order 33 pizzas.\n")


if __name__ == '__main__':
    unittest.main()
