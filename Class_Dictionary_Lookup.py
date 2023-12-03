roomNumber = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
    }
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
    }
classTime = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
    }

userSearch = input("Which class would you like information on: ")
print("Room Number: ", roomNumber[userSearch])
print("Class Instructor: ", instructors[userSearch])
print("Class Start Time: ", classTime[userSearch])
