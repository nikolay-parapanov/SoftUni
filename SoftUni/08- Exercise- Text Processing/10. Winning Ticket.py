input_list = input().split(", ")

for item in input_list:
    item = item.strip()
    if len(item) == 20:
        counter_left = 0
        counter_right = 0
        left_part = item[:10]
        right_part = item[10:]
        for symbol in range(1, len(left_part)):
            if left_part[symbol] in "@#$^" and left_part[symbol] == left_part[symbol - 1]:
                counter_left += 1
                winning_symbol_left = left_part[symbol]
            else:
                if counter_left < 4:
                    counter_left = 0

        for symbol in range(1, len(right_part)):
            if right_part[symbol] in "@#$^" and right_part[symbol] == right_part[symbol - 1]:
                counter_right += 1
                winning_symbol_right = right_part[symbol]
            else:
                if counter_right < 4:
                    counter_right = 0

        if (counter_left == counter_right) and (counter_left == 9) and winning_symbol_right == winning_symbol_left:
            print(f'ticket "{item}" - 10{winning_symbol_left} Jackpot!')
        elif (counter_right + 1 >= 6) and (counter_left + 1 >= 6) and winning_symbol_right == winning_symbol_left:
            print(f'ticket "{item}" - {min(counter_left, counter_right) + 1}{winning_symbol_left}')
        else:
            (print(f'ticket "{item}" - no match'))

    elif len(item) != 20:
        print("invalid ticket")
