grades={
    ("john","math"):5,
    ("alice","biology"):4,
    ("bob", "physics"): 3.5,
    ("eve", "music"): 5,
    ("john", "english"): 4,

}

print(grades[("john","math")])

grades[("bob", "math")]=3
print(grades)


#how to get all the students names
keys=list(grades.keys())
print(keys)
student, subject=keys[0]
print(students)