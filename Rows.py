

test_one = "a,b,c,d,e,f,g"
test_two = test_one.split(",")
test_three = [test_one, test_two, test_one]


print(test_one)
print(test_two)
print(test_three)

print("Testing One Example")
for i in test_one:
    print(i)
for i in range(len(test_one)):
    print(i)
