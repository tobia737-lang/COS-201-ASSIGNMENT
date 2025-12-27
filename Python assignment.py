# Personal Income Tax Calculator (2009)

status = int(input(
    "Enter filing status:\n"
    "0 = Single\n"
    "1 = Married Filing Jointly / Qualifying Widow(er)\n"
    "2 = Married Filing Separately\n"
    "3 = Head of Household\n"
))

income = float(input("Enter taxable income: "))

# Tax brackets for each filing status
brackets = {
    0: [  # Single
        (8350, 0.10),
        (33950, 0.15),
        (82250, 0.25),
        (171550, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ],
    1: [  # Married Filing Jointly
        (16700, 0.10),
        (67900, 0.15),
        (137050, 0.25),
        (208850, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ],
    2: [  # Married Filing Separately
        (8350, 0.10),
        (33950, 0.15),
        (68525, 0.25),
        (104425, 0.28),
        (186475, 0.33),
        (float("inf"), 0.35)
    ],
    3: [  # Head of Household
        (11950, 0.10),
        (45500, 0.15),
        (117450, 0.25),
        (190200, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ]
}

tax = 0
previous_limit = 0

for limit, rate in brackets[status]:
    if income > limit:
        tax += (limit - previous_limit) * rate
        previous_limit = limit
    else:
        tax += (income - previous_limit) * rate
        break

print(f"Total tax is ${tax:.2f}")
