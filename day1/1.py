data = open("1_data.txt", "r")
sum = 0

first_digit_flag = False
first_digit = 0
last_digit = 0

for line in data:
    for char in line:
        if(char.isdigit()):
            if(first_digit_flag == False):
                first_digit = int(char)
                last_digit = int(char)
                first_digit_flag = True
            else:
                last_digit = int(char)
    first_digit_flag = False
    combined_digits = int( str(first_digit) + str(last_digit) )
    sum += combined_digits

print( sum )