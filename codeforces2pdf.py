import sys

from selenium import webdriver
from weasyprint import HTML, CSS

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
    return contest_id + '.pdf', driver.execute_script('return document.getElementsByClassName("problem-frames")[0].innerHTML;');
  except:
    exit('Invalid arguments values')

def extract_problem(driver, contest_id, problem_character):
  # construct problem url
  problem_url = 'https://codeforces.com/contest/{0}/problem/{1}'.format(contest_id, problem_character)
  
  # get the target page
  driver.get(problem_url)

  # extract problem statement
  try:
    return contest_id + problem_character + '.pdf', driver.execute_script('return document.getElementsByClassName("problemindexholder")[0].innerHTML;');
  except:
    exit('Invalid arguments values')

def main():
  len_argv = len(sys.argv)

  # check the number of command-line arguments
  if len_argv < 2 or len_argv > 3:
    sys.exit('usage: codeforces2pdf.py <contest_id> [problem_character]')

  # set driver options
  options = webdriver.ChromeOptions()
  options.add_argument('headless')

  # initialize driver
  driver = webdriver.chrome.webdriver.WebDriver(options=options)

  # choose to extract contest or problem
  if len_argv == 2:
    file_name, html = extract_contest(driver, sys.argv[1])
  elif len_argv == 3:
    file_name, html = extract_problem(driver, sys.argv[1], sys.argv[2])

  # close the driver
  driver.quit()

  # build the PDF file
  HTML(string = html, base_url = 'https://codeforces.com/').write_pdf(file_name, stylesheets = [CSS('css.css')])

if __name__ == "__main__":
  main()
