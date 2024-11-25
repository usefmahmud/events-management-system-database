import csv
from datetime import datetime

def fix_events():
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

def fix_users():
    user_file = open('user.csv', 'r', encoding='utf8')
    users = list(csv.DictReader(user_file))
    
    i = 1
    for user in users:
        user['user_id'] = i
        i += 1
    
    with open('user_copy.csv', 'w', encoding='utf8') as file:
        fieldnames = users[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)
fix_users()

'''
user [in progress]
speaker [done]
venue [done]
sponsor [done] 
organization [done]
event [done]
event_speaker
event_sponsor
user_attend
'''