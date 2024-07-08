import math
import random


def is_number(n):
    """
    Check if the input is a number.
    """
    return n.isnumeric()


def mae(y_true, y_pred):
    """
    Mean Absolute Error (MAE) loss function
    """
    return sum(abs(y_t - y_p) for y_t, y_p in zip(y_true, y_pred)) / len(y_true)


def mse(y_true, y_pred):
    """
    Mean Absolute Error (MSE) loss function.
    """
    return sum((y_t - y_p) ** 2 for y_t, y_p in zip(y_true, y_pred)) / len(y_true)


def rmse(y_true, y_pred):
    """
    Root Mean Squared Error (RMSE) loss functions.
    """
    return math.sqrt(mse(y_true, y_pred))

# Question 7 (Multiple choice)
def calc_ae(y, y_hat):
    return abs(y - y_hat)


y_7 = 1
y_hat_7 = 6
assert calc_ae(y_7, y_hat_7) == 5
y_7 = 2
y_hat_7 = 9
print(calc_ae(y_7, y_hat_7))

# Question 8 (Multiple choice)
def calc_se(y_8, y_hat_8):
    return (y_8 - y_hat_8) ** 2


y_8 = 4
y_hat_8 = 2
assert calc_se(y_8, y_hat_8) == 4
print(calc_se(2, 1))


def main():
    num_samples = input('Input number of samples: ')

    if not is_number(num_samples):
        print('number of samples must be an integer')
        return

    num_samples = int(num_samples)

    loss_name = input('Input loss name (MAE|MSE|RMSE): ')

    y_true = [random.uniform(0, 10) for _ in range(num_samples)]
    y_pred = [random.uniform(0, 10) for _ in range(num_samples)]

    if loss_name == 'MAE':
        loss = mae(y_true, y_pred)
    elif loss_name == 'MSE':
        loss = mse(y_true, y_pred)
    elif loss_name == 'RMSE':
        loss = rmse(y_true, y_pred)
    else:
        print(f'{loss_name} is not supported')
        return

    print(f'Loss name: {loss_name}')

    for i, (y_p, y_t) in enumerate(zip(y_pred, y_true)):
        print(f'sample: {i}, pred: {y_p}, target: {y_t}')

    print(f'final {loss_name}: {loss}')


if __name__ == "__main__":
    main()
