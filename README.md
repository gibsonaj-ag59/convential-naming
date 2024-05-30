# CaseParser

CaseParser is a Python class that provides string formatting for different common programming cases. It can parse and format strings in different casing styles such as lower case, camel case, pascal case, and upper case. It also provides an option to drop vowels from the words.

## Usage

```python
from case_parser import CaseParser

# Initialize the parser
parser = CaseParser()

# Parse a list of strings
strings = ["HelloWorld", "anotherString"]
result = parser.parse(strings, sep='_', casing='camel', drop_vowels=False)

# Output: ['hello_world', 'another_string']
print(result)
```

## Methods

### `vowel_drop(word:str) -> str`

Removes all vowels from a word.

### `create_case(words_list:list[str], sep:str='', casing:str='camel', drop_vowels:bool=False) -> str`

Converts a list of words into a specified casing style and optionally drops vowels.

### `lower_case(words:list[str]) -> list[str]`

Converts a list of words to lowercase.

### `camel_case(words:list[str]) -> list[str]`

Converts a list of words to camelCase.

### `pascal_case(words:list[str]) -> list[str]`

Converts a list of words to PascalCase.

### `upper_case(words:list[str]) -> list[str]`

Converts a list of words to UPPERCASE.

### `normalize(string:str) -> str`

Converts a word to a lowercase string with no symbols or whitespace.

### `_parse(string:str, sep:str='', casing:str='lower', drop_vowels:bool=False) -> str`

The main parsing function that converts a string into a specified casing style and optionally drops vowels.

### `parse(strings:list[str], sep:str='', casing:str='lower', drop_vowels:bool=False) -> list[str]`

A concurrent version of `_parse` that can handle multiple strings at once.