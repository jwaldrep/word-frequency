# word_frequency.py

## Description

A Python 3 script that analyzes the frequency of words in `sample.txt`. It reads this file and then returns the top 20 words used in the text and the number of times they are used, as well as a histogram-style bar-chart on the command line. Case and punctuation in the input file are ignored for this analysis.

The sample text provided is the Project Gutenberg version of _The Hound of the Baskervilles_ by Sir Arthur Conan Doyle. 

A basic test suite is provided in `word_frequency_test.py`.

### Example output
Using the supplied `sample.txt` file:
```
sir         ################################################## 347
upon        ############################################# 315
one         ################################## 240
man         ############################ 199
very        ########################### 191
holmes      ########################## 184
out         ######################## 168
moor        ###################### 155
henry       #################### 143
more        ################### 138
up          ################## 125
now         ################ 117
know        ################ 117
see         ################ 115
over        ################ 115
down        ############### 111
well        ############### 111
baskerville ############### 109
watson      ############### 109
dr          ############### 107
```

The following words are ignored in the output:
 ```
 a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
 because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
 for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
 it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
 not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
 since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
 twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
 would,yet,you,your
 ```


### Requirements  
* Python 3
* (optional) A text file to analyze, named `sample.txt`

## Additional Resources

* [Project Gutenberg](https://www.gutenberg.org/) - good source of free texts.
* [String type in Python](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
* [Regular expression operations](https://docs.python.org/3/library/re.html).
