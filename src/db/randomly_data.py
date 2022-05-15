import random
import string

first_name = ('Alexader', 'Mykolay', 'Dmytro', 'Sergyi', 'Evgeny', 'Andry', 'Artem', 'Borys', 'Vitaly', 'Denys',
              'Igor', 'Mikhail', 'Nazar', 'Nikyta', 'Pavlo', 'Roman', 'Taras', 'Yurii', 'Yan', 'Yaroslav')

last_name = ('Melnik', 'Shevchenko', 'Bondarenko', 'Kovalenko', 'Tkachenko', 'Kravchenko', 'Polishchuk', 'Shevchuk',
             'Tkachuk', 'Moroz', 'Mazur', 'Pavlenko', 'Kulik', 'Shvets', 'Romanyuk', 'Gavrilyuk', 'Vasilenko',
             'Ishchenko', 'Litvin', 'Kozak')

subject = {'Ukrainian': "description Ukrainian",
           'Literature': "description Literature",
           'Geography': "description Geography",
           'English': "description English",
           'Math': "description Math",
           'Physics': "description Physics",
           'History': "description History",
           'Management': "description Management",
           'Marketing': "description Marketing",
           'Chemistry': "description Chemistry"}


def get_groups():
    random_char = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
    random_dig = ''.join(random.choice(string.digits) for _ in range(2))
    return random_char + '-' + random_dig


def get_random_student_first_name():
    return random.choice(first_name)


def get_random_student_last_name():
    return random.choice(last_name)


def get_random_subject():
    return random.choice(subject)


def get_random_group_id():
    return random.sample(range(1, 11), 10)


def get_random_course_id():
    return random.sample(range(1, 11), random.randrange(1, 4))


def get_random_digit_in_range(amount, count, start, end):
    '''
    :param amount: total
    :param count: the number of numbers by which to divide the total
    :param start: range start
    :param end: range end
    :return: list of count
    '''
    list_digit = []
    result = amount // count
    if result in range(start, end):
        while count > 1:
            if start == end:
                list_digit.append(amount // 2)
                list_digit.append(amount // 2)
                break
            random_digit = random.randrange(start, end)
            amount -= random_digit
            count -= 1
            list_digit.append(random_digit)
            min = count * 10 - 10
            max = count * 30
            remainder_min = amount - min
            remainder_max = amount + 30 - max
            if remainder_min < end:
                end = remainder_min
            if remainder_max > start:
                start = remainder_max
        else:
            list_digit.append(amount)
    else:
        raise Exception(f'{result} not in range {start} - {end}')
    return list_digit
