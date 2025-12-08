num1 = float(eval(input("Enter first number")))
opt = str(input("Enter the operation"))
num2 = float(eval(input("Enter second number")))
fTotal = ""
r = ""
funName = "add" if opt == "+" else (
    "sub" if opt == "-" else ("mul" if opt == "*" else ("div" if opt == "/" else "Wrong OPT")))

if funName == "Wrong OPT":
    print("Invalid Operation")
    
elif funName == "add":
    # def add(num1 = "",num2 = ""):
    total = num1 + num2
    fTotal = total

elif funName == "sub":
    # def sub(num1 = "",num2 = ""):
    num1DeciList = str(num1).split(".")
    num2DeciList = str(num2).split(".")
    decL = decR = ""
    if num1DeciList[1] < num2DeciList[1]:
        decR = (100 + int(num1DeciList[1])) + (~int(num2DeciList[1])) + 1
        num1DeciList[0] = int(num1DeciList[0]) - 1

    decL = int(num1DeciList[0]) + (~int(num2DeciList[0])) + 1
    total = float(decL) + float("0." + str(decR))
    fTotal = total

elif funName == "mul":
    # def mul(num1 = "",num2 = ""):
    count = 0
    if "-" in str(num1):
        count = count + 1
        num1 = (str(num1)[1::])
    if "-" in str(num2):
        count = count + 1
        num2 = (str(num2)[1::])

    num1DeciList = str(num1).split(".")
    num2DeciList = str(num2).split(".")
    decLen = len(num1DeciList[1] + num2DeciList[1])
    if int(num1DeciList[1]) > 0 or int(num2DeciList[1]) > 0:
        num1 = int(num1DeciList[0] + num1DeciList[1])
        num2 = int(num2DeciList[0] + num2DeciList[1])
    else:
        num1 = num1
        num2 = num2

    total = 0
    counter = 1
    while counter <= num2:
        total += num1
        counter += 1

    sign = "+" if count % 2 == 0 else "-"
    if int(num1DeciList[1]) > 0 or int(num2DeciList[1]) > 0:
        fTotal = float(sign + (str(total)[:len(str(total)) - decLen]) + "." + (str(total)[-1:-(decLen + 1):-1])[::-1])
    else:
        fTotal = float(sign + (str(total)))

elif funName == "div":
    # def div(num1 = "",num2 = ""):
    count = 0
    zeroCount = decUnitFix = ""
    if "-" in str(num1):
        count = count + 1
        num1 = (str(num1)[1::])

    if "-" in str(num2):
        count = count + 1
        num2 = (str(num2)[1::])

    num1DeciList = str(num1).split(".")
    num2DeciList = str(num2).split(".")
    decLen = len(num1DeciList[1] + num2DeciList[1])
    num1decLen = len(num1DeciList[1])
    num2decLen = len(num2DeciList[1])
    if int(num1DeciList[1]) >= 0 or int(num2DeciList[1]) >= 0:
        num1 = int(num1DeciList[0] + num1DeciList[1] + "".zfill(num2decLen))
        num2 = int(num2DeciList[0] + num2DeciList[1] + "".zfill(num1decLen))

    total = num1
    rem = counter = remCounter = 0
    print(total)
    print(num2)
    while total >= num2:
        total = total + (~num2) + 1
        counter += 1
        rem = total
    print(total)
    decUnitFix = len(str(num2))-len(str(total))
    rem = float(str(rem) + "".zfill(decLen))

    while rem >= num2:
        rem = rem + (~num2) + 1
        remCounter += 1

    sign = "+" if count % 2 == 0 else "-"
    fTotal = float(sign + (str(counter) + "." + "".zfill(decUnitFix) + str(remCounter)))

print(counter)
print(remCounter)
# fTotal = funName(num1,num2)
print(fTotal)