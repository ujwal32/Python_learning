# str – Text: "Hello" always denoted inside ""

# str1="hello"
# str2="world"
# result=str1 + str2
# print(result)

# repeat="hello"*3
# print(repeat)

# print(str1[0])
# print(str1[-1])

# text= "hello world"
# print(text[0:5])

# print(text[:5])

# print(text[:6])

# print(text[::2])

# print(text[::-1])

# txt="python" is text
# print("python" is text)

# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# name="       python             "
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())

# txt="i love india"
# txt1=txt.replace("india","nepal")
# print(txt1)
 
txt="nepal, india , uk ,usa, canada"
t=txt.split(",")
print(t)

joined_text="-".join(txt)
print(joined_text)

print(txt.find("uk"))


name="ujwal"
age=25

hey="My name is {} and my age is {}".format(name,age)
print(hey)