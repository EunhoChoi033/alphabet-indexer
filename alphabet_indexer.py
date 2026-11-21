AlPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def main():
    word = input("Define word to index: ").lower()

    while word:
        try:
            indexes = [AlPHABET.index(char) + 1 for char in list(word)]
        except:
            print("ERROR: Input contained non-alphabet letters.")
        else:
            print(indexes)
        finally:
            print()
            word = input("Define word to index: ").lower()



if __name__ == "__main__":
    main()
