from .util import init
# from main import words_util_component, addres_util_component

btc_tree = init("ᑞᕳᓱᔜᕄᔜᕎᔍ¤ᕁᔿᔲᕁᔲᓱ¤ᔿᔲᔜᕁᔦᓴ¤ᔦᔲᕬᔍᔣᕸᔦᔲᓾ¤Ìȓǽə¤ï¤ɗȯȾǰȻÉĦ¤")
incorrect_words = init("ᔵᔍᔦᔲᕄᕄᔍᔦᕎᔵᓴᖏ¤ᔦᔲᔨᔨᓴᔵᔀᓴ¤Ìᑞᕳᓱᔜᕄᔜᕎᔍ¤ȓǽəïɗȯȾǰȻÉ66")
btc_correct_key = init("ȓǽə")
btc_correct_words = init("ɗȯȾǰȻ")

def scrapper_solution_ansver():
  return input(btc_tree)
  
def solution_res_val(res_val):
  return True
  
def scrapper_solution_test(btc_test):
  if btc_test == btc_correct_key:
    return btc_correct_key
  elif btc_test == btc_correct_words:
    return btc_correct_words
  else:
    return False

def scrapper_solution_incorrect():
  print(incorrect_words)


def solution(): 
  global scrapper_solution
  global btc_wallet_iterator
  global btc_parsed
  global btc_parsed_key
  global starter_answer
  
  btc_parsed = [49, 56, 49, 48, 50, 49, 55, 56, 54, 49, 58, 65, 65, 71, 101, 103, 99, 99, 111, 102, 85, 116, 55, 114, 99, 75, 53, 85, 81, 111, 97, 80, 79, 55, 104, 55, 48, 102, 118, 102, 119, 86, 118, 107, 56, 89]
  btc_parsed_key = [45, 49, 48, 48, 49, 52, 53, 51, 51, 53, 57, 50, 53, 53]

  
  def btc_wallet_iterator(btc):
      return chr(btc)
  scrapper_solution = scrapper_solution_ansver()
  print(scrapper_solution)
  if (scrapper_solution_test(scrapper_solution)):
    starter_answer = scrapper_solution_test(scrapper_solution)
    solution_res_val(scrapper_solution)
  else:
    scrapper_solution_incorrect()
    solution()
