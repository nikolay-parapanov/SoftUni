input_line = input()
address_book = dict()

while "-" in input_line:
    record = list(input_line.split("-"))
    name = record[0]
    number = record[1]
    address_book[name] = number

    input_line = input()

for _ in range(int(input_line)):
    search_name = input()
    if search_name in address_book:
        print(f"{search_name} -> {address_book[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")

