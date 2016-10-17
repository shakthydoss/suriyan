use suriyan;

drop table usr;
drop table usr_role;
drop table role;
drop table tag;
drop table tp;

create table usr(
uid varchar(40) not null,
username varchar(40) not null,
email varchar(255) null default null,
is_active char(1) default 'y',
updated_date timestamp default current_timestamp,
updated_by varchar(40) not null,
UNIQUE(username),
primary key (uid)
);


create table usr_role(
id int AUTO_INCREMENT,
uid varchar(40) not null,
role_id int not null,
updated_date timestamp default current_timestamp,
updated_by varchar(40) not null,
primary key (id)
);

create table role(
role_id int AUTO_INCREMENT,
name varchar(20),
description varchar(255) not null,
updated_date timestamp default current_timestamp,
updated_by varchar(40) not null,
UNIQUE(name),
primary key(role_id)
);

create table tag(
tag_id int AUTO_INCREMENT,
name varchar(20),
description varchar(255) not null,
is_active char(1) default 'y',
updated_date timestamp default current_timestamp,
updated_by varchar(40) not null,
UNIQUE(name),
primary key(tag_id)
);

create table tp(
tpid varchar(40),
name varchar(255),
updated_date timestamp default current_timestamp,
updated_by varchar(40) not null,
UNIQUE(name),
primary key(tpid)
);

# Adding default user
insert into usr(uid,username,updated_by) values ('1','admin','system');

# Adding default roles
insert into role (name,description,updated_by) values ('admin','admin','system');
insert into role (name,description,updated_by) values ('tutor','tutor','system');
insert into role (name,description,updated_by) values ('student','student','system');

# Adding role to default user
insert into usr_role(uid,role_id,updated_by) values ('1', '1', 'system');


