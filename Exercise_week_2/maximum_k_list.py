def is_number(n):
    """
    Check if input is a number and handle negetive numbers.
    """
    if n.startswith('-'):
        return n[1:].isdigit()
    return n.isdigit()


def max_sliding_window(list, k):
    """
    Find maximum values for each window.
    """
    for i in range(len(list) - k + 1):
        sublist = list[i:i+k]
        max_values = max(sublist)
        print(f'Max value for window {sublist}: {max_values}')


def main():
    list_input = []

    sliding_window = input('Enter the size of sliding window: ')
    # Stop the program if the size of the input is not an integer.
    if not is_number(sliding_window):
        print('Error! Size of the sliding window must be an integer.')
        return
    sliding_window = int(sliding_window)

    while True:
        num_input = input('Enter a number: ')
        # Stop the loop by entering a space.
        if num_input == '':
            break
        # Stop the program if input is not an integer.
        elif not is_number(num_input):
            print('Error! Input must be an integer.')
            return

        list_input.append(int(num_input))

    max_sliding_window(list_input, sliding_window)


if __name__ == "__main__":
    main()
