from collections import defaultdict
from string import printable
import configparser
import json
class CamelCaseParser():
    """String formatter for different commmon programming cases.

    Yields:
        string: String with symbols removed.
    """
    ### init Resources
    # Read Config
    config = configparser.ConfigParser()
    config.read('case_parser.ini')
    w_json = config['DEFAULT']['WordJson']
    w_txt = config['DEFAULT']['WordTxt']
    # Init Word Dicts. w_dict is read from a
    __syms__ = [p for p in printable if not p.isalnum()]
    # txt document and is for user
    # updates to the word list. en_dict is read 
    # from JSON and is used by the
    # script. en_dict is updated from the w_dict.
    __en_dict__ = defaultdict(lambda : defaultdict(list))
    __w_dict__ = defaultdict(lambda : defaultdict(list))
    # Read Words JSON and populate en_dict
    with open(w_json, 'r') as f:
       __en_dict__ = json.load(f)
    # Read Word List and populate w_dict
    with open(w_txt, 'r') as f:
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
        # Set up a dictionary representing available case functions.
        self.__cases__ = {
        'lower': self.lower_case,
        'camel': self.camel_case,
        'pascal': self.pascal_case,
        'upper': self.upper_case,
    }

    def vowel_drop(self, word:str):
        """Converts parsed word to vwldrpcs string

        Args:
            words (list[str]): list of words.

        Returns:
            str: vwldrpcs string
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        for w in word:
            if w in vowels:
                word = word.replace(w, '')
        return word
    
    def create_case(self, words, sep='', case='camel', drop_vowels=False):
        """Converts parsed word list to a list of lowercase strings

        Args:
            words (list[str]): list of words.
            sep (str): Separtor between words. Default is ''.
            case (str): Case name for conversion.\n
                        Limited to 'lower', 'camel', 'pascal', 'upper'
            drop_vowels (bool): True to remove all vowels. Default is False

        Returns:
            string: converted strings joined on sep
        """
        words = self.__cases__[case](words)
        if drop_vowels:
            words = [self.vowel_drop(w) for w in words]
        return sep.join(words)

    def lower_case(self, words):
        """Converts parsed word list to a list of lowercase strings

        Args:
            words (list[str]): list of words.

        Returns:
            list: lowercase strings
        """
        words = [w.lower() for w in words]
        return words
    
    def camel_case(self, words):
        """Converts parsed word list to a list of camelCase strings

        Args:
            words (list[str]): list of words.

        Returns:
            list: camelCase strings
        """
        words[1:] = [w.capitalize() for w in words[1:]]
        return words
    
    def pascal_case(self, words):
        """Converts parsed word list to a list of PascalCase strings

        Args:
            words (list[str]): list of words.

        Returns:
            list: PascalCase strings
        """
        words = [w.capitalize() for w in words]
        return words
    
    def upper_case(self, words):
        """Converts parsed word list to a list of UPPERCASE strings

        Args:
            words (list[str]): list of words.

        Returns:
            list: UPPERCASE strings
        """
        words = [w.upper() for w in words]
        return words

    def parse(self, *strings:str, sep='', case='camel',
              drop_vowels=False):
        """Main parsing function.

        Args:
            *strings (tuple[str]): list of words, cleaned of symbols, and ready to convert.
            sep (str): join separator
            case (str): Case name for conversion.\n
                        Limited to 'lower', 'camel', 'pascal', 'upper'
            drop_vowels (bool): True to remove all vowels. Default is False

        Yields:
            str: String Converted to specified case and joined on sep.
        """
        for non_delim_string in strings:
            self.words_list = []
            for l in non_delim_string.lower():
                if l in self.__syms__:
                    non_delim_string = non_delim_string.replace(l, "")
            norm_string = non_delim_string.lower()
            reps = len(norm_string)
            i = reps
            while i in range(reps, 0, -1):
                if str(len(norm_string[-i:])) in self.__en_dict__.keys():
                    if norm_string[-i:].isdecimal():
                        self.words_list.append(norm_string[-i:])
                        norm_string = norm_string[:-i]
                        i = len(norm_string)
                    elif norm_string[-i:] in \
                        self.__en_dict__[str(len(norm_string[-i:]))] \
                            .get(norm_string[-i], []):
                        self.words_list.append(norm_string[-i:])
                        norm_string = norm_string[:-i]
                        i = len(norm_string)
                    else:
                        i -= 1
                else:
                    i -= 1
            self.words_list.reverse()
            yield self.create_case(self.words_list, sep, case, drop_vowels)

