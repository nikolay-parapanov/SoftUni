country_list = input().split(", ")
town_list = input().split(", ")

result = dict(zip(country_list, town_list))

for country, town in result.items():
    print(f"{country} -> {town}")
