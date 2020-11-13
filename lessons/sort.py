# nums = [1,4,2,5,8,7,2,4, 8,1,6,0]

# print(sorted(nums))

# names = ['shaun', 'ryu', 'abe', 'abe',  'shau', 'matthew']
# print(sorted(names))

# print(set(nums))

# print(set(names))

# ninjas = {'ryu': 'black', 'yoshi': 'red', 'crystal': 'black'}
# print(set(ninjas.values()))


def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

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

belt_count(ninja_belts)
