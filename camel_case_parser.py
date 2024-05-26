from collections import defaultdict
import json
from string import printable

class CamelCaseParser():
    # Read Word List
    with open('words.txt', 'r') as f:
        __words__ = f.read().split('\n')
    # Init Word Dict
    __en_dict__ = defaultdict(lambda : defaultdict(list))
    # Populate Word Dict
    for w in __words__:
            __en_dict__[len(w)][w[0]].append(w)
    __en_dict__ = dict(sorted(__en_dict__.items(), reverse=True))
    # Update Dictionary JSON
    with open('words.json', 'w') as f:
        json.dump(__en_dict__, f, indent=4)

    __alnums__ = [i for i in printable if i.isalnum() and not i.isupper()]
    def __init__(self):
        self.camel_list = []

    def parse_camel_case(self, *strings:str):
        for non_delim_string in strings:
            self.camel_list = []
            nds = non_delim_string
            norm_string = ''
            for l in non_delim_string.lower():
                if l not in self.__alnums__:
                    non_delim_string = non_delim_string.replace(l, "") 
            norm_string = non_delim_string.lower()

            reps = len(norm_string)
            i = reps
            count = len(nds)
            while i in range(reps, 0, -1):
                count+=1
                if len(norm_string[-i:]) in self.__en_dict__.keys():
                    if norm_string[-i:].isdecimal():
                        self.camel_list.append(norm_string[-i:])
                        norm_string = norm_string[:-i]
                        i = len(norm_string)
                    elif norm_string[-i:] in self.__en_dict__[len(norm_string[-i:])][norm_string[-i]]:
                        self.camel_list.append(norm_string[-i:].capitalize())
                        norm_string = norm_string[:-i]
                        i = len(norm_string)
                    else:
                        i -= 1
                else:
                    i -= 1

            self.camel_list.reverse()
            self.camel_list[0] = self.camel_list[0].lower()
            yield ''.join(self.camel_list)

