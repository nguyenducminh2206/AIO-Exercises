import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


def get_column(data, index):
    result = data.iloc[:, index]  # Use pandas DataFrame to extract columns
    return result


def prepare_data(file_name_dataset):
    data = pd.read_csv(file_name_dataset)  # Use pandas to read CSV file

    tv_data = get_column(data, 0)          # TV column
    radio_data = get_column(data, 1)       # Radio column
    newspaper_data = get_column(data, 2)   # Newspaper column
    sales_data = get_column(data, 3)       # Sales column

    X = [tv_data.tolist(), radio_data.tolist(), newspaper_data.tolist()]
    y = sales_data.tolist()

    return X, y


X, y = prepare_data('Module_2/Exercise_Week_1/advertising.csv')


def implement_linear_regression(x_data, y_data, epoch_max=50 , lr=1e-5):
    losses = []
    w1, w2, w3, b = initialize_params()    
    N = len(y_data)

    for _ in range(epoch_max):
        for i in range(N):
            x1 = x_data[0][i]
            x2 = x_data[1][i]
            x3 = x_data[2][i]

            y = y_data[i]

            y_hat = predict(x1, x2, x3, w1, w2, w3, b)

            loss = compute_loss_mse(y, y_hat)

            dl_dw1 = compute_gradient_wi(x1, y, y_hat)
            dl_dw2 = compute_gradient_wi(x2, y, y_hat)
            dl_dw3 = compute_gradient_wi(x3, y, y_hat)
            dl_db = compute_gradient_b(y, y_hat)

            w1 = update_weight_wi(w1, dl_dw1, lr)
            w2 = update_weight_wi(w2, dl_dw2, lr)
            w3 = update_weight_wi(w3, dl_dw3, lr)
            b = update_weight_b(b, dl_db, lr)

            losses.append(loss)
    return (w1, w2,  w3, b, losses)


def initialize_params():
    w1, w2, w3, b = (0.016992259082509283,
                     0.0070783670518262355, 0.0070783670518262355, 0)
    return w1, w2, w3, b


def predict(x1, x2, x3, w1, w2, w3, b):
    y_hat = w1 * x1 + w2 * x2 + w3 * x3 + b
    return y_hat


# Predict example
# print(predict(x1=1, x2=1, x3=1, w1=0, w2=0, w3=0, b=0.5))


def compute_loss_mse(y, y_hat):
    loss = (y - y_hat)**2
    return loss


# Compute loss example
# print(compute_loss_mse(y_hat=1, y=0.5))


def compute_gradient_wi(xi, y, y_hat):
    dl_dwi = 2*xi*(y_hat - y)
    return dl_dwi


def compute_gradient_b(y, y_hat):
    dl_db = 2*(y_hat - y)
    return dl_db


# MSE loss
# print(compute_gradient_wi(xi=1, y=1, y_hat=0.5))
# print(compute_gradient_b(y=2, y_hat=0.5))


def update_weight_wi(wi, dl_dwi, lr):
    wi = wi - lr*dl_dwi
    return wi


def update_weight_b(b, dl_db, lr):
    b = b - lr*dl_db
    return b

# print(update_weight_wi(wi=1,dl_dwi=-0.5, lr=1e-5)
# print(update_weight_b(b=0.5, dl_db=-1, lr=1e-5))


(w1, w2, w3, b, losses) = implement_linear_regression(X, y)
plt.plot(losses[:100])
plt.xlabel('iteration')
plt.ylabel('loss')
plt.show()

print(w1, w2, w3)

tv = 19.2
radio = 35.9
newspaper = 51.3

sales = predict(tv, radio, newspaper, w1, w2, w3, b)
print(f'predict salse: {sales}')

