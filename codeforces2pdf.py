import sys

from selenium import webdriver
from weasyprint import HTML, CSS
import os
from scipy._lib.six import xrange

def exit(message):
  print(message)
  sys.exit(1)

def extract_contest(driver, contest_id):
  # construct contest url
  contest_url = 'https://codeforces.com/contest/{0}/problems'.format(contest_id)

  # get the target page
  driver.get(contest_url)

  # extract contest
  try:
    return contest_id + '.pdf', driver.execute_script('return document.getElementsByClassName("problem-frames")[0].innerHTML;')
  except:
    exit('Invalid arguments values')

def extract_problem(driver, contest_id, problem_character):
  # construct problem url
  problem_url = 'https://codeforces.com/contest/{0}/problem/{1}'.format(contest_id, problem_character)
  
  # get the target page
  driver.get(problem_url)

  # extract problem statement
  try:
    return contest_id + problem_character + '.pdf', driver.execute_script('return document.getElementsByClassName("problemindexholder")[0].innerHTML;')
  except:
    exit('Invalid arguments values')

def extract_problems_range(driver, contest_id, start_problem_character, end_problem_character):
  range_HTML = ""
  last_found_character = ''
  for character in map(chr, xrange( ord(start_problem_character[0]), ord(end_problem_character[0])+1 )   ):
    
    # construct problem url
    problem_url = 'https://codeforces.com/contest/{0}/problem/{1}'.format(contest_id, character)
    try:
      # get the target page
      driver.get(problem_url)
      # extract problem statement
      #print("#"+driver.execute_script('return document.body.innerHTML;'))
      if driver.execute_script('return document.body.innerHTML;').find("No such problem") != -1:
        #print("#"+driver.execute_script('return document.body.innerHTML;'))
        print("No more problems to pull.")
        break
        
      range_HTML += driver.execute_script('return document.getElementsByClassName("problemindexholder")[0].innerHTML;')
      print("problem [" + character + "] has been pulled successfully.")
      last_found_character = character
    except:
      break
  return contest_id + '[' + start_problem_character + '-' + last_found_character + ']' +'.pdf', range_HTML



def main():
  len_argv = len(sys.argv)

  # check the number of command-line arguments
  if len_argv < 2 or len_argv > 4:
    sys.exit('usage: codeforces2pdf.py <contest_id> [problem_character]')

  # set driver options
  options = webdriver.ChromeOptions()
  options.add_argument('headless')

  print(options)
  # initialize driver
  driver = webdriver.Chrome(chrome_options = options)

  # choose to extract contest or problem
  if len_argv == 2:
    file_name, html = extract_contest(driver, sys.argv[1])
  elif len_argv == 3:
    file_name, html = extract_problem(driver, sys.argv[1], sys.argv[2])
  elif len_argv == 4:
    file_name, html = extract_problems_range(driver, sys.argv[1], sys.argv[2], sys.argv[3])
  # close the driver
  driver.quit()

  # build the PDF file
  HTML(string = html, base_url = 'https://codeforces.com/').write_pdf(file_name, stylesheets = [CSS('css.css')])

if __name__ == "__main__":
  main()
