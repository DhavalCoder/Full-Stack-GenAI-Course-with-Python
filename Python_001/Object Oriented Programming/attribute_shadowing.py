class chai:
    temperature = "hot"
    strength = "strong"


cutting = chai()
print(cutting.temperature)

cutting.temperature =  "Mild"
print("Sfter changong", cutting.temperature)
print("Direct look inro the class", chai.temperature)

del cutting.temperature
print(cutting.temperature)