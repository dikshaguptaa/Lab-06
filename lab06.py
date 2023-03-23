def string_to_data(data_string):
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

print("Menu")
print("-------------")
print("1. Encode")
print("2. Decode")
print("3. Quit")

userabc = input("passcode: ").split()
print(string_to_data(userabc))