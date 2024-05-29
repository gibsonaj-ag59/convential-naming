import unittest
from case_parser import CaseParser
from string import printable
from time import time
class TestCaseParser(unittest.TestCase):
    def setUp(self):
        self.timer = time() 
        self.seps = [p for p in printable if not p.isalnum()]
        self.seps.pop(23)
        self.seps.append('')
        self.CP = CaseParser()
        self.test_cases = [
                "simpleTestString",  # Simple string with no special characters
                "AnotherSimpleTest123",  # String with numbers
                "This_is_a_Test_String_with_Underscores",  # String with underscores
                "StringWith---Multiple-Hyphens",  # String with multiple hyphens
                "MiXeD_CaSe_And123Numbers456",  # String with mixed case and numbers
                "randomSTRING_withVARIOUS@@symbols&&andNumbers1234",  # String with various symbols and numbers
                "moreComplexStringWith#Various_SymbolsAnd_MixedCases567",  # String with more complex mix of symbols and cases
                "aVery---LongString_withLots__OfDifferentCharacters_1234567890",  # Long string with many different characters
                "shortString!@#",  # Short string with special characters
                "finalTestString_With123Numbers_andSymbols*&^%$#@",  # Final string with numbers and a variety of symbols
                "ExtraComplexString_with**Multiple_Separators_andNumbers6789",  # Extra complex string with multiple separators
                "NoisyStringWith@@@@Lots$$$of%%%Special###Characters",  # Noisy string with many special characters
                "UnderScore_Heavy__String_With_MixedCases_andNumbers987",  # String with heavy underscores
                "CapsLOCKStringWITHMixedCAPS_and_NUMBERS4321",  # String with mixed capitalization
                "longStringWithVariety123_andSpecialCharacters!@#$%^",  # Long string with variety and special characters
                "simpleMixedString_withNumbers1234andLetters",  # Simple mixed string with numbers and letters
                "another---example_with_Mixed!@#cases_and123Numbers",  # Another example with mixed cases and symbols
                "shortAndSweet12345",  # Short string with numbers
                "superLONGStringWithALotOfDifferentTypesOfCharacters1234567890",  # Super long string with many types
                "finalExample_String-with_Many**Kinds++of&&Symbols_and123Numbers",  # Final example with many kinds of symbols and numbers
            ]
        
    def get_time(self):
        _ct = time() - self.timer
        self.timer = time()
        return f'\n{format(_ct, ".2")} seconds to test\n' + \
               f'{len(self.seps)* len(self.test_cases) * len(list(self.CP.__cases__.keys()))} string normalizations.\n' + \
               f'Separators: {len(self.seps)}\n' + \
               f'Test Strings: {len(self.test_cases)}\n' + \
               f'Cases: {list(self.CP.__cases__.keys())}'
    
    def test_camel_case_parse(self):
        for sep in self.seps:
            strings = self.CP.parse(*self.test_cases, sep=sep, casing='camel', drop_vowels=False)
            self.assertTrue(len(strings) == 20)
            self.assertTrue(strings[0].islower())
            for s in strings:
                self.assertNotRegex(s, r'([^a-zA-Z0-9' + sep + '])')
        print(self.get_time())

    def test_lower_case_parse(self):
        for sep in self.seps:
            strings = self.CP.parse(*self.test_cases, sep=sep, casing='lower', drop_vowels=False)
            self.assertTrue(word.islower() for word in strings)
            for s in strings:
                self.assertNotRegex(s, r'([^a-zA-Z0-9' + sep + '])')
        print(self.get_time())

    def test_drop_vowels_all_cases(self):
        for sep in self.seps:
            strings = self.CP.parse(*self.test_cases, sep=sep, casing='lower', drop_vowels=True)
            for s in strings:
                self.assertNotRegex(s, r'([^a-zA-Z0-9' + sep + '])')
                self.assertNotRegex(s, r'^[^aeiou]+')
        print(self.get_time())
    
    def test_pascal_case_parse(self):
        for sep in self.seps:
            strings = self.CP.parse(*self.test_cases, sep=sep, casing='pascal', drop_vowels=False)
            self.assertTrue(word[0].isupper() for word in strings)
            for s in strings:
                self.assertNotRegex(s, r'([^a-zA-Z0-9' + sep + '])')
        print(self.get_time())

    def test_upper_case_parse(self):
        for sep in self.seps:
            strings = self.CP.parse(*self.test_cases, sep=sep, casing='upper', drop_vowels=False)
            self.assertTrue(word.isupper() for word in strings)
            for s in strings:
                self.assertNotRegex(s, r'([^a-zA-Z0-9' + sep + '])')
        print(self.get_time())