-- Active: 1730628214635@@localhost@3306@events_management_system
-- get the payment methods
select
	distinct payment_method
from user_attend;


-- get the expertise of speakers
select
	distinct expertise
from speaker;


-- retrieve the full name of speaker and its expertise
select
	concat(first_name, " ", last_name) as "Full Name",
    expertise
from speaker;

-- users who attended in at least one event
select
	user.first_name
from user
where user.user_id in (
	select 
		distinct user_id
	from user_attend
);


-- number of users which never attended any event
select
	count(user.user_id)
from user
where user.user_id not in (
	select
		distinct user_id
	from user_attend
);

-- number of tickets sold for each event and its total revenue
select
	event.title,
	sum(ticket_price) as "total price",
    count(ticket_price) as "number of tickets"
from event
join user_attend on event.event_id = user_attend.event_id
group by event.event_id
order by sum(ticket_price) desc;

-- each event with number of its attendees
select
	event.title,
    count(user_id)
from event
join user_attend on event.event_id = user_attend.event_id
group by event.event_id
order by count(user_id) desc;

-- the maximum attendees event
select
	event.title
from event
join user_attend on user_attend.event_id = event.event_id
group by event.event_id
having count(user_id) = (
	select
		max(count_user)
	from (
		select
			count(user_id) as count_user
		from event
		join user_attend on event.event_id = user_attend.event_id
		group by event.event_id
		order by count(user_id) desc
	) as f
);


-- sum of payments using each method
select
	payment_method,
    sum(ticket_price),
    count(user_id)
from user_attend
group by payment_method;


-- count accepted and rejected people for each event
select
	event.title,
    count(user_attend.user_id),
    sum(case when user_attend.status = 'accepted' then 1 else 0 end) as "Accepted",
    sum(case when user_attend.status = 'rejected' then 1 else 0 end) as "Rejected"
from event
join user_attend on event.event_id = user_attend.event_id
group by event.event_id;

-- show the percetage of males and females in each event
select
	event.title,
    count(user_attend.user_id) as "Total Attendees",
    sum(case when user.gender = 'male' then 1 else 0 end) as "Males",
    sum(case when user.gender = 'female' then 1 else 0 end) as "Females",
	round(sum(case when user.gender = 'male' then 1 else 0 end) / count(user_attend.user_id) * 100, 2) as "Males Perecentage",
	round(sum(case when user.gender = 'female' then 1 else 0 end) / count(user_attend.user_id) * 100, 2) as "Females Percentage"
from event 
join user_attend on event.event_id = user_attend.event_id
join user on user.user_id = user_attend.user_id
group by event.event_id;


-- number of users who registered after the start date for each event
select
	event.title,
	count(user_id) as "number of users"
from user_attend
join event on user_attend.event_id = event.event_id and
	user_attend.date > event.start_date
group by event.event_id
order by count(user_id) desc;