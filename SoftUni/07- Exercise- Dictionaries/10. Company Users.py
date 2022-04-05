company_dict = {}

command = input()
while command != "End":
    command_list = command.split(" -> ")
    company = command_list[0]
    id = command_list[1]

    if company not in company_dict:
        company_dict[company] = []
    if id not in company_dict[company]:
        company_dict[company].append(id)
    command = input()

for company, id in company_dict.items():
    print(f"{company}")
    for id in company_dict[company]:
        print(f"-- {id}")

