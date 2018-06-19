# codeforces2pdf
Light tool to extract CodeForces problems into PDF files

## Motivation (why I've written this?)
I was training in someday and I was tired from sitting in front of the laptop, so I decided to download CodeForces problems in PDF, then print them and solve the problems on my bed!

Unfortunately there was not any good way to download CodeForces problems in PDF, I was looking for a PDF file contains only one problem and only the problem statement, that it is no CodeForces logo, tags and anything else.

So I've wrote this code in Python. However, this my first Python code and I've extracted all CodeForces problems in PDFs, you can find them [here](https://github.com/AliOsm/PDF-CodeForces-Problems) (there is crazy facts about CodeForces in that repository).

Ok, to be honest, training was not the only thing motivated me to do this, I was looking for some small project to try Selenium on it, so this is the key motivation.

Have fun with your training.

## Prerequisites
- [Python 3.x](https://www.python.org/)
- [Selenium](https://www.seleniumhq.org/)
- [ChromeDriver](http://chromedriver.chromium.org/)
- [WeasyPrint](https://weasyprint.org/)
- The code in this repository tested on Ubuntu 18.04 LTS

## Usage
After downloading the files in this repository (codeforces2pdf.py - css.css), from terminal you can run them as follows:

`>> python3 codeforces2pdf.py <contest_id> <problem_character>`
