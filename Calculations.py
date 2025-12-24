class FinancialCalculator:

    def credit_payment(self, sum_, rate, years):
        r = rate / 100 / 12
        n = years * 12
        return sum_ * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    def deposit(self, sum_, rate, years):
        r = rate / 100
        return sum_ * (1 + r) ** years

    def bond(self, sum_, rate, years):
        r = rate / 100
        return sum_ * (1 + r * years)
