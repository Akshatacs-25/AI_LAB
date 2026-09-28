state = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

while True:

    print("\nCurrent location:", location)
    print("Room status:", state[location])

    if state[location] == "Dirty":
        action = "Suck"
        state[location] = "Clean"

    elif location == "A":
        action = "Right"
        location = "B"

    else:
        action = "Left"
        location = "A"

    print("Action:", action)

    if state["A"] == "Clean" and state["B"] == "Clean":
        print("Both rooms are clean!")
        break