print("Task 1 — Data Parsing & Profile Cleaning")

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []  # List to store cleaned student profiles to use them later

for stu in raw_students:
    clean_name = stu["name"].strip().title() # Remove leading/trailing spaces and convert to title case
    clean_roll = int(stu["roll"]) # Convert roll number from string to integer
    clean_marks = [int(m.strip()) for m in stu["marks_str"].split(",")] # Convert marks from strings to integers after splitting by comma and stripping spaces

    words = clean_name.split() # Split the cleaned name into first and last name
    check = all(w.isalpha() for w in words) # Check if all parts of the name are alphabetic and returns true if they are, otherwise false
    if check: # if the name is valid, assign a check mark to the label, otherwise assign a cross mark
        label = "✓ Valid name"
    else:
        label = "✗ Invalid name"

        
    print(f"\n{clean_name} - {label}") # Print the cleaned name along with the validation label

    print(f"\n{'=' * 50}")  
    print(f"Student : {clean_name}") # Print the full profile card
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print(f"{'=' * 50}\n")

    cleaned_students.append({
    "name": clean_name,
    "roll": clean_roll,
    "marks": clean_marks
    }) # Append the cleaned student profile to the list of cleaned students


for s in cleaned_students:
    if s["roll"] == 103: # found Priya Nair
        print(f"\n Roll 103 - ALL CAPS : {s['name'].upper()}") # Print Priya Nair's name in all uppercase letters
        print(f" Roll 103 - lowercase : {s['name'].lower()}") # Print Priya Nair's name in all lowercase letters
        break   # Exit the loop after finding and printing Priya Nair's name in different cases


print("\nTask 2 — Marks Analysis Using Loops & Conditionals")

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

def grade(m): # Function to determine the grade based on the marks
    if m >= 90:
        return "A+"
    elif m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 60:
        return "C"
    else:
        return "F"

print(f"\nGrade Report for {student_name}:")
for i in range(len(subjects)):
    subject = subjects[i]
    m = marks[i]
    subject_grade = grade(m)
    print(f"{subject}: {m} - Grade: {subject_grade}") # Loop through each subject and corresponding marks, calculate the grade using the grade function, and print the subject, marks, and grade in a formatted manner  

total_marks = sum(marks) # Calculate the total marks by summing up all the marks in the list using the built-in sum() function
avg_marks = round(total_marks / len(marks), 2) # Calculate the average marks and round it to 2 decimal places
max_marks = max(marks) # Find the maximum marks in the list
min_marks = min(marks) # Find the minimum marks in the list
highest_subject = subjects[marks.index(max_marks)] # Find the subject with the highest marks
lowest_subject = subjects[marks.index(min_marks)] # Find the subject with the lowest marks

print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {avg_marks:.2f}")
print(f"Highest Subject: {highest_subject} ({max_marks})")
print(f"Lowest Subject: {lowest_subject} ({min_marks})")

subj = subjects[:]
mark = marks[:]
count = 0

while True: # Loop to continuously ask the user for a subject until they choose to exit
    sub_input = input("\nEnter subject name (or 'done' to quit): ").strip()
    if sub_input.lower() == "done":
        break
    marks_input = input(f"Enter marks for '{sub_input}'(0-100): ").strip()
    try:
        new_mark = float(marks_input)
        if not (0<= new_mark <= 100):
            raise ValueError
        new_mark = int(new_mark)
    except ValueError:
        print("Invalid marks! Number must be between 0 and 100. Entry skipped.")
        continue # jumps to the next iteration of the loop if the marks input is invalid
    
    subj.append(sub_input) # Add the new subject to the list of subjects
    mark.append(new_mark) # Add the new marks to the list of marks
    count += 1 # Increment the count of new entries
    print(f"Added: {sub_input} - {new_mark}")

updated_avg = round(sum(mark) / len(mark), 2) # Recalculate the average marks after adding new entries
print(f"\n New Subjects added: {count}")
print(f"Updated Average Marks: {updated_avg:.2f}")



print("\nTask 3 — Class Performance Summary")
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

stu_results = []
for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    if avg >= 60:
        status = "Pass"
    else:        status = "Fail"
    stu_results.append((name, avg, status))

print(f"\n{'Student Name':<20} | {'Average Marks':>10} | {'Status':>5}")
print("-" * 50)
for name, avg, status in stu_results:
    print(f"{name:<20} | {avg:>10} | {status:>5}")

passed = []
failed = []

for i in stu_results:
    if i[2] == "Pass":
        passed.append(i)
    else: 
        failed.append(i)

topper = stu_results[0]
for i in stu_results:
    if i[1] > topper[1]:
        topper = i

total_avg = 0
for i in stu_results:
    total_avg += i[1] 
total_avg = round(total_avg / len(stu_results), 2)

print(f"\nStudents Passed: {len(passed)}")
print(f"Students Failed: {len(failed)}")
print(f"Class Average Marks: {total_avg:.2f}")
print(f"Topper: {topper[0]} with {topper[1]} marks")

print("\nTask 4 — String Manipulation Utility")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip() # Remove leading/trailing spaces of the essay
print(f"\nCleaned Essay:\n{clean_essay}")

title_essay = clean_essay.title() # Convert the essay to title case
print(f"\nTitle Case:\n{title_essay}")

python_count = clean_essay.count("python") # Count the occurrences of the word "python" in the essay
print(f"\nOccurrences of 'python': {python_count}") 

replaced_essay = clean_essay.replace("python", "Python 🐍") # Replace all occurrences of "python" with "Python" & its graphic
print(f"\nAfter Replacement:\n{replaced_essay}")

split_essay = clean_essay.split(". ") # Split the essay into sentences based on the period character
print(f"\nSentences:\n{split_essay}")

print("\n Numbered Sentences:")
i=1
for sentence in split_essay:
    last_char = sentence[-1]
    
    if last_char != ".":
        sentence += "." # Ensure each sentence ends with a period
        
        print(f"{i}. {sentence.strip()}") # Print each sentence with a number and remove any leading/trailing spaces
    
    i += 1
