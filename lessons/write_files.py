# with open('lessons/files/write.txt', 'w') as write_file:
#     write_file.write("Hey there ninjas, python is awesome")
#     write_file.write("\nI love it so much, i dream in python")

with open('lessons/files/write.txt', 'w') as write_file: #w for write
    write_file.write("Hey there ninjas, python is awesome")
 
with open('lessons/files/write.txt', 'a') as write_file: #a for amend
    write_file.write("\nI love it so much, i dream in python")

quotes = [
    '\nI can resist everything except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('lessons/files/write.txt', 'a') as write_file: #a for amend
    write_file.writelines(quotes)


