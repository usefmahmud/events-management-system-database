### Organizations and Basic Information:

* Organizations are identified by Organization_ID and store details including name, address (street, city), contact person, and phone number.
* Events require an Event_ID and contain information about title, description, start date, end date, and capacity.
* Venues are tracked with Venue_ID, name, address (street, city, state, zip code), and maximum capacity.
* Speakers in the system are assigned Speaker_ID and maintain their name, bio, contact information (email, phone), and area of expertise.
* Sponsoring companies receive Sponsor_ID and record their company name, contact person, contact information (email, phone), and logo.
* System users are given User_ID and must provide name, email, phone number, and address.

### Relationships and Business Rules:

* Each organization can manage multiple events, while every event must belong to exactly one organizing.
* All events must take place at a single venue, though venues may host numerous events.
* Multiple speakers can participate in any given event, with speakers able to present at various events throughout the year. The system tracks presentation titles and time slots for every speaker engagement.
* Sponsorship arrangements allow multiple sponsors per event, and sponsors may support multiple events simultaneously. Sponsorship levels (Gold, Silver, Bronze) and monetary contributions are recorded for every sponsorship agreement.
* Users have the flexibility to attend multiple events, and events can accommodate multiple attendees based on capacity. Registration dates and attendance status are maintained for all event participants.
* One designated organizer from the managing organization must serve as event manager, with the possibility of managing multiple events.
* Venue records must include detailed facilities information such as available rooms, equipment, and room-specific capacity limits.
* Financial tracking requires recording all event-related transactions (ticket sales, sponsorship payments) with Transaction_ID, date, amount, and transaction type.
