import sys #It lets us access system-specific parameters and functions.


def get_data_list(data, i, length):
    if i == length:
        result.append(''.join(data) )
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            get_data_list(data, i + 1, length)
            data[i], data[j] = data[j], data[i] 


n = len(sys.argv) #count the number of arguments
print("Total arguments passed:", n)
if(n != 2):
    print("enter vaild command")
else:    
    print("\nName of Python script:", sys.argv[0])
    print("\nName of text file name:", sys.argv[1])
    file_name = sys.argv[1]#is automatically a list of strings representing the arguments (as separated by spaces) on the command-line. 

    try:
        with open(file_name) as f: #open() function to open a file.
            str_input = f.readlines() #takes a text file as input and stores each line in the file as a separate element in a list
        print(str_input)
        # str_input = "abc"
        test = str_input[0].split() #breaks up a string at the specified separator and returns a list of strings.
        print(test)
        print("------------")
        result = []
        for x in test:
            sort_data = sorted(x)
            print(sort_data)
            get_data_list(list(sort_data), 0, len(sort_data))
            #print(result)
            for data_sort in result:
                print(data_sort,end='')
                print(',',end='')
            print('')
            result = []

    except FileNotFoundError:
        print("enter valid file name")
    except IndexError:
        print("No data in file")

    







# str_input = input("enter the string:")#"hat abc Zu6 T AA"




