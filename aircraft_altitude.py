from aircraft import Aircraft

model = input("Enter aircraft model:\n")
plane = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")

    if command == "X":
        break

    action, value = command.split()
    value = int(value)

    if action == "A":
        plane.ascend(value)
    elif action == "D":
        plane.descend(value)

print(f"Final altitude: {plane.altitude} feet")