def sold_cups():
    return 120

total = sold_cups()
print(total)


def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, Chai is Over"
    return "Chai is ready!"

print(chai_status(0))
print(chai_status(5))