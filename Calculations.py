class FinancialCalculator:

    def annuity_payment(self, sum_, rate, years):
        r = rate / 100 / 12
        n = years * 12
        return sum_ * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    def compound_interest(self, sum_, rate, years):
        r = rate / 100
        return sum_ * (1 + r) ** years

    def simple_interest(self, sum_, rate, years):
        r = rate / 100
        return sum_ * (1 + r * years)
