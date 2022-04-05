input_list = []
dictionary_primary = {'shards': 0, 'fragments': 0, 'motes': 0}
dictionary_secondary = {}
a=5


while True:
    command = input().lower()
    if command.isalpha():
        input_list = command.split()
        for index in range(0, len(input_list) - 1, 2):
            quantity = input_list[index]
            material = input_list[index + 1].lower()
            if material in ['shards', 'fragments', 'motes']:
                dictionary_primary[material] += int(quantity)
            else:
                dictionary_secondary[material] = int(quantity)

            if material == "shards" and dictionary_primary[material] >= 250:
                print("Shadowmourne obtained!")
                dictionary_primary[material] -= 250
                break
            elif material == 'fragments' and dictionary_primary[material] >= 250:
                print("Valanyr obtained!")
                dictionary_primary[material] -= 250
                break
            elif material == "motes" and dictionary_primary[material] >= 250:
                print("Dragonwrath obtained!")
                dictionary_primary[material] -= 250
                break
    else:
        break

a=5

print(f"shards: {dictionary_primary['shards']}")
print(f"fragments: {dictionary_primary['fragments']}")
print(f"motes: {dictionary_primary['motes']}")

for material, quantity in dictionary_secondary.items():
    print(f"{material}: {quantity}")