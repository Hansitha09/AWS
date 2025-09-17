import unittest
from unittest.mock import patch
from io import StringIO
import P2_L4  # use the real module name / file (hypotenuse script)


def fake_input(prompt=""):
    print(prompt, end="", flush=True)
    return fake_input.side_effects.pop(0)

class TestHypotenuseIO(unittest.TestCase):
    def test_1(self):
        fake_input.side_effects = ["1", "1"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L4.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Mixed Number Version 1-\n"
                        "Enter the numerator: Enter the denominator: \n"
                        "1/1 as a mixed number is 1 0/1\n")

    def test_2(self):
        fake_input.side_effects = ["3", "4"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L4.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Mixed Number Version 1-\n"
                                "Enter the numerator: Enter the denominator: \n"
                                "3/4 as a mixed number is 0 3/4\n")

    def test_3(self):
        fake_input.side_effects = ["155", "60"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L4.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Mixed Number Version 1-\n"
                                "Enter the numerator: Enter the denominator: \n"
                                "155/60 as a mixed number is 2 35/60\n")

    def test_4(self):
        fake_input.side_effects = ["4", "3"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L4.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Mixed Number Version 1-\n"
                                "Enter the numerator: Enter the denominator: \n"
                                "4/3 as a mixed number is 1 1/3\n")


if __name__ == '__main__':
    unittest.main()
