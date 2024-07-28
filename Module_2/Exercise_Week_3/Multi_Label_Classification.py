import numpy as np

data = [
    ["Weekday", "Spring", "None", "None", "On Time"],
    ["Weekday", "Winter", "None", "Slight", "On Time"],
    ["Weekday", "Winter", "None", "None", "On Time"],
    ["Holiday", "Winter", "High", "Slight", "Late"],
    ["Saturday", "Summer", "Normal", "None", "On Time"],
    ["Weekday", "Autumn", "Normal", "None", "Very Late"],
    ["Holiday", "Summer", "High", "Slight", "On Time"],
    ["Sunday", "Summer", "Normal", "None", "On Time"],
    ["Weekday", "Winter", "High", "Heavy", "Very Late"],
    ["Weekday", "Summer", "None", "Slight", "On Time"],
    ["Saturday", "Spring", "High", "Heavy", "Cancelled"],
    ["Weekday", "Summer", "High", "Slight", "On Time"],
    ["Weekday", "Winter", "Normal", "None", "Late"],
    ["Weekday", "Summer", "High", "None", "On Time"],
    ["Weekday", "Winter", "Normal", "Heavy", "Very Late"],
    ["Saturday", "Autumn", "High", "Slight", "On Time"],
    ["Weekday", "Autumn", "None", "Heavy", "On Time"],
    ["Holiday", "Spring", "Normal", "Slight", "On Time"],
    ["Weekday", "Spring", "Normal", "None", "On Time"],
    ["Weekday", "Spring", "Normal", "Heavy", "On Time"]
]

dict_class = {}


def create_train_data(data):

    return np.array(data)


train_data = create_train_data(data)


def compute_prior_probability(train_data):
    y_unique = ['On Time', 'Late', 'Very Late', 'Cancelled']
    prior_probability = np.zeros(len(y_unique))
    for i in range(len(y_unique)):
        prior_probability[i] = len(np.nonzero(
            train_data[:, 4] == y_unique[i])[0]) / len(train_data)

    return prior_probability


priority_prob = compute_prior_probability(train_data)

# Question 5
print(f"P(On Time) = {priority_prob[0]}")
print(f"P(Late) = {priority_prob[1]}")
print(f"P(Very Late) = {priority_prob[2]}")
print(f"P(Cancelled) = {priority_prob[3]}")
print()


def compute_likelihood(train_data, feature_index, feature_value, class_label):
    subset = train_data[train_data[:, 4] == class_label]
    likelihood = len(np.nonzero(
        subset[:, feature_index] == feature_value)[0]) / len(subset)

    return likelihood


# Question 6
P_weekday_ontime = compute_likelihood(train_data, 0, 'Weekday', 'On Time')
P_winter_ontime = compute_likelihood(train_data, 1, 'Winter', 'On Time')
P_high_ontime = compute_likelihood(train_data, 2, 'High', 'On Time')
P_heavy_ontime = compute_likelihood(train_data, 3, 'Heavy', 'On Time')


print(f"P(Weekday|On Time) = {P_weekday_ontime}")
print(f"P(Winter|On Time) = {P_winter_ontime}")
print(f"P(High|On Time) = {P_high_ontime}")
print(f"P(Heavy|On Time) = {P_heavy_ontime}")
print()

P_ontime_X = P_weekday_ontime * P_winter_ontime * \
    P_high_ontime * P_heavy_ontime * priority_prob[0]

dict_class["On Time"] = P_ontime_X

print(f"P(On Time|X) = {P_ontime_X:.4f}")
print()


# Question 7
P_weekday_late = compute_likelihood(train_data, 0, 'Weekday', 'Late')
P_winter_late = compute_likelihood(train_data, 1, 'Winter', 'Late')
P_high_late = compute_likelihood(train_data, 2, 'High', 'Late')
P_heavy_late = compute_likelihood(train_data, 3, 'Heavy', 'Late')


print(f"P(Weekday|Late) = {P_weekday_late}")
print(f"P(Winter|Late) = {P_winter_late}")
print(f"P(High|Late) = {P_high_late}")
print(f"P(Heavy|Late) = {P_heavy_late}")
print()

P_late_X = P_weekday_late * P_winter_late * \
    P_high_late * P_heavy_late * priority_prob[1]

dict_class["Late"] = P_late_X

print(f"P(Late|X) = {P_late_X:.4f}")
print()

# Question 8
P_weekday_very_late = compute_likelihood(train_data, 0, 'Weekday', 'Very Late')
P_winter_very_late = compute_likelihood(train_data, 1, 'Winter', 'Very Late')
P_high_very_late = compute_likelihood(train_data, 2, 'High', 'Very Late')
P_heavy_very_late = compute_likelihood(train_data, 3, 'Heavy', 'Very Late')


print(f"P(Weekday|Very Late) = {P_weekday_very_late}")
print(f"P(Winter|Very Late) = {P_winter_very_late}")
print(f"P(High|Very Late) = {P_high_very_late}")
print(f"P(Heavy|Very Late) = {P_heavy_very_late}")
print()

P_very_late_X = P_weekday_very_late * P_winter_very_late * \
    P_high_very_late * P_heavy_very_late * priority_prob[2]

dict_class["Very Late"] = P_very_late_X

print(f"P(Very Late|X) = {P_very_late_X:.4f}")
print()

# Question 9
P_weekday_cancelled = compute_likelihood(train_data, 0, 'Weekday', 'Cancelled')
P_winter_cancelled = compute_likelihood(train_data, 1, 'Winter', 'Cancelled')
P_high_cancelled = compute_likelihood(train_data, 2, 'High', 'Cancelled')
P_heavy_cancelled = compute_likelihood(train_data, 3, 'Heavy', 'Cancelled')


print(f"P(Weekday|Cancelled) = {P_weekday_cancelled}")
print(f"P(Winter|Cancelled) = {P_winter_cancelled}")
print(f"P(High|Cancelled) = {P_high_cancelled}")
print(f"P(Heavy|Cancelled) = {P_heavy_cancelled}")
print()

P_cancelled_X = P_weekday_cancelled * P_winter_cancelled * \
    P_high_cancelled * P_heavy_cancelled * priority_prob[3]

dict_class["Cancelled"] = P_cancelled_X

print(f"P(Cancelled|X) = {P_cancelled_X:.4f}")
print()


def predict_class(class_dict):
    return max(class_dict)


# Question 10
print(f"Predicted class for event X: {predict_class(dict_class)}")
print()
