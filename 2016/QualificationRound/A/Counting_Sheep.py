def find_all_digits(start):
    if int(start) == 0:
        return 'INSOMNIA'

    list_of_found_numbers = []

    number = start
    current_count = 0
    while len(list_of_found_numbers) < 10:
        current_count += 1
        curr_num = str(int(number) * current_count)
        for x in curr_num:
            int_x = int(x)
            if int_x not in list_of_found_numbers:
                list_of_found_numbers.append(int_x)

    return curr_num


def count_sheep(input_file):
    with open(input_file) as input_file:
        next(input_file)
        count = 1
        for line in input_file:
            start = line.strip()
            print('Case #' + str(count) + ':', find_all_digits(start))
            count += 1


if __name__ == '__main__':
    count_sheep('/Users/arthurnguyen/Downloads/A-small-practice.in')
