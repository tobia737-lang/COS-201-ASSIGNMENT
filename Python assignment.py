class TaxCalculator:
    def __init__(self, status, income):
        self.status = status
        self.income = income

    def compute_tax(self):
        tax = 0

       if self.status == 0:
            if self.income <= 10000:
                tax = self.income * 0.10
            elif self.income <= 30000:
                tax = 10000 * 0.10 + (self.income - 10000) * 0.15
            else:
                tax = 10000 * 0.10 + 20000 * 0.15 + (self.income - 30000) * 0.25

        elif self.status == 1:
            if self.income <= 20000:
                tax = self.income * 0.10
            elif self.income <= 50000:
                tax = 20000 * 0.10 + (self.income - 20000) * 0.15
            else:
                tax = 20000 * 0.10 + 30000 * 0.15 + (self.income - 50000) * 0.25

         elif self.status == 2:
            if self.income <= 12000:
                tax = self.income * 0.10
            elif self.income <= 35000:
                tax = 12000 * 0.10 + (self.income - 12000) * 0.15
            else:
                tax = 12000 * 0.10 + 23000 * 0.15 + (self.income - 35000) * 0.25

        elif self.status == 3:
            if self.income <= 15000:
                tax = self.income * 0.10
            elif self.income <= 40000:
                tax = 15000 * 0.10 + (self.income - 15000) * 0.15
            else:
                tax = 15000 * 0.10 + 25000 * 0.15 + (self.income - 40000) * 0.25

        else:
            print("Invalid filing status")
            return 0

        return tax
        
status = int(input(
    "Enter filing status:\n"
    "0 = Single\n"
    "1 = Married Filing Jointly\n"
    "2 = Married Filing Separately\n"
    "3 = Head of Household\n"
))

income = float(input("Enter taxable income: "))

calculator = TaxCalculator(status, income)
tax = calculator.compute_tax()

print(f"Total tax is ${tax:.2f}")



