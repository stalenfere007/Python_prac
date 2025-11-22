cont1 = input('Enter text to write to the file: ')


# Write
with open('output.txt', 'w') as file:
    file.write(cont1 + "\n")
print("Data successfully written to the file")



cont2 = input('Enter additional text to append to the file: ')
# Append
with open('output.txt', 'a') as file:
    file.write(cont2 + "\n")
print("Data successfully appended to the file")

# Read and display
print("Final contents of the file:")
with open('output.txt', 'r') as file:
    print(file.read())
