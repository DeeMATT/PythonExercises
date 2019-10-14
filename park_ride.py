"""
    A program for park users of all ages to select a ride of choice

                                                                    """

available_rides = {'1': "Scenic River Cruise", '2': "Carnival Carousel",
                   '3': "Jungle Adventure Water Splash",
                   '4': "Downhill Mountain Run",
                   '5': "The Regurgitator", }

print("Welcome to our Theme Park", "\n\nThese are the available rides:\n")

# A loop to display the available rides
for numb, ride in available_rides.items():
    print(numb + '.' + ride)

# Ask the user's choice of ride and age
selected_num = int(input("\nPlease enter the ride number you want: "))
age = int(input("Kindly enter your age real age in numbers"))

eligibility = "You are eligible to take this ride"
permit = "Go on and enjoy your ride"
denial = "Sorry, you are ineligible to take this ride"

if selected_num == 1:
    print("You have selected the " + available_rides['1'])
    print("There are no age limits for this ride")
    print(permit)

elif selected_num == 2:
    print("You have selected the " + available_rides['2'])
    if age >= 3:
        print(eligibility)
        print(permit)
    else:
        print(denial)

elif selected_num == 3:
    print("You have selected the " + available_rides['3'])
    if age >= 6:
        print(eligibility)
        print(permit)
    else:
        print(denial)

elif selected_num == 4:
    print("You have selected the " + available_rides['4'])
    if age >= 12:
        print(eligibility)
        print(permit)
    else:
        print(denial)
elif selected_num == 5:
    print("You have selected the " + available_rides['5'])
    if age >= 12 or age < 70:
        print(eligibility)
        print(permit)
    else:
        print(denial)
