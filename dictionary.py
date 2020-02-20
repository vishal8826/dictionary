import json
from difflib import get_close_matches
data = json.load(open('data.json'))

def translate(w):
    if w.lower() in data:
        return data[w.lower()]

    elif w.title() in data:
        return data[w.title()]
    
    elif w.upper() in data:
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
        print('Did you mean %s instead ?'% get_close_matches(w, data.keys())[0])
        
        choice = input('Y or N\n')

        if choice == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "We didn't understand your query."

    else:
        return "This word doesn't exist. Please double check it."

word = input('Enter the word: ')
o = translate(word)
if isinstance(o, list):
    for i in o:
        print(i)
else:
    print(o)
