import unittest
import requests
import json


class TestLoanCalculator(unittest.TestCase):

    url = "/calculate"

    def test_monthly_rate_with_amount_85000(self):

        data = json.dumps({
            "maturity": 120,
            "productType": "LOANSE02",
            "amount": 85000,
            "interestRate": 10.95,
            "monthlyPaymentDay": 27,
            "administrationFee": 40,
            "conclusionFee": 695,
            "currency": "SEK"
        })

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request(method="POST", url=TestLoanCalculator.url, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['monthlyPayment'], 1211.58)
        self.assertEqual(response.json()['totalRepayableAmount'], 145016)


    



if __name__=="__main__":
    unittest.main()






