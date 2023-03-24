#Written by Shiven Desai
# Open the file in read mode
file = open("things.txt", "r")

# Read all lines of the file and store them in a list
lines = file.readlines()

# Close the file
file.close()

# Display the contents of the file
print("Contents of things.txt:")
for line in lines:
    print(line.strip())
