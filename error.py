import json
import csv
import re
file_path = "logs.json"
with open(file_path) as json_file:
    data = json.load(json_file)
    header = data[0].keys()
    values = [list(item.values()) for item in data]
    with open("error_logs.csv","w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        if len(header)==0:
            print("Issue writing header to CSV file, header is empty!")
        pattern = r"ERROR"
        for string in values:
            match = re.search(pattern,string,re.IGNORECASE)
            if match:
                writer.writerow(string)
                if len(string)==0:
                    print("Error writing string to CSV file, string is empty!")
            
            











    