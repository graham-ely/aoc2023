# from my start of 7
data = open("11_test_data.txt", "r")
#data = open("11_data.txt", "r")

#vars outside loop
sum = 0

for line in data:
    #iteration through lines
    items = data.split()
    for idx, item in enumerate(items):
        #iteration through line if needed
        print(idx)
    #iterate vars oustside loop
    #clear flags

print( sum )