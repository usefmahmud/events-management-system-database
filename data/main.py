import csv
from datetime import datetime

event_file = open('event.csv', 'r', encoding='utf8')
events = list(csv.DictReader(event_file))

for event in events:
    event['start_date'] = datetime.strptime(event['start_date'],'%m/%d/%Y').strftime('%Y-%m-%d')
    event['end_date'] = datetime.strptime(event['end_date'],'%m/%d/%Y').strftime('%Y-%m-%d')

with open('events_copy.csv', 'w', encoding='utf8') as file:
    fieldnames = events[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(events)
    print(len(events))