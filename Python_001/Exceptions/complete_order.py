class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40 }
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cup must be an integer")
        toatal = menu[flavor] * cups
        print(f"Your bill for cups {cups} of {flavor} chai: rupees {toatal}")
    except Exception as e:
        print("error:" , e)
    finally:
        print("Thank You for visting Dhaval's Cafe")    


bill("mint", 2)
bill("masala", "three")
bill("ginger", 3500)
bill("masala", 45)