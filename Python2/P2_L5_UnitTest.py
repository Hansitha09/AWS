import unittest
from unittest.mock import patch
from io import StringIO
import P2_L5  # use the real module name / file (hypotenuse script)


def fake_input(prompt=""):
    print(prompt, end="", flush=True)
    return fake_input.side_effects.pop(0)

class TestHypotenuseIO(unittest.TestCase):
    def test_1(self):
        fake_input.side_effects = ["1", "1", "1", "1", "1", "2"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L5.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Profit Calculator-\n"
                                "Order quantity: Cost per item: Case size: Shipping Cost per case: Tariff percentage: Sale price: \n"
                                "The acquisition cost of these items is $2.01 with an estimated profit of $-0.01 once sold.\n")

    def test_2(self):
        fake_input.side_effects = ["8", "1", "5", "2", "20", "5"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L5.main()

        output = m_out.getvalue()
        self.assertEqual(output,"-Profit Calculator-\n"
                                "Order quantity: Cost per item: Case size: Shipping Cost per case: Tariff percentage: Sale price: \n"
                                "The acquisition cost of these items is $13.60 with an estimated profit of $26.40 once sold.\n")


    def test_3(self):
        fake_input.side_effects = ["125", ".87", "25", "1.80", "13", "3.87"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L5.main()

        output = m_out.getvalue()
        self.assertEqual(output, "-Profit Calculator-\n"
                                 "Order quantity: Cost per item: Case size: Shipping Cost per case: Tariff percentage: Sale price: \n"
                                 "The acquisition cost of these items is $131.89 with an estimated profit of $351.86 once sold.\n")

    def test_4(self):
        fake_input.side_effects = ["5000", "4.75", "24", "15.97", "25", "5.87"]
        with patch('builtins.input', new=fake_input), \
                patch('sys.stdout', new_callable=StringIO) as m_out, \
                patch('sys.stderr', new_callable=StringIO) as m_err:
            P2_L5.main()

        output = m_out.getvalue()
        self.assertEqual(output, "-Profit Calculator-\n"
                                 "Order quantity: Cost per item: Case size: Shipping Cost per case: Tariff percentage: Sale price: \n"
                                 "The acquisition cost of these items is $33025.23 with an estimated profit of $-3675.23 once sold.\n")
if __name__ == '__main__':
    unittest.main()
