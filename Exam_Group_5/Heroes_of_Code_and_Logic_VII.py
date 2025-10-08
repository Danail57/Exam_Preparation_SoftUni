number_of_heroes = int(input())

heroes = {}

for _ in range(number_of_heroes):
    data = input().split()
    hero_name = data[0]
    hit_points = int(data[1])
    mana_points = int(data[2])
    heroes[hero_name] = {"HP": hit_points, "MP": mana_points}

while (command := input()) != "End":
    parts = command.split(" - ")
    action = parts[0]
    hero_name = parts[1]

    if action == "CastSpell":
        mana_points_required = int(parts[2])
        spell_name = parts[3]
        if heroes[hero_name]["MP"] >= mana_points_required:
            heroes[hero_name]["MP"] -= mana_points_required
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(parts[2])
        attacker = parts[3]
        heroes[hero_name]["HP"] -= damage
        if heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount = int(parts[2])
        current = heroes[hero_name]["MP"]
        recharge = min(200 - current, amount)
        heroes[hero_name]["MP"] += recharge
        print(f"{hero_name} recharged for {recharge} MP!")

    elif action == "Heal":
        amount = int(parts[2])
        current = heroes[hero_name]["HP"]
        heal = min(100 - current, amount)
        heroes[hero_name]["HP"] += heal
        print(f"{hero_name} healed for {heal} HP!")

for hero, stats in heroes.items():
    print(hero)
    print(f"  HP: {stats['HP']}")
    print(f"  MP: {stats['MP']}")
