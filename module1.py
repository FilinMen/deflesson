list_1 = ["hello"]

def list(x):
    list_1.append(x) 
    return list_1

def main():
    text = (input("введите слово"))
    text_app = list(text)
    print("полученный список ", text_app)

if __name__ == '__main__':
    main()