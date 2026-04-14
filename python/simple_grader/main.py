import csv

def grade():
    # iterate over student names and grades
    while True:
        name = input("Enter student name: ")
        mark1 = float(input("Enter first mark: "))
        mark2 = float(input("Enter second mark: "))
        mark3 = float(input("Enter third mark: "))

        avg = (mark1 + mark2 + mark3)/3
        print("\nAverage: ", avg)

        # Initialize an list for makrs
        marks = [mark1, mark2, mark3]

        # Iniitalize empty dictionary for grades
        grades = {}
        grades['name'] = name
        grades['marks'] = marks
        grades['avg'] = avg
        grades['grade'] = grade

        for value in grades.values():
            if avg >= 70:
                grades['grade'] = 'A'
            elif avg >= 60 and avg < 70:
                grades['grade'] = 'B'
            elif avg >= 50 and avg < 60:
                grades['grade'] = 'C'
            elif avg >= 40 and avg < 50:
                grades['grade'] = 'D'
            elif avg >= 30 and avg < 40:
                grades['grade'] = 'E'
            else:
                grades['grade'] = 'Fail' 

        print(grades)
        print('-' * 20)

        with open("grades.csv", "a", newline="") as file:
            write = csv.writer(file)
            for key, value in grades.items():
                write.writerow([key,value])
        print("File 'grades.csv' written successfully")

        choice = input("Do you wish to continue? (y/n): ")
        if choice == 'no' or choice == 'n':
            print("Exiting grader...")
            break

if __name__ == "__main__":
    grade()
