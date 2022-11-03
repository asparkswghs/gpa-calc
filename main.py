#!/usr/bin/env python3
print("Calculate GPA:")
while True:
  all_gpas = []
  for i in range(user_classes):
    course = input("What course do you want calculated? ")
    grade_in = input("What letter grade do you have in " + what_course + " ?")
    grade = grade_in.lower()

    if grade == "a" or grade == "a-":
      gpa = 4.0
    elif grade == "b+":
      gpa = 3.5
    elif grade == "b":
      gpa = 3.0
    elif grade == "c+":
      gpa = 2.5
    elif grade == "c":
      gpa = 2.0
    elif grade == "d+":
      gpa = 1.5
    elif grade == "d" or grade == "d-":
      gpa = 1.0
    elif grade == "f":
      gpa = 0.5
    print("Your GPA for " + course + " is: " + str(gpa))
    all_gpas.append(gpa)
    avg_gpa = sum(all_gpas) / user_classes
  avg_gpa = all_gpas / user_classes
  print("Your average GPA is: " + str(avg_gpa))
  user_says = input("Do you want to calculate another GPA? (yes/no) ")
  user_classes = int(input("How many classes do you have? "))
