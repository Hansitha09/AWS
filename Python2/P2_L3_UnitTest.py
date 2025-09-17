import unittest
from unittest.mock import patch
from io import StringIO
import P2_L3  # use \nThe real module name / file (hypotenuse script)


def fake_input(prompt=""):
    print(prompt, end="", flush=True)
    return fake_input.side_effects.pop(0)

class TestHypotenuseIO(unittest.TestCase):
    def test_1(self):
        fake_input.side_effects = ["0"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L3.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Time-\n"
                                "Enter total minutes: \nThe time is 0 hours and 0 minutes.\n")

    def test_2(self):
        fake_input.side_effects = ["1"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L3.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Time-\n"
                                "Enter total minutes: \nThe time is 0 hours and 1 minutes.\n")

    def test_3(self):
        fake_input.side_effects = ["180"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L3.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Time-\n"
                                "Enter total minutes: \nThe time is 3 hours and 0 minutes.\n")

    def test_4(self):
        fake_input.side_effects = ["193"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L3.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Time-\n"
                                "Enter total minutes: \nThe time is 3 hours and 13 minutes.\n")

    def test_5(self):
        fake_input.side_effects = ["10258"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L3.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Time-\n"
                                "Enter total minutes: \nThe time is 170 hours and 58 minutes.\n")

    def test_6(self):
        fake_input.side_effects = ["74865"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L3.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Time-\n"
                                "Enter total minutes: \nThe time is 1247 hours and 45 minutes.\n")

    def test_7(self):
        fake_input.side_effects = ["549"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L3.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Time-\n"
                                "Enter total minutes: \nThe time is 9 hours and 9 minutes.\n")
if __name__ == '__main__':
    unittest.main()
