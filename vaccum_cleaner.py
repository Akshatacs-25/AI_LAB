
def vacuum_cleaner():
    rooms = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    location = 'A'

    while 'Dirty' in rooms.values():
        print("Location:", location)

        if rooms[location] == 'Dirty':
            print("Cleaning room", location)
            rooms[location] = 'Clean'
        else:
            print("Room is already clean")

        if location == 'A':
            location = 'B'
        else:
            location = 'A'

    print("\nAll rooms are clean!")
    print(rooms)


vacuum_cleaner()
