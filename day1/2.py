data = open("1_data.txt", "r")
#data = open("2_test_data.txt", "r")
sum = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
first_digit_flag = False
first_digit = 0
first_digit_pos = 0
last_digit = 0
last_digit_pos = 0

for line in data:
    for idx, char in enumerate(line):
        if(char.isdigit()):
            if(first_digit_flag == False):
                first_digit = int(char)
                first_digit_pos = idx
                last_digit = int(char)
                last_digit_pos = idx
                first_digit_flag = True
            else:
                last_digit = int(char)
                last_digit_pos = idx
    for idx, digit in enumerate(digits):
        digit_pos = line.find(digit)
        rdigit_pos = line.rfind(digit)
        if( digit_pos > -1 and digit_pos < first_digit_pos ):
            first_digit = idx + 1
            first_digit_pos = digit_pos
        if digit_pos > last_digit_pos:
            last_digit = idx + 1
            last_digit_pos = digit_pos
        # this last condition tripped me up for awhile
        if rdigit_pos > last_digit_pos:
            last_digit = idx + 1
            last_digit_pos = rdigit_pos

    first_digit_flag = False
    first_digit_pos = 100000000
    last_digit_pos = -1
    combined_digits = int( str(first_digit) + str(last_digit) )
    sum += combined_digits

print( sum )