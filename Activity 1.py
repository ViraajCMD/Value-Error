try:

    number = int(input("Please enter a number: "))
    print(f"The number entered is {number}!")

except ValueError as ex:
    print("Exeption:", ex)