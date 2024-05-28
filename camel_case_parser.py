from collections import defaultdict
import json
from string import printable
class CamelCaseParser():
    """String formatter for different commmon programming cases.

    Yields:
        string: String with symbols removed.
    """
    ### init Resources
    # Initialize valid character list
    __alnums__ = [i for i in printable \
                  if i.isalnum() \
                    and not i.isupper()]
    # Init Word Dicts. w_dict is read from a 
    # txt document and is for user
    # updates to the word list. en_dict is read 
    # from JSON and is used by the
    # script. en_dict is updated from the w_dict.
    __en_dict__ = defaultdict(lambda : defaultdict(list))
    __w_dict__ = defaultdict(lambda : defaultdict(list))
    # Read Words JSON and populate en_dict
    with open('words.json', 'r') as f:
       __en_dict__ = json.load(f)
    # Read Word List and populate w_dict
    with open('words.txt', 'r') as f:
        for w in f.read().split('\n'):
                __w_dict__[str(len(w))][w[0]].append(w)
    __w_dict__ = dict(sorted(__w_dict__.items(), reverse=True))
    # Check that both lists are equal
    # Update en_dict from w_dict (this is for user ease)
    try:
        if not __w_dict__ == __en_dict__:
            raise AssertionError(f"en_dict was \
                    {'' if __w_dict__ == __en_dict__ else 'not'} \
                        equal to w_dict")
    except AssertionError as e:
        __en_dict__ |= __w_dict__
        with open('words.json', 'w') as f:
            json.dump(__en_dict__, f, indent=4)

    def __init__(self):
        """Constructor, set's obj level properties.
        """
        self.parse_list = []
        self.formats = {
            'lowercase': self.lower_case,
            'camelCase': self.camel_case,
            'PascalCase': self.pascal_case,
            'UPPERCASE': self.upper_case,
            'snake_case': self.snake_case,
            'camel_Snake_Case': self.camel_snake_case,
            'Pascal_Snake_Case': self.pascal_snake_case,
            'UPPER_SNAKE_CASE': self.upper_snake_case,
            'kebab-case': self.kebab_case,
            'camel-Kebab-Case': self.camel_kebab_case,
            'Pascal-Kebab-Case': self.pascal_kebab_case,
            'UPPER-KEBAB-CASE': self.upper_kebab_case,
            'dotted.case': self.dotted_case,
            'camel-Dotted-Case': self.camel_dotted_case,
            'Pascal-Dotted-Case': self.pascal_dotted_case,
            'UPPER-DOTTED-CASE': self.upper_dotted_case,
        }

    def vowel_drop_helper(self, word:str):
        """Converts parsed word to vwldrpcs string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: vwldrpcs string
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        for w in word:
            if w in vowels:
                word = word.replace(w, '')
        return word
    
    def create_case(self, words, sep='', case='camel', start=0, stop=-1, step=1):
        

    def lower_case(self, parse_l:list[str], drop_vowels=False):
        """Converts parsed word list to flatcase string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: flatcase string
        """
        return self.vowel_drop_helper(''.join(parse_l)) \
            if drop_vowels else ''.join(parse_l)
    
    def camel_case(self, parse_l:list[str]):
        """Converts parsed word list to a camelCase string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: camelCase string
        """
        parse_l[1:] = [w.capitalize() for w in parse_l[1:]]
        return ''.join(parse_l)
    
    def pascal_case(self, parse_l:list[str]):
        """Converts parsed word list to a PascalCase string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: PascalCase string
        """
        parse_l = [w.capitalize() for w in parse_l]
        return ''.join(parse_l)
    
    def upper_case(self, parse_l:list[str]):
        """Converts parsed word list to a UPPERCASE string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: UPPERCASE string
        """
        parse_l = [w.upper() for w in parse_l]
        return ''.join(parse_l)
    
    def vowel_drop_snake_case(self, parse_l:list[str]):
        """Converts parsed word list to vwl_drp_snk_cs string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: vwl_drp_snk_cs string
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        parse_l = '_'.join(parse_l)
        parse_l = [w for w in parse_l if w not in vowels]
        return ''.join(parse_l)
    
    def snake_case(self, parse_l:list[str]):
        """Converts parsed word list to a snake_case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: snake_case string
        """
        return '_'.join(parse_l)
    
    def camel_snake_case(self, parse_l:list[str]):
        """Converts parsed word list to a camel_Snake_Case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: camel_Snake_Case string
        """
        parse_l[1:] = [w.capitalize() for w in parse_l[1:]]
        return '_'.join(parse_l)
    
    def pascal_snake_case(self, parse_l:list[str]):
        """Converts parsed word list to a Pascal_Snake_Case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: Pascal_Snake_Case string
        """
        parse_l = [w.capitalize() for w in parse_l]
        return '_'.join(parse_l)
    
    def upper_snake_case(self, parse_l:list[str]):
        """Converts parsed word list to an UPPER_SNAKE_CASE string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: UPPER_SNAKE_CASE string
        """
        parse_l = [w.upper() for w in parse_l]
        return '_'.join(parse_l)
    
    def vowel_drop_kebab_case(self, parse_l:list[str]):
        """Converts parsed word list to vwl-drp-kbb-cs string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: vwl_drp_snk_cs string
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        parse_l = '_'.join(parse_l)
        parse_l = [w for w in parse_l if w not in vowels]
        return ''.join(parse_l)
    
    def kebab_case(self, parse_l:list[str]):
        """Converts parsed word list to a kebab-case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: kebab-case string
        """
        return '-'.join(parse_l)
    
    def camel_kebab_case(self, parse_l:list[str]):
        """Converts parsed word list to a camel-Kebab-Case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: camel-Kebab-Case string
        """
        parse_l[1:] = [w.capitalize() for w in parse_l[1:]]
        return '-'.join(parse_l)
    
    def pascal_kebab_case(self, parse_l:list[str]):
        """Converts parsed word list to a Pascal-Kebab-Case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: Pascal-Kebab-Case string
        """
        parse_l = [w.capitalize() for w in parse_l]
        return '-'.join(parse_l)
    
    def upper_kebab_case(self, parse_l:list[str]):
        """Converts parsed word list to a UPPER-KEBAB-CASE string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: UPPER-KEBAB-CASE string
        """
        parse_l = [w.upper() for w in parse_l]
        return '-'.join(parse_l)
    
    def dotted_case(self, parse_l:list[str]):
        """Converts parsed word list to a dot.notation.case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: dot.notation.case string
        """
        return '.'.join(parse_l)
    
    def camel_dotted_case(self, parse_l:list[str]):
        """Converts parsed word list to camel.Dotted.Case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: camel.Dot.Note.Case string
        """
        return '.'.join(parse_l)
    
    def pascal_dotted_case(self, parse_l:list[str]):
        """Converts parsed word list to a Pascal-Dotted-Case string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: Pascal-Dotted-Case string
        """
        parse_l = [w.capitalize() for w in parse_l]
        return '.'.join(parse_l)
    
    def upper_dotted_case(self, parse_l:list[str]):
        """Converts parsed word list to a UPPER-DOTTED-CASE string

        Args:
            parse_l (list[str]): list of words.

        Returns:
            str: UPPER-DOTTED-CASE string
        """
        parse_l = [w.upper() for w in parse_l]
        return '-'.join(parse_l)

    def parse(self, *strings:str, format='camelCase'):
        for non_delim_string in strings:
            self.parse_list = []
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
                        self.parse_list.append(norm_string[-i:])
                        norm_string = norm_string[:-i]
                        i = len(norm_string)
                    elif norm_string[-i:] in \
                        self.__en_dict__[len(norm_string[-i:])] \
                            [norm_string[-i]]:
                        
                        self.parse_list.append(norm_string[-i:])
                        norm_string = norm_string[:-i]
                        i = len(norm_string)
                    else:
                        i -= 1
                else:
                    i -= 1
            

