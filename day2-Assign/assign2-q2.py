def compound_interest(p, r, t):
 
    Amount = p * (pow((1 + r / 100), t))
    CI = Amount - p
    print(f"Compound interest is", CI)

compound_interest(10000,5,12)
