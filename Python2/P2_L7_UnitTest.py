import unittest
from unittest.mock import patch
from io import StringIO
import P2_L7  # use the real module name / file (hypotenuse script)


def fake_input(prompt=""):
    print(prompt, end="", flush=True)
    return fake_input.side_effects.pop(0)

class TestHypotenuseIO(unittest.TestCase):
    def test_1(self):
        fake_input.side_effects = ["3.8", "9"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L7.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Square Right Pyramid Calculator-\n"
                            "Enter the height: "
                            "Enter the base: \n"
                            "The pyramid has a surface area of 187.017 and a volume of 102.600\n")

    def test_2(self):
        fake_input.side_effects = ["0", "0"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L7.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Square Right Pyramid Calculator-\n"
                            "Enter the height: "
                            "Enter the base: \n"
                            "The pyramid has a surface area of 0.000 and a volume of 0.000\n")

    def test_3(self):
        fake_input.side_effects = ["1", "4"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L7.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Square Right Pyramid Calculator-\n"
                            "Enter the height: "
                            "Enter the base: \n"
                            "The pyramid has a surface area of 33.889 and a volume of 5.333\n")

    def test_4(self):
        fake_input.side_effects = ["17.6532", "9.99999"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L7.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Square Right Pyramid Calculator-\n"
                            "Enter the height: "
                            "Enter the base: \n"
                            "The pyramid has a surface area of 466.952 and a volume of 588.439\n")


if __name__ == '__main__':
    unittest.main()
