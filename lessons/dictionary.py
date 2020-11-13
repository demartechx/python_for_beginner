# ninja_belts = {"crystal": "red", "ryu": "black",}
# # ninja_belts['crystal']
# # print(ninja_belts['crystal'])

# # name = 'ryu' in ninja_belts

# # print(name)

# ninja_belts.keys()
# list(ninja_belts.keys())

# ninja_belts.values()
# vals = list(ninja_belts.values())

# vals.count('black')

# ninja_belts['yoshi'] = 'red'
# # print(ninja_belts)

# person = dict(name="matt", age=22, height="6ft")
# print(person)

def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name:')
    ninja_belt = input('enter a belt colour:')
    ninja_belts[ninja_name] = ninja_belt


    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)
