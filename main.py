import sys
import pickle
import random
import argparse
import logging
import spacy
import fitz

def main():

  parser = argparse.ArgumentParser(
        description='Script to parse PDF resumes, and create a csv file containing contact info '
                    'and required fields')
  parser.add_argument('--data_path', help='Path to folder containing documents ending in .pdf',
                      required=True)

  args = parser.parse_args()
  path = args.data_path

  resume_parser(path)

def resume_parser(path):
  nlp_model = spacy.load('nlp_model')
  fname = path
  doc = fitz.open(fname)
  text = ""
  for page in doc:
    text = text + str(page.getText())
    text= "".join(text.split('\n'))
  doc = nlp_model(text)
  for ent in doc.ents:
    print(f'{ent.label_.upper():{30}}-{ent.text}')
    

if __name__ == '__main__':
    main()
