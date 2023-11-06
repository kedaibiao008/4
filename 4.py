import itertools

def generate_combinations():
    for first_char in 'abcdefghijklmnopqrstuvwxyz':
        for second_char in 'abcdefghijklmnopqrstuvwxyz0123456789':
            for third_char in 'abcdefghijklmnopqrstuvwxyz0123456789':
                for fourth_char in 'abcdefghijklmnopqrstuvwxyz0123456789':
                    yield f"{first_char}{second_char}{third_char}{fourth_char}"

def main():
    with open('4l.txt', 'w') as file:
        for combination in generate_combinations():
            if combination[1:4] == combination[0] * 3:
                file.write(combination + '\n')

if __name__ == '__main__':
    main()
