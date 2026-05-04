from aircraft import Aircraft

model = input("Enter aircraft model:\n")
plane = Aircraft(model)

altitude = 0

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()

    if command == "X":
        break

    parts = command.split()

    if len(parts) != 2:
        continue

    action, value = parts
    value = int(value)

    if action == "A":
        altitude += value
    elif action == "D":
        altitude -= value

print(f"Final altitude: {altitude} feet")