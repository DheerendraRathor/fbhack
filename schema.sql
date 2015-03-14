drop table  IF EXISTS  user;
drop table  IF EXISTS  status;
drop table  IF EXISTS  review;
drop table  IF EXISTS volunteer;

create table user (
	user_id serial primary key ,
	fbid varchar(200) unique key not null ,
	name varchar (300) ,
	email varchar (300) 
);

create table status (
	status_id serial primary key ,
	latitude real ,
	longitude real ,
	user_id integer ,
	comment text  ,
	rate real,
	locality varchar(200) ,
	city varchar(200) ,
	state varchar(200) ,
	country varchar(200) 
);

create table review (
	review_id serial primary key,
	user_id integer unique key,
	rate integer,
	comment text
);

create table volunteer (
	status_id integer,
	user_id integer ,
	primary key (status_id , user_id)
);