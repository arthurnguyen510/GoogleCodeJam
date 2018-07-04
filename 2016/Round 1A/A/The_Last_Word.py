

def insert_and_shift(letter, number, list_of_letters):
    list_a = list_of_letters[:number]
    list_b = list_of_letters[number:]

    return list_a + letter + list_b


def form_last_word(word):
    final_word = ''
    current_spot = 0
    for letter in word:
        if final_word != '':

            if final_word[current_spot] > letter:
                final_word = insert_and_shift(letter, len(final_word), final_word)
            else:
                final_word = insert_and_shift(letter, current_spot, final_word)
        else:
            final_word = letter
    return final_word


def get_last_word(input_file):
    with open(input_file) as input_file:
        next(input_file)
        count = 1
        for line in input_file:
            final_word = form_last_word(line.split())
            print('Case #{0}: {1}'.format(str(count), final_word))
            count += 1


if __name__ == '__main__':
    get_last_word('/Users/arthurnguyen/Downloads/A-small-practice.in')