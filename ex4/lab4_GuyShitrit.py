# Assignment: 4
# Author: Guy Shitrit, ID: 330707761


def Q1(n1, n2):
    if (n1 + n2) % 2 == 0:
        return n1

    return n2

def Q2(num):
    if not (10000 <= num <= 99999):
        print("Number is not 5-digits")
        return -1

    ones = num % 10
    tens = (num // 10) % 10
    hundreds = (num // 100) % 10
    thousands = (num // 1000) % 10
    ten_thousands = num // 10000

    reversed_num = ones * 10000 + tens * 1000 + hundreds * 100 + thousands * 10 + ten_thousands
    summ = ones + tens + hundreds + thousands + ten_thousands

    if num == reversed_num:
        return summ

    return reversed_num



def Q3(n1, n2, n3):
    if (n1 < n2 < n3):
        print("ascending")
    elif (n3 < n2 < n1):
        print("descending")
    else:
        print("not sorted")


def Q4(x, y, z):
    if x < 0 or y < 0 or z < 0:
        print("Lengths must be positive.")
        return False

    if x > y + z or y > x + z or z > x + y:
        print("Lengths must be smaller than the sum of the other two lengths in a triangle.")
        return False

    return True



def Q5(num):
    if 10 <= num <= 99: # 2 ספרות
        return (num // 10) - (num % 10)

    elif 100 <= num <= 999: # 3 ספרות
        ones = num % 10
        tens = num // 10 % 10
        hundreds = num // 100

        if (ones > tens and ones > hundreds): return ones
        elif (tens > ones and tens > hundreds): return tens
        elif (hundreds > ones and hundreds > tens): return hundreds

    elif 1000 <= num <= 9999: # 4 ספרות
        ones = num % 10
        tens = num // 10 % 10
        hundreds = num // 100 % 10
        thousands = num // 1000

        reversedNum = ones * 1000 + tens * 100 + hundreds * 10 + thousands

        if num == reversedNum:
            return True

        return False

    elif 10000 <= num <= 99999: # 5 ספרות
        pass # לעשות אחר כך



    else:
        return "input error"


def Q6(num1, num2):
    if not ((100 <= num1 <= 999) and (100 <= num2 <= 999)):
        print("The numbers must be 3-digits.")
        return -1

    ones1 = num1 % 10
    ones2 = num2 % 10

    tens1 = (num1 // 10) % 10
    tens2 = (num2 // 10) % 10
    


def Q7(num):
    if not (10000 <= num <= 99999):
        print("Number is not 5-digits.")
        return -1

    LENGTH = 5 # המספר חייב להיות 5 ספרות

    odd_count = 0
    even_count = 0

    ones = num % 10
    tens = (num // 10) % 10
    hundreds = (num // 100) % 10
    thousands = (num // 1000) % 10
    ten_thousands = num // 10000

    if ones % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if tens % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if hundreds % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if thousands % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if ten_thousands % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


    if even_count == LENGTH:
        print("only even digits")
    elif odd_count == LENGTH:
        print("not even digits")
    else:
        print(even_count + ", " + odd_count)



if __name__ == "__main__":
    pass
