activities = ["robotics", "coding", "science", "arts"]

name = input("Enter your name: ").lower()
age = int(input("Enter your age: "))
activity_choice = input("Choose an activity: ")

if name.strip() and 12 >= age <= 18 and activity_choice not in activities:
    print("Registration Successful")

if name.strip() or activity_choice in activities or 12 >= age <= 18:
    if not name.strip() and activity_choice not in activities and not 12 >= age <= 18:
        print("Invalid name, activity, and age. Enter a name, valid activity, and a whole number ranging from 12 to 18.")
    elif not name.strip() and activity_choice not in activities:
        print("Invalid name and activity. Enter a name and a valid activity.")
    elif not name.strip() and not 12 >= age <= 18:
        print("Invalid name and age. Enter a name and a whole number ranging from 12 to 18.")
    elif not 12 >= age <= 18 and activity_choice not in activities:
        print("Invalid age and activity. Enter a whole number ranging from 12 to 18 and a valid activity.")
    elif name.strip():
        print("Invalid name. Enter a name.")
    elif not 12 >= age <= 18:
        print("Invalid age. Enter a whole number ranging from 12 to 18.")