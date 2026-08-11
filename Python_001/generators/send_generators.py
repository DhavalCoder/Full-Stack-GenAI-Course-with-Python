def chai_customer():
    print("Welcome ! What chai would u like?")
    order = yield
    while True:
       print(f"Preaparing: {order}")
       order = yield


stall = chai_customer()
next(stall)  #start the generator


stall.send("Masala Chai")

