#Written by Shiven Desai
# Open the file for writing
with open("number_list.txt", "w") as file:
    # Write numbers 1 through 100 to the file
    for i in range(1, 101):
        file.write(str(i) + "\n")
