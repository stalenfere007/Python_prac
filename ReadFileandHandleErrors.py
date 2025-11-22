name = input("Enter the file name: ")

# with open('name','w') as file:
#     file.write("This is a sample text file.")
#     file.write("\nThis file contains multiple lines.")
try:
    with open(name,'r') as file:
        content1 = file.readline()
        content2 = file.readline()
    print(f"Line 1: {content1}")
    print(f"Line 2: {content2}")

except FileNotFoundError:
    print(f"The file {name} not found.Pls check file name!!")