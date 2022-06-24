def start_spring(**kwargs):
    result = ''
    dict = {}
    for item, type in kwargs.items():
        if type not in dict:
            dict[type] = []
        dict[type].append(item)

    sorted_dict = sorted(dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple in sorted_dict:
        type, item = tuple
        items_sorted = sorted(item)
        result += f'{type}:\n'
        for item in items_sorted:
            result += f'-{item}\n'

    return result

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }

start_spring(**example_objects)
