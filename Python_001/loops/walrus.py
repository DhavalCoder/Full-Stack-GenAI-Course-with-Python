# value = 13
# remainder = value % 5 

# if remainder:
    # print(f"Not divisible, Remainder is {remainder}")


value = 13

if (remainder := value % 5):
    print(f"Not divisible, Remainder is {remainder}")



available_sizes  = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup sizes: ")) in available_sizes:
    print(f"Serving {requested_size} Chai")
else:
    print(f"Size is Unavailable - {requested_size}")    