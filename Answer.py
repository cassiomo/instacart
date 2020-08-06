
import csv
from datetime import datetime
from dateutil.parser import parse
import re

def validate(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url)

def check_empty_string(str):
    if str:
        return str
    else:
        return "n/a"

def check_empty_string(str):
    if str:
        return str
    else:
        return "n/a"

def convert_float(str):
    if str:
        return float(str)
    else:
        return float(0)

save_file = open("output.csv", "w")

with open("data.csv", "rb") as f:
    reader = csv.reader(f, delimiter="\t")
    header = reader.next()
    rest = [row for row in reader]

colnum = 0

new_header = "order_id" + "\t" + "order_date" + "\t" + "user_id" + "\t" + "avg_item_price" + "\t" + "start_page_url" + "\t" + "error_msg"
new_header +="\r\n"
save_file.write(new_header)

new_row = ""

for row in rest:
    if row[0]:
        t0 = row[0].split(":")
        t0_count = len(t0)
        if t0_count == 2:
            new_row+=t0[0]
            new_row+="\t"
            # ot = datetime.strptime(t0[1], '%Y%m%d').strftime('%y-%m-%d')
            # ot = datetime.datetime.strptime(t0[1], '%Y%m%d').strftime('%y-%m-%d')
            #dt = parse(t0[1])
            #ot = dt.strftime('%y-%m-%d')
            new_row+=t0[1]
            # new_row+=ot
            new_row+="\t"
        else:
            new_row == "error"
    if not row[0]:
        new_row += "n/a"
        new_row+="\t"
    if row[1]:
        t1 = row[1]
        new_row+=t1
        new_row+="\t"
    if not row[1]:
        new_row += "n/a"
        new_row+="\t"

    avg_price = (convert_float(row[2]) + convert_float(row[3]) + convert_float(row[4]) +convert_float(row[5]))/ 4
    new_row += str(avg_price)
    new_row+="\t"
    if row[6]:
        if validate(row[6]):
            new_row+= row[6]
        else:
            new_row+=""
            new_row+="\t"
            new_row+="Invalid URL"
    if not row[6]:
        new_row+=""
        new_row+="\t"
        new_row+="Invalid URL"
    new_row +="\r\n"
    save_file.write(new_row)
    new_row=""


save_file.close()
f.close()
