# Constraint Satisfaction Problem (CSP)
# Timetable Scheduling using Backtracking

subjects = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

# Constraints: These pairs cannot have the same time slot
constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI")
]

# Check whether assigning a slot is valid
def is_valid(subject, slot, assignment):
    for sub1, sub2 in constraints:
        if subject == sub1 and sub2 in assignment:
            if assignment[sub2] == slot:
                return False

        if subject == sub2 and sub1 in assignment:
            if assignment[sub1] == slot:
                return False

    return True


# Backtracking function
def backtrack(assignment):
    # If all subjects are assigned
    if len(assignment) == len(subjects):
        return assignment

    # Select an unassigned subject
    for subject in subjects:
        if subject not in assignment:

            # Try every available time slot
            for slot in time_slots:

                if is_valid(subject, slot, assignment):
                    assignment[subject] = slot

                    result = backtrack(assignment)

                    if result is not None:
                        return result

                    # Backtrack
                    del assignment[subject]

            return None


# Solve the CSP
solution = backtrack({})


# Display final timetable
print("Final Timetable")
print("-------------------------")

for subject in subjects:
    print(subject, "->", solution[subject])