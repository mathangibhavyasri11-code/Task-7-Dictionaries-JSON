# Q2. Store student details using dictionary
import json
students = {
    "101": {
        "name": "Bhavya",
        "age": 20,
        "course": "CSE",
        "marks": 85
    },
    "102": {
        "name": "Rahul",
        "age": 21,
        "course": "ECE",
        "marks": 78
    }
}
# Q3. Access keys and values
print("Q3 Output:")
print("Student IDs:", students.keys())
print("Details of Student 101:", students["101"])
# Q4. Update and delete entries
# Update marks
students["101"]["marks"] = 90
# Delete student 102
del students["102"]
print("\nQ4 Output (After Update & Delete):")
print(students)
# Q5. Loop through dictionary
print("\nQ5 Output (Looping through dictionary):")
for student_id, details in students.items():
    print("\nID:", student_id)
    for key, value in details.items():
        print(key.capitalize(), ":", value)
# Q6. Convert dictionary to JSON
json_data = json.dumps(students, indent=4)
print("\nQ6 Output (Dictionary converted to JSON format):")
print(json_data)
# Q7. Save JSON to file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
print("\nQ7 Output: JSON saved to students.json")
# Q8. Read JSON back into Python
with open("students.json", "r") as file:
    data = json.load(file)
# Q9. Print clean formatted output
print("\nQ9 Output (Reading from JSON file):")
print(json.dumps(data, indent=4))