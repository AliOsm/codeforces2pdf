import sys

from selenium import webdriver
from weasyprint import HTML, CSS

def main():
  if len(sys.argv) != 3:
    sys.exit('usage: codeforces2pdf.py <contest_id> <problem_character>')

  # construct problem url
  url = 'https://codeforces.com/contest/{0}/problem/{1}'.format(sys.argv[1], sys.argv[2])
  
  # construct problem file name
  filename = sys.argv[1] + sys.argv[2] + '.pdf'

  # set driver options
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  options.add_argument('window-size=1920x1080')

  # initialize driver
  driver = webdriver.Chrome(chrome_options = options)
  driver.get(url)

  # extract problem statement
  try:
    html = driver.execute_script('return document.getElementsByClassName("problemindexholder")[0].innerHTML;');
  except:
    print("Invalid arguments.")
    sys.exit(1)
  
  driver.quit()

  # build the PDF file
  HTML(string = html).write_pdf(filename, stylesheets = [CSS('css.css')])

if __name__ == "__main__":
  main()
