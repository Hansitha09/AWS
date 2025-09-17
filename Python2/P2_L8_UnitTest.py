import unittest
from unittest.mock import patch
from io import StringIO
import P2_L8  # use the real module name / file (hypotenuse script)


def fake_input(prompt=""):
    print(prompt, end="", flush=True)
    return fake_input.side_effects.pop(0)

class TestHypotenuseIO(unittest.TestCase):
    def test_1(self):
        fake_input.side_effects = ["100_000","10_000","30",".0625"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L8.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Mortgage Calculator-\n"
                                "Enter house cost:\n"
                                "Enter down payment:\n"
                                "Enter number of years on the loan:\n"
                                "Enter annual interest rate (Value should be less that 1):\n"
                                "\nBuying a house with a cost of $100,000.00 over 30 years at an interest rate of $6.25% "
                                "with a down payment of $10,000.00 would have a total cost of $199,492.37 with a monthly payment of $554.15.\n")

    def test_2(self):
        fake_input.side_effects = ["100_000", "10_000", "30", ".03"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L8.main()

        output = m_out.getvalue()
        self.assertEqual(output, "-Mortgage Calculator-\n"
                                 "Enter house cost:\n"
                                 "Enter down payment:\n"
                                 "Enter number of years on the loan:\n"
                                 "Enter annual interest rate (Value should be less that 1):\n"
                                 "\nBuying a house with a cost of $100,000.00 over 30 years at an interest rate of $3.00% "
                                 "with a down payment of $10,000.00 would have a total cost of $136,599.71 with a monthly payment of $379.44.\n")

    def test_3(self):
        fake_input.side_effects = ["5_345", "500", "1", ".10"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L8.main()

        output = m_out.getvalue()
        self.assertEqual(output, "-Mortgage Calculator-\n"
                                 "Enter house cost:\n"
                                 "Enter down payment:\n"
                                 "Enter number of years on the loan:\n"
                                 "Enter annual interest rate (Value should be less that 1):\n"
                                 "\nBuying a house with a cost of $5,345.00 over 1 years at an interest rate of $10.00% "
                                 "with a down payment of $500.00 would have a total cost of $5,111.43 with a monthly payment of $425.95.\n")

    def test_4(self):
        fake_input.side_effects = ["356_000", "100_000", "40", ".0455"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L8.main()

        output = m_out.getvalue()
        self.assertEqual(output, "-Mortgage Calculator-\n"
                                 "Enter house cost:\n"
                                 "Enter down payment:\n"
                                 "Enter number of years on the loan:\n"
                                 "Enter annual interest rate (Value should be less that 1):\n"
                                 "\nBuying a house with a cost of $356,000.00 over 40 years at an interest rate of $4.55% "
                                 "with a down payment of $100,000.00 would have a total cost of $556,378.43 with a monthly payment of $1,159.12.\n")

    def test_4(self):
        fake_input.side_effects = ["426_000", "250_000", "20", ".0513"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L8.main()

        output = m_out.getvalue()
        self.assertEqual(output, "-Mortgage Calculator-\n"
                                 "Enter house cost:\n"
                                 "Enter down payment:\n"
                                 "Enter number of years on the loan:\n"
                                 "Enter annual interest rate (Value should be less that 1):\n"
                                 "\nBuying a house with a cost of $426,000.00 over 20 years at an interest rate of $5.13% "
                                 "with a down payment of $250,000.00 would have a total cost of $281,807.67 with a monthly payment of $1,174.20.\n")

if __name__ == '__main__':
    unittest.main()
