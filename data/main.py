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

def create_event_speaker():
    presentation_titles = {
        "Technology": [
            "The Future of Quantum Computing: Possibilities and Challenges",
            "Blockchain Beyond Cryptocurrencies: Revolutionizing Digital Transactions",
            "The Role of 5G in Bridging the Digital Divide",
            "Progressive Web Apps: The Future of Mobile Experiences",
            "Web Development in the AI Era: Opportunities and Challenges"
        ],
        "Health": [
            "The Science of Sleep: How It Affects Productivity and Longevity",
            "The Role of Technology in Modern Healthcare: Telemedicine and Beyond",
            "Mental Health Awareness in the Digital Age"
        ],
        "Fitness": [
            "The Impact of Wearable Tech on Personal Fitness Goals",
            "Mind-Body Connection: Yoga for Physical and Mental Wellness",
            "Debunking Fitness Myths: What Really Works?"
        ],
        "Business": [
            "Digital Transformation: The Future of Small and Medium Businesses",
            "Global Market Trends: Opportunities for Emerging Entrepreneurs",
            "The Art of Negotiation: Building Better Business Relationships"
        ],
        "Finance": [
            "Decoding Personal Finance: From Budgeting to Investments",
            "The Rise of FinTech: Transforming Financial Services",
            "Crypto vs. Traditional Finance: The Great Debate"
        ],
        "Marketing": [
            "Leveraging Social Media for Business Growth in 2024",
            "The Psychology of Consumer Behavior: How Marketing Influences Decisions",
            "Content Marketing in the Age of AI: Balancing Creativity and Automation"
        ],
        "Education": [
            "Gamification in Learning: Making Education Engaging and Fun",
            "The Impact of AI on Personalized Learning Experiences",
            "Bridging Gaps in Education: The Role of Online Platforms"
        ],
        "Science": [
            "CRISPR and Gene Editing: Ethical Implications and Innovations",
            "Exploring Renewable Energy: Advances in Solar and Wind Power",
            "The Mysteries of Space: What We’ve Learned from the James Webb Telescope"
        ],
        "Psychology": [
            "Understanding Emotional Intelligence: Key to Personal and Professional Success",
            "The Role of Dopamine in Motivation and Behavior",
            "How Social Media Shapes Modern Psychology"
        ],
        "Arts & Culture": [
            "The Evolution of Digital Art in the NFT Era",
            "Preserving Indigenous Cultures in a Globalized World",
            "The Role of Art in Activism and Social Change"
        ],
        "Entrepreneurship": [
            "Startup Survival: Scaling from Idea to Execution",
            "The Role of Failure in Entrepreneurial Success",
            "Networking Strategies for Aspiring Entrepreneurs",
            "Transformational Leadership: Inspiring Change in Organizations",
            "The Role of Empathy in Modern Leadership",
            "Building Resilient Teams: Lessons from Sports Leadership"
        ],
        "Sports": [
            "The Impact of Technology on Sports Performance and Training",
            "Analyzing Major Sports Trends: From Esports to Traditional Games",
            "Sports Psychology: Mental Conditioning for Peak Performance"
        ],
        "Innovation": [
            "Design Thinking: A Framework for Innovation in Any Field",
            "How AI Is Reshaping the Innovation Landscape",
            "Disruptive Innovations That Changed Entire Industries"
        ],
        "Sustainability": [
            "The Role of Corporations in Achieving Global Sustainability Goals",
            "Circular Economy: Reducing Waste and Maximizing Resources",
            "Urban Farming: The Future of Sustainable Food Production"
        ]
    }
    exported_data = []

    events_file = open('event.csv', 'r', encoding='utf8')
    events = list(csv.DictReader(events_file))

    speakers_file = open('speaker.csv', 'r', encoding='utf8')
    speakers = list(csv.DictReader(speakers_file))
    
    i = 1
    for event in events:
        number_of_speakers = random.randint(1, 15)
        random_sample_speakers = random.sample(speakers, number_of_speakers)
        order = 1

        for speaker in random_sample_speakers:
            exported_data.append({
                'id': i,
                'speaker_id': speaker['speaker_id'],
                'event_id': event['event_id'],
                'presentation_titles': random.choice(presentation_titles[speaker['expertise']]),
                'stage_order': order
            })
        i += 1
        order += 1

    with open('event_speaker.csv', 'w', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'id', 'speaker_id', 'event_id', 'presentation_titles', 'stage_order'
        ])
        writer.writeheader()
        writer.writerows(exported_data)
    print(len(exported_data))

create_event_speaker()

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