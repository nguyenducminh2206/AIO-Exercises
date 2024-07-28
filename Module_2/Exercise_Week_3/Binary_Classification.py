import numpy as np

data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]


def create_train_data(data):

    return np.array(data)


train_data = create_train_data(data)


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    for i in range(len(y_unique)):
        prior_probability[i] = len(np.nonzero(
            train_data[:, 4] == y_unique[i])[0]) / len(train_data)

    return prior_probability


# Question 1
priority_prob = compute_prior_probability(train_data)
print(f"P(Play Tennis = Yes) = {priority_prob[1]}")
print(f"P(Play Tennis = No) = {priority_prob[0]}")
print()


def compute_likelihood(train_data, feature_index, feature_value, class_label):
    subset = train_data[train_data[:, 4] == class_label]
    likelihood = len(np.nonzero(
        subset[:, feature_index] == feature_value)[0]) / len(subset)

    return likelihood


# Question 2
P_sunny_yes = compute_likelihood(train_data, 0, 'Sunny', 'yes')
P_cool_yes = compute_likelihood(train_data, 1, 'Cool', 'yes')
P_high_yes = compute_likelihood(train_data, 2, 'High', 'yes')
P_true_yes = compute_likelihood(train_data, 3, 'Strong', 'yes')


print(f"P(Sunny|Yes) = {P_sunny_yes}")
print(f"P(Cool|Yes) = {P_cool_yes}")
print(f"P(High|Yes) = {P_high_yes}")
print(f"P(True|Yes) = {P_true_yes}")
print()

P_yes_X = P_sunny_yes * P_cool_yes * \
    P_high_yes * P_true_yes * priority_prob[1]

print(f"P(Yes|X) = {P_yes_X:.4f}")
print()


# Question 3
P_sunny_no = compute_likelihood(train_data, 0, 'Sunny', 'no')
P_cool_no = compute_likelihood(train_data, 1, 'Cool', 'no')
P_high_no = compute_likelihood(train_data, 2, 'High', 'no')
P_true_no = compute_likelihood(train_data, 3, 'Strong', 'no')

print(f"P(Sunny|No) = {P_sunny_no}")
print(f"P(Cool|No) = {P_cool_no}")
print(f"P(High|No) = {P_high_no}")
print(f"P(True|No) = {P_true_no}")
print()

P_no_X = P_sunny_no * P_cool_no * P_high_no * P_true_no * priority_prob[0]

print(f"P(No|X) = {P_no_X:.4f}")
print()
