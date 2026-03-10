course_number = {"cs101": 3004, "cs102": 4501, "cs103": 6755, "nt110": 1244, "cm241": 1411}
instructor = {"cs101": "Haynes", "cs102": "Alvarado", "cs103": "Rich", "nt110": "Burke", "cm241": "Lee"}
meeting_time = {"cs101": "8:00 a.m.", "cs102": "9:00 a.m.", "cs103": "10:00 a.m.", "nt110": "11:00 a.m.", "cm241": "1:00 p.m."}
course = input("Enter a course number: ")

if course in course_number:
    print("Course Number: ", course_number[course])
    print("Instructor: ", instructor[course])
    print("Meeting Time: ", meeting_time[course])
else:    print("Invalid course number. Please enter a valid course number.")
