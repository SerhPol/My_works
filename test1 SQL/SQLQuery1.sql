create database game;

use game;

create table metric (
n_records int,
eventName varchar(20),
eventTimestamp date,
gaUserStartDate date,
matchResult varchar(5),
platform varchar(5),
userID varchar(25) not null
)
