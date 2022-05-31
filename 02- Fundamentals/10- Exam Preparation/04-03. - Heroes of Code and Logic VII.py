n = int(input())
dict = {}
for i in range(n):
    command_list1 = input().split(" ")
    name = command_list1[0]
    hp = int(command_list1[1])
    mp = int(command_list1[2])
    dict[name] = [hp, mp]

while True:
    command = input()

    if command != "End":
        command_list = command.split(" - ")
        name = command_list[1]
        if command_list[0] == "CastSpell":
            mp = int(command_list[2])
            spell_name = command_list[3]
            if dict[name][1] >= mp:
                dict[name][1] -= mp
                print(f"{name} has successfully cast {spell_name} and now has {dict[name][1]} MP!")
            else:
                print(f"{name} does not have enough MP to cast {command_list[3]}!")
        elif command_list[0] == "TakeDamage":
            damage = int(command_list[2])
            attacker = command_list[3]
            dict[name][0] -= damage
            if dict[name][0] > 0:
                print(f"{name} was hit for {damage} HP by {attacker} and now has {dict[name][0]} HP left!")
            else:
                print(f"{name} has been killed by {attacker}!")
                dict.pop(name)
        elif command_list[0] == "Recharge":
            mp = int(command_list[2])
            if dict[name][1] + mp >200:
                mp = 200 - dict[name][1]
            dict[name][1] += mp
            print(f"{name} recharged for {mp} MP!")
        elif command_list[0] == "Heal":
            hp = int(command_list[2])
            if dict[name][0] + hp > 100:
                hp = 100 - dict[name][0]
            dict[name][0] += hp
            print(f"{name} healed for {hp} HP!")
    else:
        break

for key in dict:
    print(f'{key}')
    print(f'  HP: {dict[key][0]}')
    print(f'  MP: {dict[key][1]}')
