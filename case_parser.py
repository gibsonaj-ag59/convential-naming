from collections import defaultdict
import concurrent.futures
from string import printable
import configparser
import json
class CaseParser():
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
    __syms__.pop(23)
    __syms__.append('')
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
        # Set up a dictionary representing available casing functions.
        self.__cases__ = {
        'lower': self.lower_case,
        'camel': self.camel_case,
        'pascal': self.pascal_case,
        'upper': self.upper_case,
    }

    def vowel_drop(self, word:str):
        """Converts parsed word to vself.words_listdrpcs string

        Args:
            words (list[str]): list of words.

        Returns:
            str: vself.words_listdrpcs string
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        for v in vowels:
            if v in word:
                word = word.replace(v, '')
        return word
    
    def create_case(self, 
                    words_list:list[str], 
                    sep:str='', 
                    casing:str='camel', 
                    drop_vowels:bool=False):
        """Converts parsed word list to a list of lowercase strings

        Args:
            words (list[str]): list of words.
            sep (str): Separtor between words. Default is ''.
            casing (str): casing name for conversion.\n
                        Limited to 'lower', 'camel', 'pascal', 'upper'
            drop_vowels (bool): True to remove all vowels. 
                                Default is False

        Returns:
            string: converted strings joined on sep
        """
        words = self.__cases__[casing](words_list)
        if drop_vowels is True:
            words = [self.vowel_drop(w) for w in words_list \
                     if len(w) > 1]
        return sep.join(words)

    def lower_case(self, 
                   words:list[str]
                   ) -> list[str]:
        """Converts parsed word list to a list of lowercase strings

        Args:
            words (list[str]): list of words.

        Returns:
            list: lowercase strings
        """
        words = [w.lower() for w in words]
        return words

    def camel_case(self, 
                   words:list[str]
                   ) -> list[str]:
        """Converts parsed word list to a list of camelCase strings

        Args:
            words (list[str]): list of words.

        Returns:
            list: camelCase strings
        """
        words = [words[0].lower()] + \
            [word.capitalize() for word in words[1:]]
        return words
    
    def pascal_case(self, 
                   words:list[str]
                   ) -> list[str]:
        """Converts parsed word list to a list of PascalCase strings

        Args:
            words (list[str]): list of words.

        Returns:
            list: PascalCase strings
        """
        words = [word.capitalize() for word in words]
        return words
    
    def upper_case(self, 
                   words:list[str]
                   ) -> list[str]:
        """Converts parsed word list to a list of UPPERCASE strings

        Args:
            words (list[str]): list of words.

        Returns:
            list: UPPERCASE strings
        """
        words = [word.upper() for word in words]
        return words
    def normalize(self, 
                  string:str
                  ) -> str:
        """Converts word to a lowercase string with no symbols or 
            whitespace.

        Args:
            strring (str): word to be stripped of symbols.

        Returns:
            str: word stripped of symbols and lowercase.
        """
        for s in self.__syms__:
            if s in string:
                string = string.replace(s, '')
        return ''.join(string).lower()
    
    def _parse(self, 
               string:str, 
               sep:str='', 
               casing:str='lower', 
               drop_vowels:bool=False
               ) -> str:
        """Main parsing function.

        Args:
            *strings (tuple[str]): list of words, 
                                    cleaned of symbols, 
                                    and ready to convert.
            sep (str): join separator
            casing (str): casing name for conversion.
                        Limited to 'lower', 'camel', 'pascal', 'upper'
            drop_vowels (bool): True to remove all vowels. 
                                Default is False

        Yields:
            str: String Converted to 
                 specified casing and joined on sep.
        """
        words_list = []
        norm_string = self.normalize(string)
        reps = len(norm_string)
        i = 0
        n = reps
        while i in range(n):
            if str(len(norm_string[i:n])) in self.__en_dict__.keys():
                if norm_string[i:n].isdecimal():
                    words_list.append(norm_string[i:n])
                    n -= len(norm_string[i:n])
                    i = 0
                elif norm_string[i:n] in \
                    self.__en_dict__[str(len(norm_string[i:n]))] \
                        .get(norm_string[i], []):
                    words_list.append(norm_string[i:n])
                    n -= len(norm_string[i:n])
                    i = 0
                else:
                    i += 1
            else:
                i += 1
        words_list.reverse()
        return self.create_case(words_list, 
                                sep=sep, 
                                casing=casing, 
                                drop_vowels=drop_vowels
                                )

    def parse(self, 
              strings:list[str], 
              sep:str='', 
              casing:str='lower', 
              drop_vowels:bool=False
              ) -> list[str]:
        """Main parsing function.

        Args:
            *strings (tlist[str]): list of words, to be cleaned of 
            symbols, and ready to convert.
            sep (str): join separator
            casing (str): casing name for conversion.
                        Limited to 'lower', 'camel', 'pascal', 'upper'
            drop_vowels (bool): True to remove all vowels. 
                                Default is False

        Yields:
            str: String Converted to specified casing and joined on 
                 sep.
        """
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_results = [executor.submit(self._parse, 
                                    str(string), 
                                    sep=sep, 
                                    casing=casing, 
                                    drop_vowels=drop_vowels
                                    ) \
                                        for string in strings
                                        ]
            results = [future.result() \
                for future in concurrent.futures
                .as_completed(future_results)]
        return results