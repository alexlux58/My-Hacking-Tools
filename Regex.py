import re

text_to_search = '''
abcderfghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacter (Need to be escaped):
.^$*?{}[]\|()

coreyms.com

321-555-4321
123.555.1234

Mr.Schafer
Mr Smith
Ms Davis
Mrs. Robinson'''

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r'\bHa')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
print(text_to_search[1:4])