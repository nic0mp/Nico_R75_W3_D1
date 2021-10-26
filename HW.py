# patternName = re.compile(' ([A-Z][a-z][A-Za-z]+)')
# fullName = patternName.findall(data)
# print(fullName)

# print(span, type(fullName))
# print(fullName[span])

# for name in fullName:
#     match = patternName.search(name)
#     print(name)

with open('files/names.txt') as f:
    data = f.readlines()
    
# patternName = re.compile('([A-Z][a-z][a-zA-Za-z][A-Za-z]+)')
patternName = re.compile('([A-Z][a-zA-Za-z]+), ([A-Z][-a-zA-Za-z]+)')

for person in data:
    match = patternName.search(person)
    if match:
        print(f"{match.group(1)} {match.group(2)}")

twitterNames = re.compile('[@a-z]')

for handle in data:
    match2 = twitterNames.search(handle)
    if match:
        print(handle)
    else:
        print("none")




