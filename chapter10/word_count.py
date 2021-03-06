def count_words(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry the file {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} as {num_words} words.")

filename = 'alice.txt'
count_words(filename)