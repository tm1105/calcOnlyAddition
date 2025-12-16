def deciSplit(num=None):
    if num is not None:
        return str(num).split(".")
    else:
        return False


def mathOp(nums=None, opEx=None):
    if nums is not None and opEx is not None:
        num1 = float(nums[0])
        num2 = float(nums[1])
        opEx = opEx[0]

        if opEx == "+":
            total = num1 + num2
            fTotal = total
            # Addition Logic :: End

        # Substraction Logic :: Start
        elif opEx == "-":
            num1DeciList = deciSplit(num1)  # Number1 Splitup into whole and decimal
            num2DeciList = deciSplit(num2)  # Number1 Splitup into whole and decimal
            decL = decR = ""
            if len(num1DeciList[1]) > len(num2DeciList[1]):
                num2DeciList[1] = int(str(num2DeciList[1])+"".zfill(len(num1DeciList[1])-len(num2DeciList[1])))
            elif len(num1DeciList[1]) < len(num2DeciList[1]):
                num1DeciList[1] = int(str(num1DeciList[1]) + "".zfill(len(num2DeciList[1]) - len(num1DeciList[1])))

            if int(num1DeciList[1]) < int(num2DeciList[1]):  # Decimal Subs logic
                decR = (int("1"+"".zfill(len(num1DeciList[1]))) + int(num1DeciList[1])) + (~int(num2DeciList[1])) + 1
                num1DeciList[0] = int(num1DeciList[0]) - 1  # Right Shift operation logic
            elif int(num1DeciList[1]) >= int(num2DeciList[1]):
                decR = (int(num1DeciList[1])) + (~int(num2DeciList[1])) + 1

            decL = int(num1DeciList[0]) + (~int(num2DeciList[0])) + 1
            total = float(decL) + float("0." + str(decR))  # Combining both Unit and Decimal
            fTotal = total
        # Substraction Logic :: End

        # Multiplication Logic :: Start
        elif opEx == "*":
            count = 0
            if "-" in str(num1):  # Negitive Check and Sign removal
                count = count + 1
                num1 = (str(num1)[1::])
            if "-" in str(num2):  # Negitive Check and Sign removal
                count = count + 1
                num2 = (str(num2)[1::])

            sign = "+" if count % 2 == 0 else "-"  # Final Sign assignment

            num1DeciList = deciSplit(num1)  # Number1 Splitup into whole and decimal
            num2DeciList = deciSplit(num2)  # Number1 Splitup into whole and decimal
            decLen = len(num1DeciList[1] + num2DeciList[1])  # adding lengths of both decimal parts
            if int(num1DeciList[1]) > 0 or int(num2DeciList[1]) > 0:  # checking if values are greater then 0
                num1 = int(num1DeciList[0] + num1DeciList[1])  # concatenating values of both parts of the number 1
                num2 = int(num2DeciList[0] + num2DeciList[1])  # concatenating values of both parts of the number 2
            else:
                num1 = num1  # otherwise as it is(no a decimal number)
                num2 = num2  # otherwise as it is(no a decimal number)

            total = 0  # assigning total as zero
            counter = 1  # counter value set as 1 for multiplication
            while counter <= num2:  # initializing while loop for multiply
                total += num1  # adding num1 num2 times
                counter += 1  # updating value for num2 times

            if int(num1DeciList[1]) > 0 or int(
                    num2DeciList[1]) > 0:  # checking if botht the numbers are decimal numbers
                fTotal = float(sign + (str(total)[:len(str(total)) - decLen]) + "." + (str(total)[-1:-(decLen + 1):-1])[
                    ::-1])  # Decimal (.) assignment
            else:
                fTotal = float(sign + (str(total)))  # multiplication logic
        # Multiplication Logic :: END

        # Division Logic :: Start
        elif opEx == "/":  # division logic start
            count = 0  # counter value set as 0 to check till what time we need to do repeatative subtraction using addition
            zeroCount = decUnitFix = ""  # defining variable
            if "-" in str(num1):  # counting and removing -ve sign
                count = count + 1  # updating counter value
                num1 = (str(num1)[1::])  # removing sign

            if "-" in str(num2):  # counting and removing -ve sign from number 2
                count = count + 1  # updating counter value
                num2 = (str(num2)[1::])  # removing sign

            sign = "+" if count % 2 == 0 else "-"  # re-assigning sign

            num1DeciList = deciSplit(num1)  # spliting the number from decimal and storing it in the list
            num2DeciList = deciSplit(num2)  # spliting the number from decimal and storing it in the list
            decLen = len(num1DeciList[1] + num2DeciList[1])  # storing length of both the number's decimal part
            num1decLen = len(num1DeciList[1])  # calculating and storing length of decimal part of number1
            num2decLen = len(num2DeciList[1])  # calculating and storing length of decimal part of number2
            if int(num1DeciList[1]) >= 0 or int(
                    num2DeciList[1]) >= 0:  # if decimal length of both the numbers is greater then 0
                num1 = int(num1DeciList[0] + num1DeciList[1] + "".zfill(
                    num2decLen))  # adding zeros at the end according to decimal length
                num2 = int(num2DeciList[0] + num2DeciList[1] + "".zfill(
                    num1decLen))  # adding zeros at the end according to decimal length

            total = num1  # assigning total as number 1 to store as a temporary variable
            rem = counter = remCounter = 0  # defining variable

            while total >= num2:  # checking if total is greater than the divisor
                total = total + (~num2) + 1  # repeatative substraction
                counter += 1  # incrementing counter
                rem = total  # storing the remainder

            decUnitFix = len(str(num2)) - len(str(total)) if len(str(num2)) - len(
                str(total)) > 0 else 0  # fixing decimal's unit place
            rem = float(str(rem) + "".zfill(decLen))  # storing remainder

            while rem >= num2:  # to divide checking reminder
                rem = rem + (~num2) + 1  # repeatative substraction
                remCounter += 1  # updating counter variable

            fTotal = float(
                sign + (str(counter) + "." + "".zfill(decUnitFix) + str(remCounter)))  # division final assignment
        # Division Logic :: End
        print(fTotal)


def getNumAndOp(inp=None):
    if inp != None:
        import re
        regex = r'(?<=\d)[^\d.]'
        numList = [numbers for numbers in re.split(regex, inp) if numbers != '']
        opList = re.search(regex, inp).group()
        if numList is not None and opList is not None:
            mathOp(numList, opList)
    else:
        return "Please enter correct mathematical expression"

userInput = input("Enter mathematical expression")

getNumAndOp(userInput)