#Written by Shiven Desai
filename = "things.txt"

# Open the file in write mode
with open(filename, "w") as file:
    # Write the name of an animal, a fruit, and a country on separate lines
    file.write("Elephant\n")
    file.write("Apple\n")
    file.write("Spain\n")

# Open the file in read mode and print its contents
with open(filename, "r") as file:
    print(file.read())
