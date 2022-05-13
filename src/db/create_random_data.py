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


# count = 1
# for _ in range(20):
# random_list = f'{random.choice(first_name)} {random.choice(last_name)}'
# random_name = ''.join(random.choice(first_name) + ' ' + random.choice(last_name))
# random_char = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
# random_group = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
# print(random_name)
# count += 1
# random_group = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

# for _ in range(10):
#     random_char = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
#     random_dig = ''.join(random.choice(string.digits) for _ in range(2))
#     print(random_char + '-' + random_dig)
# print((first_name))
# print(len(last_name))
# for _ in range(10):
#     print(get_groups())

# for k, v in courses.items():
#     print(f'{k} - {v}')
# for _ in range(10):
#     print(get_groups())
# for i in get_random_group_id():
# print(get_random_group_id())
# k = 1
# j = 1
# for i in (get_random_digit_in_range(200, 10, 10, 30)):
#     # print(i)
#     count = 1
#     print(f'Group №{j} has {i} students:')
#     while count <= i:
#         print(f'{get_random_student_first_name()} {get_random_student_last_name()}, group_id: {j}')
#         count += 1
#     j += 1
# print(get_random_digit(200, 10, 10, 30))
# for _ in range(10):
#     print(random.choice([0, random.randrange(10, 30)]))
# print(get_groups())