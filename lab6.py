def encode(data_string):
    ReturnData = ""

    for index in data_string:
        if i < 7:
            ReturnData = ReturnData + str(i) + 3
        else:
            if i == 7:
                i = 0
                ReturnData = ReturnData + str(i)
            elif i == 8:
                i = 1
                ReturnData = ReturnData + str(i)
            elif i == 9:
                i = 2
                ReturnData = ReturnData + str(i)

    return ReturnData

def decode(phrase):
    #result string with a foreloop, run through each element of the string and then convert to a number, and then convert
    phrase = input('Enter a phrase to decode:')
    phrase_list = phrase.split()
    for i in range(0, len(phrase_list)):
        phrase_list[i] = int(phrase_list[i])
    for i in range(0, len(phrase_list)):
        phrase_decode_list = []
        phrase_decode_list.append(phrase_list[i] - 3)
    for i in range(0, len(phrase_decode_list)):
        phrase_decode_list[i] = str(phrase_decode_list[i])
        phrase_joined_list = ''.join(phrase_decode_list)


        return phrase_joined_list

def main():
    # looping menu
    option = '1'
    phrase = ''
    while option != '0':
        # print menu
        print('0. Exit')
        print('1. Enter a new phrase')
        print('2. Print encoded phrase')
        print('3. Print decoded phrase')
        option = input('Enter an option: ')

        if option == '1':
            phrase = input('Enter your phrase: ')
        elif option == '2':
            print('Encoded phrase is', encode(phrase))
        elif option == '3':
            print('Decoded phrase is', decode(phrase))


if __name__ == "__main__":
    main()