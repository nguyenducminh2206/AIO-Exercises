import os


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


def main():
    file_name = input('Enter file name: ')
    # Get the absolute path of the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the absolute path to the file
    file_path = os.path.join(current_dir, file_name)

    # Verify if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    # If the file exists, proceed with word counting
    word_dict = word_count(file_path)

    for word, count in sorted(word_dict.items()):
        print(f'{word}: {count}')


if __name__ == "__main__":
    main()
