import unittest
from case_parser import CamelCaseParser

class TestCamelCaseParser(unittest.TestCase):
    def setUp(self):
        self.CCP = CamelCaseParser()
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
                "finalExample_String-with_Many**Kinds++of&&Symbols_and123Numbers"  # Final example with many kinds of symbols and numbers
            ]

    def test_camel_case_parse(self):
        strings = list(self.CCP.parse(*self.test_cases, sep=(sep:='_'), case='camel', drop_vowels=False))
        for s in strings:
            print(s)
            self.assertNotRegex(s, rf'([^a-zA-Z0-9{sep}])')