users = {
    'deematt': {
        'first': 'damilola',
        'last': 'kajola',
        'location': 'ikotun',
    },

    'berryboy': {
        'first': 'Segun',
        'last': 'Kanjuola',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    