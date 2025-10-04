# Professional Grade Organizer

print("===== Welcome to the Grade Organizer =====")

# Input student details
student_name = input("Enter student's name: ")
marks_input = input("Enter marks (0-100): ")

# Check if input is numeric
if marks_input.isnumeric():
    marks = float(marks_input)
    
    # Validate marks range
    if 0 <= marks <= 100:
        # Determine grade and remarks
        if marks >= 90:
            grade = "A+"
            remark = "Excellent work! "
        elif marks >= 80:
            grade = "A"
            remark = "Very good! "
        elif marks >= 70:
            grade = "B"
            remark = "Good job! "
        elif marks >= 60:
            grade = "C"
            remark = "Fair effort! "
        elif marks >= 50:
            grade = "D"
            remark = "Needs improvement. "
        else:
            grade = "F"
            remark = "Failed. Try harder! "

        # Display organized report
        print("\n===== Grade Report =====")
        print(f"Student Name: {student_name}")
        print(f"Marks Obtained: {marks}")
        print(f"Grade: {grade}")
        print(f"Remarks: {remark}")
    else:
        print(" Invalid marks! Please enter a number between 0 and 100.")
else:
    print("Invalid input! Please enter valid marks.")

