chai = [1,2,3]

def edit_chai(cup):
    cup[1] = 42


edit_chai(chai)
print(chai)    

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keywords

def special_chai(*ingridients, **extras):
    print("Ingridients", ingridients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="Yes")


  