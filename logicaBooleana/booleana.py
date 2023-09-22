# if test_expression:
# statement(s) to be run
# else:
# statement(s) to be run

a = 16
b = 25
if a >= b:
    print(a)
else:
    print(b)

# if test_expression:
# statement(s) to be run
# elif test_expression:
# statement(s) to be run

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")


c = 27
if a > b:
    if b > c:
        print("a is greater than b and b is greater than c")
    else:
        print("a is greater than b and less than c")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")


# Or And

d = 23
e = 34
if d == 34 or e == 34:
    print(d + e)


if d == 34 and e == 34:
    print(d + e)

teste = 1

if teste == True:
    print("true")
else:
    print("false")
