class Basechai:
    def __init__(self, type_):
        self.type = type_



    def prepare(self):   
        print(f"Preparing {self.type} chai....")

class Masalachai(Basechai):
    def add_spices(self):
        print("Adding cardmom, ginger, cloves.")

class ChaiShop:
    chai_cls = Basechai


    def __init__(self):
        self.chai = self.chai_cls("Regular")


    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop ")

        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls = Masalachai                            


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()    