# codeforces2pdf
Light tool to extract CodeForces problems into PDF files

## Motivation (Why I've written this?)
I was training in someday and I was tired from sitting in front of the laptop, so I decided to download CodeForces problems in PDF, then print them and solve the problems on my bed!

Unfortunately, there was not any good way to download CodeForces problems in PDF, I was looking for a PDF file that contains one problem with its statement only, without CodeForces` logo, tags or anything else.

So I've written this code in Python. However, this is my first Python code and I've extracted all CodeForces problems in PDFs, you can find them [here](https://github.com/AliOsm/PDF-CodeForces-Problems) (there are crazy facts about CodeForces in that repository).

Ok, to be honest, training was not the only thing motivated me to do this, I was looking for some small project to try Selenium on it, so this was the key of motivation.

Have fun with your training.

## Prerequisites
- [Python 3.x](https://www.python.org/)
- [Selenium](https://www.seleniumhq.org/)
- [ChromeDriver](http://chromedriver.chromium.org/)
- [WeasyPrint](https://weasyprint.org/)
- The code in this repository tested on Ubuntu 18.04 LTS

## Usage
After downloading the files in this repository (codeforces2pdf.py - css.css), from terminal you can run them as follows:

- Extract the entire contest problems in one PDF file:  
	`~ python3 codeforces2pdf.py <contest_id>`

- Extract one problem from a contest:  
	`~ python3 codeforces2pdf.py <contest_id> <problem_character>`
	