def calculate_marginal_tax(income, brackets, beyond_rate):
    tax = 0.0
    prev_upper = 0

    for upper, rate in brackets:
        if income > prev_upper:
            portion = min(income, upper) - prev_upper
            tax += portion * rate
        prev_upper = upper

    # Beyond case
    if income > prev_upper:
        tax += (income - prev_upper) * beyond_rate

    return tax


# Example usage
brackets = [
    (15_000, 0.00),
    (20_000, 0.10),
    (30_000, 0.20)
]
beyond_rate = 0.30

print(calculate_marginal_tax(17_000, brackets, beyond_rate))  # 200
print(calculate_marginal_tax(27_000, brackets, beyond_rate))  # 1900
