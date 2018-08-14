def python_food(*args, file=None):
    for arg in args:
        print(arg, file=alluFile)


with open("allu", mode='w') as alluFile:
    python_food(70, 34, 32, 2, file=alluFile)