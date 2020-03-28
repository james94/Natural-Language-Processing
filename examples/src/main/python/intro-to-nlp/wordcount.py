"""Count words."""

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return

    text_list = []

    # Convert text string to lowercase
    if text.islower() != True:
        text = text.lower()

    # print("text = ", text)
    # print()

    # Remove punctuations and symbols from text string
    punctuations = ".!@#&()-[{}]:;',?/*"
    symbols = "`~$^+=<>"
    for ch in punctuations:
        text = text.replace(ch, "")

    for ch in symbols:
        text = text.replace(ch, "")

    # print("text = ", text)
    # print()

    # Convert string to list, Split text into words
    text_list = list(text.split(" "))

    # print(text_list)

    # Aggregate word counts using a dictionary
    for word in text_list:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()