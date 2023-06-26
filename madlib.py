import re

print("Welcome to madlib!")

def read_template(file_path):
  """
  Reads the madlib template from a file.

  Args:
    file_path: The path to the madlib template file.

  Returns:
    The contents of the madlib template as a string.
  """

  with open(file_path, 'r') as file:
    template = file.read()

    return template

def parse_template(template):
  """
  Parses the madlib template and returns a dictionary of story elements and a list of
  words that need to be filled in by the user.

  Args:
    template: The madlib template as a string.

  Returns:
    A dictionary of story elements and a list of words that need to be filled in
    by the user.
  """

  # nonCurly variable is used to keep track whether or not characters are inside curly braces
  nonCurly = False

  # storyDictionary stores the story elements as a dictionary.
  storyDictionary = {}

  # emptyFiller variable is used to store content inside curly braces
  emptyFiller = ''

  # wholeWordList stores individual words found inside the curly braces
  wholeWordList = []

  # ignore simply ignores these specific characters when reading the template
  ignore = ['{', '}']

  for char in template:
    if char == '}':
      wholeWordList.append(emptyFiller)
      emptyFiller = ''
      nonCurly = False

    if char == '{':
      storyDictionary[emptyFiller] = ''
      nonCurly = True

    if nonCurly == False:
      storyDictionary[emptyFiller] += char
    else:
      if char not in ignore:
        emptyFiller += char

  return storyDictionary, tuple(wholeWordList)

def newList(wholeWordList):
  """
  Prompts the user to enter values for the words in the wholeWordList.

  Args:
    wholeWordList: A list of words that need to be filled in by the user.

  Returns:
    A list of the user-entered values.
  """

  newWholeWordList = []

  for i in wholeWordList:
    userInput = input(f"Enter a(n) {i}: ")
    newWholeWordList.append(userInput)

  return tuple(newWholeWordList)

def merge(storyDictionary, newWholeWordTuple):
  """
  Merges the storyDictionary with the newWholeWordTuple.

  Args:
    storyDictionary: The story dictionary.
    newWholeWordTuple: A tuple of the user-entered values.

  Returns:
    The merged story dictionary.
  """

  newWholeWordList = list(newWholeWordTuple)
  pattern = r"\{([^}]*)\}"
  result = re.sub(pattern, lambda x: newWholeWordList.pop(0), storyDictionary)

  return result

def write_madlib_to_file(file_path, madlib):
  """
  Writes the madlib to a file.

  Args:
    file_path: The path to the madlib file.
    madlib: The madlib as a string.
  """

  with open(file_path, 'w') as file:
    file.write(madlib)

if __name__ == "__main__":
  template = read_template('madlib.txt')
  stripped_template, parts = parse_template(template)
  newList = newList(parts)
  finalStory = merge(stripped_template, newList)
  write_madlib_to_file('finished_madlib.txt', finalStory)
  parse_template(template)
