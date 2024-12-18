def simple_interest(p,t,r):
    print(f"The principal is", p)
    print(f"The time period is", t)
    print(f"The rate of interest is",r)
    
    si = (p * t * r)/100
    
    print(f"The Simple Interest is", si)
    return si


simple_interest(8000,12,6)
