import csv
from datetime import datetime, timedelta
import random

def get_random_date(start_date: str, end_date: str,) -> str:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    delta = (end - start).days
    
    random_days = random.randint(0, delta)
    random_date = start + timedelta(days=random_days)
    
    return random_date.strftime("%Y-%m-%d")

def get_random_date_before(end_date: str, days_range: int) -> str:
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    random_days = random.randint(0, days_range)
    random_date = end - timedelta(days=random_days)
    
    return random_date.strftime("%Y-%m-%d")

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
# fix_users()

def create_user_attend():
    exported_data = []

    events_file = open('event.csv', 'r', encoding='utf8')
    events = list(csv.DictReader(events_file))

    users_file = open('user.csv', 'r', encoding='utf8')
    users = list(csv.DictReader(users_file))

    list_of_tickets = [
        [150, 200, 300],
        [300, 400, 600],
        [500, 700, 1000, 2000],
        [50, 60, 100, 150],
        [0, 200, 500],
        [3500, 5000]
    ]

    i = 1
    for event in events:
        event_max_attendees = event['maximum_attendees']
        
        random_percentage = random.randint(10,110) / 100
        max_users = round(random_percentage * int(event_max_attendees))
        chosen_list_tickets = random.choice(list_of_tickets)

        event_start, event_end = event['start_date'], event['end_date']
        after_start_prob = True if random.random() <= .15 else False
        random_date = ''
        if after_start_prob:
            random_date = get_random_date(event_start, event_end)
        else:
            random_date = get_random_date_before(event_start, random.randint(1, 30))

        users_random_sample = random.sample(users, min(len(users), max_users))
        for user in users_random_sample:
            random_attend_status = 'accepted' if random.random() < .8 else 'rejected'
            exported_data.append({
                'id': i,
                'user_id': user['user_id'],
                'event_id': event['event_id'],
                'ticket_price': random.choice(chosen_list_tickets),
                'payment_method': random.choice([
                    'Paypal', 'Debit Card', 'Cash', 'Cash'
                ]),
                'status': random_attend_status,
                'date': random_date # 15% after start of the event, 85% before start
            })

            i += 1
    
    with open('user_attend1.csv', 'w', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'id', 'user_id', 'event_id', 'ticket_price', 'payment_method', 'status', 'date'
        ])
        writer.writeheader()
        writer.writerows(exported_data)
    print(len(exported_data))
create_user_attend()

'''
user [done]
speaker [done]
venue [done]
sponsor [done] 
organization [done]
event [done]
event_speaker
event_sponsor
user_attend
'''