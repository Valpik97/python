dict = {
    'a': 'b',
    'c': 'd'
}

string = '{\n'
for key in dict:
    string += '    \'{}\': \'{}\',\n'.format("key", "dict[key]", "dafd")
string += '}'
print(string)-*