#Duplication Method
class chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

class GingerChai(chai):
    def __init__(self, type_, strength, spice_level):
                self.type = type_
                self.strength = strength
                self.spice_level = spice_level

#Explicit Call

class GingerChai(chai):
      def __init__(self, type_, strength, spice_level):
            chai.__init__(self, type_, strength)
            self.spice_level = spice_level


#Super()

class GingerChai(chai):
      def __init_(self, type_, strength, spice_level):
            super().__init__(type_, strength)                            
            self.spice_level = spice_level