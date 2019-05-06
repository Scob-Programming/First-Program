#       How to calculate the day of the week using the Doomsday Algorithm
#
# 08/28/1990 7, 6, 1, 3, 17, 3, -1
# Step On:      Last two digits of year / 12 = a
#               eg. 54 / 12 = 4
# Step Two:     Last two digits of year % (a * 12) = b
#               eg. 54 % (4 * 12) = 6
# Step Three:   b / 4 = c
#               eg. 6 / 4 = 1
# Step Four:    Find the century's anchor day
#               eg. 2000-2099 = Tuesday(2)
# Step Five:    a + b + c + anchor day = d
#               eg. 4 + 6 + 1 + 2 = 13
# Step Six:     d % 7 = e
#               eg. 13 % 7 = 6
# Step Seven:   Find the closest Doomsday
#               eg. 6/13
# Step Eight:   Count forward or backwards from the Doomsday to the specified date
#               eg. 06/16/2054 is +3 from the Doomsday which makes it a Friday(5)
#
#       Doomsday of each Month
#
# January:      1/3 or 1/4 on a leap year
# February:     2/28 or 2/29 on a leap year
# March:        3/0
# April:        4/4
# May:          5/9
# June:         6/6
# July:         7/11
# August:       8/8
# September:    9/5
# October:      10/10
# November:     11/7
# December:     12/12


# Dictionary to convert doomsday values to weekday strings
weekDict = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
# Dictionary to convert century anchor day value to doomsday value
anchorDictionary = {3: 3, 0: 2, 1: 0, 2: 5}
# Variables to store user entered date individual values
userDay = 0
userMonth = 0
userYear = 0
# Variables to compare User entered date against for calculations
monthYear = 12
daysMonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
daysMonthLeap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# If True the program loops if False it stops
runDoom = True


# Function to process doomsday algorithm
def doomsday(year, day, anchor, nearanchor):
    a = int(year) / 12
    a = int(str(a).split(".")[0])
    b = int(year) % 12
    c = (int(year) % 12) / 4
    c = int(str(c).split(".")[0])
    d = ((a + b + c) + int(anchor)) % 7
    answer = ((int(day) - int(nearanchor)) + d) % 7
    return answer


# Function to calculate the nearest anchor day
def anchordays(leapyear, month, day):
    months = {1: [3, 10, 17, 24, 31], 2: [0, 7, 14, 21, 28], 3: [0, 7, 14, 21, 28], 4: [4, 11, 18, 25], 5: [2, 9, 16, 23, 30],
              6: [6, 13, 20, 27], 7: [4, 11, 18, 25], 8: [1, 8, 15, 22, 29], 9: [5, 12, 19, 26], 10: [3, 10, 17, 24, 31],
              11: [0, 7, 14, 21, 28], 12: [5, 12, 19, 26]}
    leapmonths = {1: [4, 11, 18, 25], 2: [1, 8, 15, 22, 29], 3: [0, 7, 14, 21, 28], 4: [4, 11, 18, 25], 5: [2, 9, 16, 23, 30],
                  6: [6, 13, 20, 27], 7: [4, 11, 18, 25], 8: [1, 8, 15, 22, 29], 9: [5, 12, 19, 26], 10: [3, 10, 17, 24, 31],
                  11: [0, 7, 14, 21, 28], 12: [5, 12, 19, 26]}

    if leapyear:
        result = [x for x in leapmonths[month] if x >= day]
        try:
            if result[0] >= day:
                return result[0]
        except:
            result = [x for x in leapmonths[month] if x >= (day - 7)]
            return result[0] + 7
    else:
        result = [x for x in months[month] if x > day]
        try:
            if result[0] >= day:
                return result[0]
        except:
            result = [x for x in months[month] if x >= (day - 7)]
            return result[0] + 7


# Function to calculate leap years using stored user input
def leapCalc(self):
    if (int(userYear) / 4) == round(self / 4):
        if (int(userYear) / 100) == round(self / 100):
            if (int(userYear) / 400) == round(self / 400):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Main body of the program
while runDoom:
    print("Enter the date.(mm/dd/yyyy) ")
    userDate = input()
    if "/" in userDate[2] and userDate[5]:

        # Splitting the User input into the appropriate variables as integers
        userMonth = userDate.split("/")[0]
        userDay = userDate.split("/")[1]
        userYear = userDate.split("/")[2]

        # Calculating Leap year status using User input
        leapValue = leapCalc(int(userYear))

        # If statement to check if User input is within required range
        if int(userMonth) <= monthYear and int(userDay) <= daysMonth[int(userMonth)]:
            userYearLastTwo = userYear[2] + userYear[3]
            userYearFirstTwo = userYear[0] + userYear[1]
            userAnchor = anchorDictionary[(int(userYearFirstTwo) % 4)]
            userNearAnchor = str(anchordays(leapValue, int(userMonth), int(userDay)))
            result = doomsday(userYearLastTwo, userDay, userAnchor, userNearAnchor)
            print(userDate + " was a " + weekDict[result])
            print("")
            print("Enter another date?")
            runAgain = input()

            # Checking if User wants to exit program
            if "y" in runAgain[0].lower():
                print("")
            else:
                quit()

        else:
            print("Please enter a valid Date.")
    else:
        print("Please use the proper format.")
