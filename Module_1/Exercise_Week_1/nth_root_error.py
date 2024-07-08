def md_nre(y_true, y_pred, n, p):
    """
    Calculate the Mean Difference of the n-th root Error (MD_nRE).
    """
    num_sample = len(y_true)
    sum_md_nre = 0

    for i in range(num_sample):
        root_y_true = y_true[i] ** (1 / n)
        root_y_pred = y_pred[i] ** (1 / n)
        sum_md_nre += abs(root_y_true - root_y_pred) ** p

    md_nre_value = sum_md_nre / num_sample
    return md_nre_value


def main():
    import math

    num_samples = int(input('Input number of samples: '))

    # Input values of y and y_pred
    y_true = []
    y_pred = []

    for i in range(num_samples):
        y_true.append(float(input(f'Input y_true[{i}]: ')))
        y_pred.append(float(input(f'Input y_pred[{i}]: ')))

    # Input n and p
    n = int(input('Input n: '))
    p = int(input('Input p: '))

    md_nre_value = md_nre(y_true, y_pred, n, p)
    print(f'MD_nRE (n={n}, p={p}: {md_nre_value})')


if __name__ == "__main__":
    main()
