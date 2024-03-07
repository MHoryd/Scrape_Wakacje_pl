CREATE TABLE public.destinations (
	id serial4 NOT NULL,
	country varchar(60) NOT NULL,
	country_label varchar(60) NOT NULL,
	CONSTRAINT destinations_country_key UNIQUE (country),
	CONSTRAINT destinations_country_label_key UNIQUE (country_label),
	CONSTRAINT destinations_pkey PRIMARY KEY (id)
)

CREATE TABLE public.search_param (
	id serial4 NOT NULL,
	country varchar(60) NOT NULL,
	date_from timestamp NOT NULL,
	date_to timestamp NOT NULL,
	stay_length varchar(60) NOT NULL,
	stars varchar(60) NOT NULL,
	max_price varchar NOT NULL,
	transportation varchar(60) NOT NULL,
	amenities varchar(60) NOT NULL,
	departure_city varchar(60) NOT NULL,
	rating varchar(100) NOT null,
	CONSTRAINT search_param_pkey PRIMARY KEY (id)
)


insert into public.search_param (country, date_from,date_to,stay_length,stars,max_price,transportation,amenities,
departure_city,rating)
values
('hiszpania','2024-03-04 00:00:00.000','2024-03-11 00:00:00.000',
'1-10','2-gwiazdkowe',10000,'samolotem','all-inclusive','z-warszawy','ocena-9')