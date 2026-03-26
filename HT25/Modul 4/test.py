def change(x):
    print(f"värdet i funktionen: {x}")
    x[0] = 77
    print(f"värdet i funktionen: {x}")


a = [1,2,3]
change(a)
print(a)