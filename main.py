from stats import count_words, count_chararcters, sort_characters
import sys

def main():
    total_words = count_words(args)
    total_characters = count_chararcters(args)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_characters(total_characters)
    for i in sorted_characters:
        if i["char"].isalpha() != False:
            print(f"{i["char"]}: {i["count"]}")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    args = sys.argv[1]

main()
