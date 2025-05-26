import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    from stats import get_word_count
    get_word_count(filename)
main()