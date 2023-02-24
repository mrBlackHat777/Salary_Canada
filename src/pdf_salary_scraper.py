# importing required modules
from PyPDF2 import PdfReader
import re
from pathlib import Path
import pandas as pd
# creating a pdf reader object
reader = PdfReader("data/2023 Salary Guide _PDF.pdf")
provinces = ["ontario", "québec", "british columbia", "alberta", "manitoba", "saskatchewan", "nova scotia", "new brunswick", "newfoundland & labrador", "prince edward island"]
regions=['calgary metropolitan region', 'edmonton metropolitan region', 'northern alberta', 'red deer', 'fort st. john', 'fraser valley', 'greater vancouver', 'greater victoria', 'kelowna', 'prince george', 'surrey/delta', 'winnipeg metropolitan region', 'greater moncton', 'saint john', 'york region', 'conception bay - st. john’s', 'greater halifax', 'brant county', 'cambridge', 'durham region', 'frontenac county', 'greater hamilton area', 'greater sudbury area', 'greater toronto area', 'halton region', 'hastings county', 'london area', 'niagara region', 'ottawa metropolitan region', 'oxford county', 'peel region', 'peterborough county', 'simcoe county', 'waterloo region', 'wellington county', 'windsor-essex county', 'york region', 'queens - charlottetown', 'centre-du-québec', 'chaudière-appalaches', 'estrie', 'lanaudière', 'laurentides', 'laval', 'mauricie', 'montérégie - agglomeration ', 'montérégie - brome-missisquoi', 'montérégie - la haute-yamaska', 'montérégie - les maskoutains', 'montérégie - vaudreuil-soulanges', 'montréal', 'national capital', 'outaouais', 'saguenay-lac-saint-jean', 'moose jaw', 'regina metropolitan area', 'saskatoon metropolitan area']


data = {'province': [],'region':[], 'job': [], 'entry': [], 'mid': [], 'senior': []}
# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page = reader.pages
current_region=""
current_province=""
for page in reader.pages:

    text = page.extract_text().lower()

    for line in text.splitlines():
        #find the province
        for province in provinces:
            if province in text.lower():
                current_province = province  # Save the province that was found
                break  # Exit the loop once a province is found
        for region in regions:
            if region in text.lower():
                current_region = region
                break
        #2023 salary guide  |61director of operations 110.0 -140.0 186.0 -190.0 210.0 -230.0
        if "2023 salary guide" in line.lower():
            #remove 2023 salary guide  |XX from the line to keep only the job title and salary range
            pattern = r"\d{4}\s\S+\s\S+\s+\|\d+"
            line = re.sub(pattern, "", line)
            
            

        # extract job title and salary range
        #inventory control manager 68.9 -87.5 78.9 -99.6 91.2-119.8
        if "-" in line.lower() :

        
            #administrative assistant43.6 - 56.449.9 - 61.355.2 - 66.7
            #administrative manager65.2 - 74.371.1 - 81.978.7 - 94.6
            regex = r"^(\D+)(.*)$"

            # Extract job title
            match = re.match(regex, line)
            job_title = match.group(1).strip()

            # Split remaining numbers
            numbers = match.group(2)


            #14.25 - 18.0 16.0 - 21.0 18.0 -21.0
            pattern = r'(\d+\.\d+)\s*-\s*(\d+\.\d+)'

            # Find all matches of the pattern in the line
            numbers = re.findall(pattern, numbers)

            #split numbers into 3 groups or 4 groups(finance department)
            if len(numbers) == 3:
                    entry_range = numbers[0][0] + "-" + numbers[1][1]
                    mid_range = numbers[1][0] + "-" + numbers[1][1]
                    senior_range = numbers[2][0] + "-" + numbers[2][1]
            elif(len(numbers) == 4):
                continue
                year_1 = numbers[0] + "-" + numbers[1]
                years_3 = numbers[2] + "-" + numbers[3]
                years_5= numbers[4] + "-" + numbers[5]
                years_10=  numbers[6] + "-" + numbers[7]
            

            #print(f"job: {job_title}, entry: {entry_range}, mid: {mid_range}, senior: {senior_range}")
            data['job'].append(job_title)
            data['entry'].append(entry_range)
            data['mid'].append(mid_range.strip())
            data['senior'].append(senior_range.strip())
            data['province'].append(current_province)
            data['region'].append(current_region)
        else:
            #secteurs d'activité    
            #print(line)
            continue


#save data to pickle file
output_file = 'data/salary_guide.pkl'
pd.to_pickle(data,output_file)
df =  pd.DataFrame(data)
print(df.head())

