def flights(*args):
    dict = {}
    for idx in range(0,len(args)+1, 2 ):
        print(args[idx])
        if args[idx] != "Finish":
            if args[idx] not in dict:
                dict[args[idx]] = 0
            dict[args[idx]] += args[idx + 1]
        else:
            break
    return dict



# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
#
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
#
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))