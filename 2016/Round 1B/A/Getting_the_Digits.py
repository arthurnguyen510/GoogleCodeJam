
def number_inside(number, check_number):
    check = check_number
    original_number = number
    for letter in original_number:
        if len(check):
            for iter_letter in range(len(check)):
                if check[iter_letter] == letter:
                    check = check[:iter_letter] + check[iter_letter + 1:]
                    break

    if not len(check):
        for letter in check_number:
            for iter_letter in range(len(original_number)):
                if letter == original_number[iter_letter]:
                    original_number = original_number[:iter_letter] + original_number[iter_letter + 1:]
                    break
        return True, original_number
    return False, original_number


def find_numbers(number):
    dict_of_numbers = {"ZERO": '0',
                       "EIGHT": '8',
                       "TWO": '2',
                       "FOUR": '4',
                       "SIX": '6',
                       "FIVE": '5',
                       "THREE": '3',
                       "SEVEN": '7',
                       "NINE": '9',
                       "ONE": '1',}

    list_of_used_numbers = ''

    for check_number in dict_of_numbers.keys():
        number_in = True
        while number_in:
            number_in, number = number_inside(number, check_number)
            if number_in:
                list_of_used_numbers += dict_of_numbers[check_number]

    return list_of_used_numbers, number


def find_numbers_in_test(input_file):
    with open(input_file) as input_file:
        next(input_file)
        count = 1
        for line in input_file:
            line = line.strip()
            used_numbers, rest_of_numbers = find_numbers(line)
            print('Case #{0}: {1}'.format(str(count), used_numbers))
            count += 1


if __name__ == '__main__':
    find_numbers_in_test('/Users/arthurnguyen/Downloads/A-small-practice.in')