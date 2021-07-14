def conversion(euros):
    """A simple function that converts an input of euros to an output of dollars."""
    euros = float(input("Enter amount of euros: \n"))
    dollars = round(1.18730 * euros,2)
    #print(f"{euros} euros converted to US dollars is ${dollars}.".format(euros, dollars))
    return dollars
    
def cookies_price(dollars):
    """A simple function designed to convert the input of dollars to amount of $0.50 cookies that can be purchased, including the remainder of money left after buying maximum amount of cookies."""
    #dollars = conversion(euros)
    cookies = dollars // 0.50
    remainder = dollars - (cookies * 0.50)
    print(f"You can buy {cookies} cookies with ${dollars}.\nYou will have ${remainder:.2f} left if you buy the maximum amount of cookies.")
    return cookies

def create_change(dollars, cookies):
    """A simple function that converts dollars to quarters, dimes, nickels, and pennies. \nWith 2 arguments, returns 1 value."""
    #cookies = cookies_price(euros)
    #dollars = conversion(euros)
    remainder = dollars - (cookies * 0.50)
    q = remainder // 0.25
    d = (remainder - q*0.25) //0.10
    n = (remainder - q* 0.25 - d*0.10) //0.05
    p = remainder // 0.5
    print(f"Your remaining money will be given in {q} quarters, {d} dimes, {n} nickels, and {p} pennies.")
    return remainder

def cookie_convert(euros):
    """Final function is meant to string all previous functions together."""
    dollars = conversion(euros)
    print(f"{euros} euros converted to US dollars is ${dollars}.".format(euros, dollars))
    cookies = cookies_price(dollars)
    print(f"You can buy {cookies} cookies with {euros} euros.") 
    remainder = create_change(dollars, cookies)
    #print(f"Your remaining money will be given in {q} quarters, {d} dimes, {n} nickels, and {p} pennies.")
