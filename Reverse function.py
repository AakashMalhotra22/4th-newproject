def reverse_function(num):
    y = (len(num))
    if y == 1:
        print(num)
    elif y ==2:
        print(num[1]+num[0])
    elif y == 3:
        print(num[2]+num[1]+num[0])

(reverse_function(input("Enter a number: ")))


