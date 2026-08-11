#Pure vs impure
def pure_chai(cups):
    return cups * 10

total_chai = 0

#NOT RECOMMENDED FOR USE
def impure_chai(cups):
    global total_chai
    total_chai += cups



#Recursive 
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups Poured"
    return pour_chai(n-1)

print(pour_chai(3))


#LAMBDAS (ANONYMOUS FUNCTION)

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)