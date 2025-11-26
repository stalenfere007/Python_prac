student_marks = {"Alice": 85.5,
                 "Bob": 69.0,"Charlie": 77.0,"David": 66.0,"Emma": 66.0 ,
                 "Frank": 66.0,"Alex": 90.2}

names = input("Enter your student name: ")

if names in student_marks:
     print(f"{names} marks: {student_marks[names]}")


else:
    print("Sorry, your name is not in the Records")
    print("Please check with admin!!")
