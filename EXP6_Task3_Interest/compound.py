def compound_interest(principle, rate, time):
    ci = (principle * ((1 + (rate/100)) ** time)) - principle
    return ci
