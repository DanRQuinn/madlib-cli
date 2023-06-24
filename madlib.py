# print welcome message

import re

def welcome_message():
    welcome_message = "Its Madlib time! Get ready to make some fun Madlibs! Fill in the blanks with funny words and see what comes out!"

    print(welcome_message)


# open the file into string
def read_template(file_path):
  non_curly = False
  story_dictionary = ''
  story_list = []
  word_list = []
  empty_filler = ''
  ignore = ["{","}"]
  new_list = []
  with open('madlib.txt', "r")as file:
    template = file.read()
  


      # parse template into useable parts
    for char in template:
      if char == "}":
          word_list.append(empty_filler)
          empty_filler = ''
          non_curly = False

      if char == "{":
          # when changing value use single =
          non_curly = True
          story_dictionary = ''

      if non_curly == False:
          if char not in ignore:
            story_dictionary += char

      else:
          if char not in ignore:
            empty_filler += char


          # print story list
              
          # print(word_list)

  for i in word_list:  
    user_input = input(f"enter a(n) {i}: ")
      #  take user input and populate the template with user answer
    updated_string = new_list.append(user_input)

  print(new_list)
        #  give user back completed response
        # prompt user to submit words for matching spaces
  return template

def parse_template(template):
  pattern = r"\{([^}]*)\}"
  result = re.sub(pattern, lambda word: new_list.pop(0), template)
  print(result)

def merge(stripped_template):



  with open('finished_madlib.txt', "w")as file:
    template = file.write(result)

if __name__ == "__main__":
  welcome_message()
