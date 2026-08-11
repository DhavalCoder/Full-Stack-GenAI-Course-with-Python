def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Cardamom Chai"


# stall = serve_chai()

# for cup in stall:
#     print(cup)


#Generator
def get_Chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_Chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) #Gives Error