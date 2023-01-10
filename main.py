PLACEHOLDER = '[name]'

with open('./Input/Letters/starting_letter.txt') as file:
    starting_letter = file.read()

with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

for name in names:
    name = name.strip('\n')
    letter = starting_letter.replace(PLACEHOLDER, name)
    filename = f'letter_for_{name}.txt'
    with open(f'./Output/ReadyToSend/{filename}', mode='w') as file:
        file.write(letter)