import unittest
from unittest.mock import patch
from io import StringIO
import P2_L1  # use the real module name / file (hypotenuse script)

def fake_input(prompt=""):
    print(prompt, end="", flush=True)
    return fake_input.side_effects.pop(0)

class TestHypotenuseIO(unittest.TestCase):
    def test_1(self):
        fake_input.side_effects = ["John","Smith","34","S123456","Engineering"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L1.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-ID Badge-\n"
                            "Enter your first name:\n" 
                            "Enter your last name:\n"
                            "Enter your age:\n"
                            "Enter your employee ID number:\n"
                            "Enter your department:\n\n"
                            "Employee:     Smith, John (34)\n"
                            "Department:        Engineering\n"
                            "ID Number:             S123456\n")

    def test_2(self):
        fake_input.side_effects = ["Tina","Carmo","42","C74354","Administration"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L1.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-ID Badge-\n"
                            "Enter your first name:\n" 
                            "Enter your last name:\n"
                            "Enter your age:\n"
                            "Enter your employee ID number:\n"
                            "Enter your department:\n\n"
                            "Employee:     Carmo, Tina (42)\n"
                            "Department:     Administration\n"
                            "ID Number:              C74354\n")
if __name__ == '__main__':
    unittest.main()