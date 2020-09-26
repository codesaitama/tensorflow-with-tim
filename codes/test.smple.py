def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    print((len(arrivals) / 2))
    return (arrivals.index(name) + 1 != len(arrivals)) and (arrivals.index(name) >= (len(arrivals) / 2))

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
s = ['Paul', 'John', 'Ringo', 'George']

print(fashionably_late(s, 'Ringo'))
#print(fashionably_late(party_attendees, 'Ford'))