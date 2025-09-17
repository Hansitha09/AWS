import unittest
from unittest.mock import patch
from io import StringIO
import P2_L6  # use the real module name / file (hypotenuse script)


def fake_input(prompt=""):
    print(prompt, end="", flush=True)
    return fake_input.side_effects.pop(0)

class TestHypotenuseIO(unittest.TestCase):
    def test_1(self):
        fake_input.side_effects = ["12", "16"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L6.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Hypotenuse Calculator-\n"
                         "Enter the length of the first leg of your triangle:"
                         "\nEnter the length of the second leg of your triangle:"
                         "\n\nThe hypotenuse of your triangle is 20.000\n")

    def test_2(self):
        fake_input.side_effects = ["0", "0"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L6.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Hypotenuse Calculator-\n"
                         "Enter the length of the first leg of your triangle:"
                         "\nEnter the length of the second leg of your triangle:"
                         "\n\nThe hypotenuse of your triangle is 0.000\n")

    def test_3(self):
        fake_input.side_effects = ["3.8", "5.77"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L6.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Hypotenuse Calculator-\n"
                         "Enter the length of the first leg of your triangle:"
                         "\nEnter the length of the second leg of your triangle:"
                         "\n\nThe hypotenuse of your triangle is 6.909\n")

if __name__ == '__main__':
    unittest.main()