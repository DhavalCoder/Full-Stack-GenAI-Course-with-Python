menu = [
   "Masala chai",
   "Iced lemon Tea",
   "Green Tea",
   "Iced Peach Tea",
   "Ginger Chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)