def flip_pancake(pancake, length):
    flipped = ''
    count = 0
    for x in pancake:
        if count <= length:
            if x == '-':
                flipped += '+'
            elif x == '+':
                flipped += '-'
        else:
            flipped += x
        count += 1
    return flipped


def is_happy(stack_of_pancakes):
    non_happy = 0
    for pancake in stack_of_pancakes:
        if pancake == '-':
            non_happy += 1

    if non_happy == len(stack_of_pancakes):
        stack_of_pancakes = flip_pancake(stack_of_pancakes, len(stack_of_pancakes) - 1)
        return True, 1, stack_of_pancakes
    elif non_happy == 0:
        return True, 0, stack_of_pancakes
    else:
        return False, 0, stack_of_pancakes


def serve_pancake(stack_of_pancakes):
    flips = 0

    if len(stack_of_pancakes) == 0:
        return flips

    if len(stack_of_pancakes) == 1:
        if stack_of_pancakes[0] == '-':
            flips += 1
            return flips
        else:
            return flips
    all_happy = False

    while not all_happy:
        for iter_pancake in range(1, len(stack_of_pancakes)):
            if stack_of_pancakes[iter_pancake] != stack_of_pancakes[iter_pancake - 1]:
                stack_of_pancakes = flip_pancake(stack_of_pancakes, iter_pancake - 1)
                flips += 1
        all_happy, curr_flips, stack_of_pancakes = is_happy(stack_of_pancakes)

        flips += curr_flips

    return flips


def serve_pancake_w_file(input_file):
    with open(input_file) as input_file:
        next(input_file)
        for line in input_file:
            print(line.strip(), serve_pancake(line.strip()))


if __name__ == '__main__':
    serve_pancake_w_file('GoogleCodeJam/2016/QualificationRound/B/B-small-practice.in')
