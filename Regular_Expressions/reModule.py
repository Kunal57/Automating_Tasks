import re

# basic regex
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())

# grouping with parentheses
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))
# print(mo.group())

# print(mo.groups())
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

# matching multiple groups with the pipe
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey.')
# print(mo1.group())

# mo2 = heroRegex.search('Tina Fey and Batman.')
# print(mo2.group())

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))

# optional matching with the question mark
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())

# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('My number is 415-555-4242')
# print(mo1.group())

# mo2 = phoneRegex.search('My number is 555-4242')
# print(mo2.group())

# matching zero or more with the star
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())

# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo3.group())

# matching one or more with the plus
# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batwoman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo2.group())

# mo3 = batRegex.search('The Adventures of Batman')
# print(mo3)

# matching specific repetitions with curly brackets
# haRegex = re.compile(r'(Ha){3}')
# mo1 = haRegex.search('HaHaHa')
# print(mo1.group())

# mo2 = haRegex.search('Ha')
# print(mo2)

# greedy and nongreedy matching
# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHaHaHa')
# print(mo1.group())

# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# print(mo2.group())

# the findall() method
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# print(phoneNumRegex.findall('Cell: 414-555-9999 Work: 212-555-0000'))

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has no groups
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# making your own character classes
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))

# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))

# the caret and dollar sign characters
# beginsWithHello = re.compile(r'^Hello')
# print(beginsWithHello.search('Hello world!'))
# print(beginsWithHello.search('He said hello.') == None)

# endsWithNumber = re.compile(r'\d$')
# print(endsWithNumber.search('Your Number is 42'))
# print(endsWithNumber.search('Your number is forty two.') == None)

# wholeStringIsNum = re.compile(r'^\d+$')
# print(wholeStringIsNum.search('1234567890'))
# print(wholeStringIsNum.search('12345xyz67890') == None)
# print(wholeStringIsNum.search('12   34567890') == None)

# the wildcard character
# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# matching everything with Dot-Star
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))

# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

# greedyRegex = re.compile(r'<.*>')
# mo = greedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

# matching newlines with the dot character
# noNewLineRegex = re.compile('.*')
# print(noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# noNewLineRegex = re.compile('.*', re.DOTALL)
# print(noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# case-insensitive matching
# robocop = re.compile(r'robocop', re.I)
# print(robocop.search('Robocop is part man, part machine, all cop.').group())

# print(robocop.search('ROBOCOP protects the innocent').group())

# print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

# substituting strings with the sub() method
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.'))

# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# managing complex regexes
# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))?            # area code
# (\s|-|\.)?                    # separator
# \d{3}                         # first 3 digits
# (\s|-|\.)                     # separator
# \d{4}                         # last 4 digits
# (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
# )''', re.VERBOSE)
