cities = {}
while True:
    command = input()
    if command == "Sail":
        break

    city, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)

    if city not in cities:
        cities[city] = {'population': population, 'gold': gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold

while True:
    command = input()
    if command == "End":
        break
    parts = command.split("=>")
    action = parts[0]
    if action == "Plunder":
        town = parts[1]
        people = int(parts[2])
        gold = int(parts[3])

        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        town = parts[1]
        gold = int(parts[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, data in cities.items():
        print(f"{town} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
