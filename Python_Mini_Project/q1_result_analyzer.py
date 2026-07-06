def analyze_result(name, roll, marks):
    # Calculate total and average
    total = sum(marks)
    average = total / len(marks)
    
    # Determine the grade
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'Fail'
        
    # Find subjects below 40
    failed_subjects = []
    for i, mark in enumerate(marks):
        if mark < 40:
            failed_subjects.append(f"Subject {i+1}")
            
    # Print the results
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")
    
    if failed_subjects:
        print(f"Subjects below 40: {', '.join(failed_subjects)}")
    else:
        print("Subjects below 40: None")

if __name__ == "__main__":
    # Sample Input
    name = "Aarav"
    roll = 101
    marks = [88.5, 35.0, 76.0, 92.5, 48.0]
    
    # Run the function
    analyze_result(name, roll, marks)
