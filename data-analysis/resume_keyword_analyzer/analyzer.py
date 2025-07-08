import re
def read_file(filePath):
    try:
        with open(filePath,'r',encoding='utf-8') as f:
            return f.read().lower()
    except FileNotFoundError:
        print("file not found")
        return ""

print("Step 1 : Reading the files Resume and Job Description respectively")                    
resume_text = read_file(r'C:\Users\Dell\OneDrive\Desktop\GIT\Python-Learning\data-analysis\resume_keyword_analyzer\resume.txt')
jd_text = read_file(r'C:\Users\Dell\OneDrive\Desktop\GIT\Python-Learning\data-analysis\resume_keyword_analyzer\job_description.txt')

print(resume_text)
print(jd_text)

print("_________________________________________________________________________________________________________________")
print("Step 2: Preprocess the Text (Basic Cleaning) ")
def clean_file(text):
    #Remove Punctuation and Special Characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().split()
    
resume_words = clean_file(resume_text)
jd_words = clean_file(jd_text)

print("Step3: Resume and jd after cleaning respectively")
print(resume_words)
print(jd_words)

print("_________________________________________________________________________________________________________________")
print("Step 4: Extract Unique Keywords from JD")
jd_keywords = list(set(jd_words))

print("Step 5: Unique words of jd: ")
print(jd_keywords)

print("_________________________________________________________________________________________________________________")
print("Step 6: Count Matching Words using NumPy + Pandas")

import numpy as np
import pandas as pd
#Counting frequency of words in resume
resume_word_freq = pd.Series(resume_words).value_counts()

# Filter those that match JD keywords
matched = resume_word_freq[resume_word_freq.index.isin(jd_keywords)]

not_matched = resume_word_freq[~resume_word_freq.index.isin(jd_keywords)]

print(matched)



print("_________________________________________________________________________________________________________________")
print("Step 7: Calculate a Matching Score")

matched_count = len(matched)
total_count = len(jd_keywords)

score = (matched_count/total_count) * 100

print(f"\nMatching Score: {score:.2f}%")
print("_________________________________________________________________________________________________________________")
improvement = input("Do you want to know how to improve your score and what are the missing words?: Y for yes , N for No: ").upper()

if(improvement=='Y'):
    print('These are the words which are lacking in your resume, add relevant experience using these words to improve your score: ')
    print(not_matched)
else:
    print("All the best for your job search journey !!")    




  
    