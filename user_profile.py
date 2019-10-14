def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


kehinde = build_profile('Kehinde', 'Olaide',
                             location='abuja',
                             field='doctor')
taiwo = build_profile('Taiwo', 'Olaide',
                             location='lagos',
                             field='mechanic')

print(kehinde)
print(taiwo)