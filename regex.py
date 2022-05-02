import re
string = 'search inside of this text please please'
print('search' in string)
print(re.search('this',string))
a=re.search('this',string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())##returns part of string where there was a match.
##if a is not found in search then output shows error.
pattern=re.compile('please')
##the 'pattern' is captured and can be used everywhere multiple times
b=pattern.findall(string)
print(b)
c=pattern.fullmatch(string)
print(c)
##returns None as it searches matching of full string in pattern which is not possible.
pattern1=re.compile('search inside of this text please please')
d=pattern1.fullmatch(string)
print(d)
e=pattern1.match(string)
##matches 0 or more characters in string return span till it matches
print(e)
##it return span till where it matches in string from pattern 1 or considering pattern1 as hypothesis.
pattern2=re.compile(r"([a-zA-Z]).([a])")
f=pattern2.search(string)
print(f.group())
##in above command searching for 'a' i.e. letter followed by anything followed by 'a' i.e sea is returned as it contains 'a'.
print(f.group(1))
print(f.group(2))
print(f.group(0))#same as f.group()
# at least 1 upper, 1 lower, 1 digit, 1 special char, ends of number and mininum eight char in length
import re
def validate_password(p):
  rxp = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}(\d)$' 
  if re.compile(rxp).fullmatch(p):
    return 'valid'
  else:
    return 'in valid'
password = 'aM*787po+`*1xdfe7'
validate_password(password) #  valid
import re

pattern = re.compile(r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{8,}$')

password = input('Choose a password: ') check = pattern.fullmatch(password)

if len(password) >= 8 and check != None: print('Correct password') else: print('Wrong, try again')