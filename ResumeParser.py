# # Libraries used
""" pdf2txt -> pdf to text (downloaded file as development stopped before Py 2.7)
spacy -> natural language processing
re -> regex
os -> os file
pandas -> output csv """

import spacy  # nlp
import re  # regex
import os  # file manipulation
import pandas as pd  # csv
import pdf2txt
from tabulate import *


# Company Details
companyName = input("Enter the name of the company : ")
companyPosition = input("Enter the job designation : ")
companySkills = list(map(str, input("Enter all the skills required by the company : ").split()))
companyTable = [["NAME", "DESIGNATION", "SKILLS REQUIRED"]] + [[companyName, companyPosition, companySkills]]
print(tabulate(companyTable, headers="firstrow", tablefmt="fancy_grid"))
companySkills = [i.lower() for i in companySkills]

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Capture 4 important details: name, mobile no., email and skills
result_dict = {
    'name': [],
    'email': [],
    'phones': [],
    'skills': [],
    'compatibility': []
}
names = []
phones = []
emails = []
skills = []
compatibility = []


# converting pdf to text
def convert_pdf(f):
    """
    Converts the pdf file to text and saves it in the output/txt folder
    It also reads the file
    1. Creating output filename
    2. Creating output filepath
    3. Converting pdf to text
    4. Printing user message
    5. Returning the txt content
    """
    names.append(os.path.splitext(f)[0][8:])
    output_filename = os.path.basename(os.path.splitext(f)[0]) + ".txt"
    output_filepath = os.path.join("output/txt/", output_filename)
    pdf2txt.main(args=[f, "--outfile", output_filepath])
    print(output_filepath + " saved successfully!")
    return open(output_filepath).read()


def parse_content(text):
    """
    Parses the content of the file by making use of regex and nlp
    """
    skill_set = re.compile("|".join(companySkills))
    phone_num = re.compile(
        "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    )
    doc = nlp(text)
    email = [word for word in doc if word.like_email][0]
    phone = re.findall(phone_num, text.lower())
    skills_list = list(set(re.findall(skill_set, text.lower())))
    emails.append(email)
    phones.append(phone[0])
    skills.append(skills_list)
    count = 0
    for i in skills_list:
        if i in companySkills:
            count += 1
    compatibility.append(str((count/len(companySkills))*100)[:5]+"%")


print()
for file in os.listdir('resumes/'):
    if file.endswith('.pdf'):
        print("Reading -> ", file)
        txt = convert_pdf(os.path.join('resumes/', file))
        parse_content(txt)
        print("Extraction completed successfully\n")

result_dict['name'] = names
result_dict['email'] = emails
result_dict['phones'] = phones
result_dict['skills'] = skills
result_dict['compatibility'] = compatibility

result_df = pd.DataFrame(result_dict)
result_df.to_csv('output/csv/ResumeDetails.csv')
answer = [["NAME", "EMAIL-ID", "PHONE-NUMBER", "SKILLS", "COMPATIBILITY"]]
for i in range(len(names)):
    answer.append([names[i], emails[i], phones[i], skills[i], compatibility[i]])

print(tabulate(answer, headers="firstrow", tablefmt="fancy_grid"))