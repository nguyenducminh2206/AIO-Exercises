import numpy as np


def is_number(n):
    try:
        float(n)

    except ValueError:
        return False
    return True


def sigmoid(x):
    """
    Sigmoid activation function.

    """
    return 1 / (1 + np.exp(-x))


# Question 4 (Multiple choice)
print(round(sigmoid(2), 2))


def relu(x):
    """
    ReLu activation function.

    """
    return np.maximum(0, x)


def elu(x, alpha=0.01):
    """
    ELU activation function.

    """
    return x if x > 0 else alpha * (np.exp(x) - 1)


# Question 5 (Multiple choice)
assert round(elu(1)) == 1
print(round(elu(-1), 2))

# Question 6 (Multiple choice)


def calc_activation_func(x, act_name):
    if not is_number(x):
        return

    valid_x = int(x)

    if act_name == 'sigmoid':
        return sigmoid(valid_x)
    elif act_name == 'relu':
        return relu(valid_x)


assert calc_activation_func(x=1, act_name='relu') == 1
print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))


def main():
    x = input('Input x = ')

    # Check if the input is a number
    if not is_number(x):
        print('x must be a number')
        return

    valid_x = float(x)

    function_input = input('Input activation Function (sigmoid|relu|elu): ')

    if function_input == 'sigmoid':
        result = sigmoid(valid_x)
    elif function_input == 'relu':
        result = relu(valid_x)
    elif function_input == 'elu':
        result = elu(valid_x)
    else:
        print(f'{function_input} is not supported')
        return

    print(f'{function_input}: f({valid_x}) = {result}')


if __name__ == "__main__":
    main()
