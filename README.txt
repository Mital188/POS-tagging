----------------------
Programming Language and Compiler
----------------------

-Python3.0
-Pycharm3 edu

----------------------
To compile the code
----------------------

Copy paste the POSTagging.py python file and corpus.txt text file in the window


In command line 
python POSTagging.py

- Just the file name is sufficient, the code reads from the corpus directly
- Code has a runtime of 4min
- Corpus name (corpus.txt), to be kept in the same folder as the source code

----------------------
OutPut
----------------------
Table with top 5 erroneously tagged words, error rate and new error rate after applying rules

'Word'          'Error Rate'    'New Error Rate'
------------------------------------------------------
some word  	0		0


------------------------
RULES (POS tagging)
------------------------

1. if previous word is tagged NN, then tag "that" with "IN"
2. if previous word is tagged MD, then tag "have" with "VBP"
3. if previous word is tagged VBD, then tag "more" with "JJR"
4. if previous word is tagged PRP, then tag "'s" with "POS"
5. if previous word is tagged NN, then tag "plans" with "VBZ"

