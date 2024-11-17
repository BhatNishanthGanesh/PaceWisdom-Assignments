# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.


no_of_classes_held = int(input("Enter the number of classes held"))
no_of_classes_attended = int(input("Enter the number of attended classes"))

attendence_percent = (no_of_classes_attended/no_of_classes_held)*100
print(attendence_percent)

if(attendence_percent>75):
    print("Allowed")
else:
    print("Not Allowed")    