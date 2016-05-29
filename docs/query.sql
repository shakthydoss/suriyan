create table urs(
uid varchar(20) not null, 
name varchar(40) not null,
email varchar(255) not null,
is_active char(1) default 'y',
created_date timestamp default current_timestamp,
UNIQUE(email),
primary key (uid)
);
 
create table secret(
uid varchar(20) not null, 
secret varchar(40) not null,
created_date timestamp default current_timestamp,
primary key (uid)
);