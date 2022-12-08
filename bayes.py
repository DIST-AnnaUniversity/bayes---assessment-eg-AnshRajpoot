# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:35:45 2022

@author: Ansh Rajpoot
"""

def prob(expect,total):
  return expect/total
def bayesTheorem(pBook, pBoys, pBoysbook):
    return (pBook * pBoysbook) / pBoys
total=10
boys=40
girls=60
boys_having_book=5
girls_having_book=20
p_of_book=prob(25,100)
p_of_boys_having_books=prob(5,25)
pBoy=prob(40,100)

print("probablity oh boys that having book: "+str(round(bayesTheorem(p_of_book,pBoy,p_of_boys_having_books),2)))