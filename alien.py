alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['x_position'] = 6
alien_0['y_position'] = 12
print(alien_0)

alien_1 = {}
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)

del alien_0['points']
print(alien_0)
