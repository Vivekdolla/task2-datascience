# Required imports 
from PIL import Image 
import pandas as pd 
import requests 
import csv 
# ---------- IMAGE FILE ---------- 
def process_image(image_path): 
img = Image.open(image_path) 
print("Image Details:") 
print("Format:", img.format) 
print("Size:", img.size) 
print("Mode:", img.mode) 
# ---------- CSV FILE ---------- 
def process_csv(csv_path): 
df = pd.read_csv(csv_path) 
print("\n CSV File Columns:", df.columns.tolist()) 
print("Data Types:\n", df.dtypes) 
return df 
# ---------- EXCEL FILE ---------- 
def process_excel(excel_path): 
df = pd.read_excel(excel_path) 
print("\n Excel File Preview:\n", df.head()) 
# User-defined function to calculate average marks 
def calculate_averages(df): 
df['Average'] = df.iloc[:, 1:].mean(axis=1) 
return df 
return calculate_averages(df) 
# ---------- JSON FILE from API ---------- 
def process_json_from_api(url): 
response = requests.get(url) 
if response.status_code == 200: 
data = response.json() 
print("\n JSON from API (https://disease.sh):") 
print("Updated:", data['updated']) 
print("Total Cases:", data['cases']) 
print("Deaths:", data['deaths']) 
print("Recovered:", data['recovered']) 
return { 
"TotalCases": data['cases'], 
"Deaths": data['deaths'], 
"Recovered": data['recovered'] 
} 
else: 
print("Failed to fetch API data.") 
return {} 
# ---------- SAVE SUMMARY ---------- 
def save_summary_to_csv(df, summary_data, output_path): 
# Save Excel data 
df.to_csv(output_path, index=False) 
print(f"\n Processed Excel data saved to: {output_path}") 
# Save JSON summary below the CSV as additional info 
with open(output_path, 'a', newline='') as file: 
writer = csv.writer(file) 
writer.writerow([])  # empty line 
writer.writerow(['--- COVID-19 Global Summary ---']) 
for key, value in summary_data.items(): 
writer.writerow([key, value]) 
print(" COVID-19 summary appended to the same CSV.") 
# ---------- MAIN EXECUTION ---------- 
# Replace these with actual file paths 
image_path = 'D:/Anu/anurekha_photo.jpg' 
csv_path = 'E:/veltech/SS2526/Data Science/Data Science lab SS2526/students.csv' 
excel_path = 'E:/veltech/SS2526/Data Science/Data Science lab SS2526/student_marks.xlsx' 
json_url = 'https://disease.sh/v3/covid-19/all' 
output_csv = 'E:/veltech/SS2526/Data Science/Data Science lab SS2526/final_summary_output.csv' 
# Run each processor 
process_image(image_path) 
csv_data = process_csv(csv_path) 
excel_data = process_excel(excel_path) 
json_summary = process_json_from_api(json_url) 
# Save final output 
save_summary_to_csv(excel_data, json_summary, output_csv) 