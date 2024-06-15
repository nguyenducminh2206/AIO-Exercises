# Question 1
print('Question 1')

def max_sliding_window(list, k):
    """
    Find maximum values for each window.
    """
    max_values_list = []
    for i in range(len(list) - k + 1):
        sublist = list[i:i+k]
        max_values = max(sublist)
        max_values_list.append(max_values)
    return max_values_list


assert max_sliding_window([3, 4, 5, 1, -44], 3) == [5, 5, 5]

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window((num_list), k))

# Question 2
print('Question 2')

def count_chars(word):
    """
    Count appearence of a characters.
    """
    dict_for_chars = {}

    for letters in word:
        if letters in dict_for_chars:
            dict_for_chars[letters] += 1
        else:
            dict_for_chars[letters] = 1

    return dict_for_chars

assert count_chars("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(count_chars('smiles'))

# Question 3
print('Question 3')

def word_count(file_path):
    word_dict = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    return word_dict


file_path = r'C:\Users\PC\AIO-Exercises\Exercise_week_2\P1_data.txt'
result = word_count(file_path)

assert result['who'] == 3
print(result['man'])

# Question 4
print('Question 4')

def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)
    D = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        D[i][0] = i

    for j in range(1, n + 1):
        D[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if source[i - 1] == target[j - 1] else 1
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] +
                          1, D[i - 1][j - 1] + cost)

    return D[m][n]


assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))

# Question 5
print("Question 5")

def check_the_number(n):
    list_of_numbers = []

    for i in range(1, 5):
        list_of_numbers.append(i)

    if n in list_of_numbers:
        results = "True"
    else:
        results = "False"
    return results

N = 7
assert check_the_number(N) == "False"

N = 2
results = check_the_number(N)
print(results)

# Question 6
print('Question 6')

def my_function_6(data, max, min):
    result = []

    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result

my_list = [5, 2, 5, 0, 1]
assert my_function_6(max=1, min=0, data=my_list) == [1, 1, 1, 0, 1]

my_list = [10, 2, 5, 0, 1]
print(my_function_6(max=2, min=1, data=my_list))

# Question 7
print('Question 7')

def my_function_7(x, y):
    x.extend(y)
    return x

list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0,0]
assert my_function_7(list_num1, my_function_7(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print(my_function_7(list_num1, my_function_7(list_num2, list_num3)))

# Question 8
print('Question 8')
def my_function_8(n):
    return min(n)

my_list = [1, 22, 93, -100]
assert my_function_8(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function_8(my_list))

# Question 9
print('Question 9')

def my_function_9(n):
    return max(n)

my_list = [1001, 9, 100, 0]
assert my_function_9(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function_9(my_list))

# Question 10
print('Question 10')
def my_function_10(integers, number=1):
    return any(element == number for element in integers)

my_list = [1, 3, 9, 4]
assert my_function_10(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(my_function_10(my_list, 2))

# Question 11
print('Question 11')
def my_function_11(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)

assert my_function_11([4, 6, 8]) == 6
print(my_function_11())

# Question 12
print('Question 12')

def my_function_12(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var
assert my_function_12([3, 9, 4, 5]) == [3, 9]
print(my_function_12([1, 2, 3, 5, 6]))

# Question 13
print('Question 13')

def my_function_13(y):
    var = 1
    while y > 1:
        var *= y
        y -= 1
    return var

assert my_function_13(8) == 40320
print(my_function_13(4))

# Question 14
print('Question 14')

def my_function_14(x):
    return x[::-1]

x = 'I can do it'
assert my_function_14(x) == 'ti od nac I'

x = 'apricot'
print(my_function_14(x))

# Question 15
print('Question 15')

def function_helper(x):
    if x > 0:
        return 'T'
    else:
        return 'N'

def my_function_15(data):
    res = [function_helper(x) for x in data]
    return res

data = [10, 0, -10, -1]
assert my_function_15(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(my_function_15(data))

# Question 16
print('Question 16')

def function_helper_16(x, data):
    for i in data:
        if x == i:
            return 0
    return 1

def my_function_16(data):
    res = []
    for i in data:
        if function_helper_16(i, res):
            res.append(i)
    return res

lst = [10, 10, 9, 7, 7]
assert my_function_16(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(my_function_16(lst))