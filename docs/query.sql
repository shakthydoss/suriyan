use suriyan;

drop table usr;
drop table secret;
drop table usr_role;
drop table role;

create table usr(
uid varchar(20) not null, 
username varchar(40) not null,
email varchar(255) null default null,
is_active char(1) default 'y',
updated_date timestamp default current_timestamp,
updated_by varchar(20) not null,
UNIQUE(username),
primary key (uid)
);
 
create table secret(
uid varchar(20), 
secret varchar(40) not null,
updated_date timestamp default current_timestamp,
updated_by varchar(20) not null,
primary key (uid)
);

create table usr_role(
id int AUTO_INCREMENT,
uid varchar(20) not null, 
role_id int not null,
updated_date timestamp default current_timestamp,
updated_by varchar(20) not null,
primary key (id)
);

create table role(
role_id int AUTO_INCREMENT,
name varchar(20), 
description varchar(20) not null, 
updated_date timestamp default current_timestamp,
updated_by varchar(20) not null,
UNIQUE(name),
primary key(role_id)
);

create table tag(
tag_id int AUTO_INCREMENT,
name varchar(20), 
description varchar(20) not null, 
is_active char(1) default 'y',
updated_date timestamp default current_timestamp,
updated_by varchar(20) not null,
UNIQUE(name),
primary key(tag_id)
);

create table tp(
tpid varchar(30),
name varchar(255),
updated_date timestamp default current_timestamp,
updated_by varchar(20) not null,
UNIQUE(name),
primary key(tpid)
);

# Adding default user
insert into usr(uid,username,email,updated_by) values ("1","admin",null, "sys");
insert into secret(uid,secret,updated_by) values("1","Reset123", "sys");

# Adding default rule
insert into role (name,description,updated_by) values ('admin','admin','system');
insert into role (name,description,updated_by) values ('tutor','tutor','system');
insert into role (name,description,updated_by) values ('student','student','system');

# Adding role to default user
insert into usr_role(uid,role_id,updated_by) values ("1", "1", "sys");


