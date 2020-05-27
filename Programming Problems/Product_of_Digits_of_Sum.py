# Shameen Shetty

'''
    We create a function that takes numbers as arguments, adds them together, and returns
     the product of digits until the answer is only 1 digit long.

    For example, 

    sum_dig_prod(16, 28) ➞ 6
    # 16 + 28 = 44
    # 4 * 4 =  16
    # 1 * 6 = 6

    sum_dig_prod(0) ➞ 0

    sum_dig_prod(1, 2, 3, 4, 5, 6) ➞ 2
'''

# Gets the length of the number, this way we can check if the result
# of our operations is 1 digit or not
def getLen(num):
    return len(str(num))

# If we enter multiple args eg. (2, 3, 4) then we sum those numbers
# or if there is a single arg, we multiply the individual digits of those
# numbers.
# Then we return either the sum or the prod, depending on which operation was done
def get_Sum_or_Prod(*args):
    sum = 0
    prod = 1

    isSum = False

    if len(args) > 1:
        # Since there are more than one arguments entered,
        # we will sum the numbers first
        isSum = True
        for num in args:
            sum += num
    
    elif len(args) == 1:
        # Since there is just one arg that is passed
        # we will first convert that integer into a string,
        # then get all the digits of that number and store it into a list
        # listOfDigits, and then multiply all those digits and store it in prod
        stringNum = str(*args)
        listOfDigits = []
        for digit in stringNum:
            listOfDigits.append(int(digit))

        for digit in listOfDigits:
            prod *= digit

    # A flag, isSum checks if we did a sum or not, this way we can return
    # either the sum or the product.    
    if isSum:
        return sum
    else:
        return prod

'''
    Function: sum_dig_prod
    
    Parameters: 1) *args, which takes in an arbitrary number of arguments
    
    Returns: None

    Description: Our function sum_digits_prod that finds the product of digits until the answer is only 1 digit long
    which we check by first getting the 'first sum' by passing all the arbitrary arguments, then
    we check if the length of firstSum is 1. If it isn't, then we recurively pass it through our
    sum_digits_prod() function until we get a result that is only 1 digit long.
'''
def sum_dig_prod(*args):
    firstSum = get_Sum_or_Prod(*args)
    
    if getLen(firstSum) != 1:
        sum_dig_prod(firstSum)
    else:
        print(f"sum_dig_prod() -> {firstSum}")



if __name__ == "__main__":
    sum_dig_prod(16, 28)
    sum_dig_prod(0)
    sum_dig_prod(1, 2, 3, 4, 5, 6)
