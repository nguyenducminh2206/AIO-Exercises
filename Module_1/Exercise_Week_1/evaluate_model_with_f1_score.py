def calculate_f1_score(tp=2, fp=3, fn=4):
    # Check if all variables are integers
    if not all(isinstance(i, int) for i in [tp, fp, fn]):
        for name, value in zip(['tp', 'fp', 'fn'], [tp, fp, fn]):
            if not isinstance(value, int):
                print(f'{name} must be int')
        return

    # Check if all variables are greater than zero
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('all variables must be greater than zero')
        return

    # Calculate precision
    precision = tp / (tp + fp)

    # Calculate recall
    recall = tp / (tp + fn)

    # Calculate F1-Score
    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = 2 * (precision * recall) / (precision + recall)

    # Print the results
    print(f'precistion: {precision}')
    print(f'recall: {recall:.2f}')
    print(f'f1-score: {f1_score:.2f}')
