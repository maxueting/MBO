f = open('C:/Users/wb.maxueting/Desktop/123.txt', 'r')
str = f.read()
str_list = str.split()
for id in str_list:
    print("'"+id+"'"+",")