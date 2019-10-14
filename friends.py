
friend_0 = {'color': 'green', 'points': 5}
friend_1 = {'color': 'yellow', 'points': 10}
friend_2 = {'color': 'red', 'points': 15}

friends = [friend_0, friend_1, friend_2]

for friend in friends:
    print(friend)

print("...")

# Make an empty list for storing friends.
friends = []

# Make 30 friends with green colour.
for number in range(30):
    new_friend = {'color': 'green', 'points': 5, 'size': 'fat'}
    friends.append(new_friend)

for friend in friends[0:3]:
    if friend['color'] == 'green':
        friend['color'] = 'yellow'
        friend['size'] = 'thin'
        friend['points'] = 10

# Show the first 5 friends.
for friend in friends[:5]:
    print(friend)
print("...")

# Show how many friends have been created.
print("Total number of friends: " + str(len(friends)))
