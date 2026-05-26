create table doctor 
( 
doc_id VARCHAR (4) NOT NULL, 
doc_name VARCHAR (30),
doc_title VARCHAR (30), 
doc_sex VARCHAR (2), 
doc_telephone VARCHAR (11), 
dept_id VARCHAR (4), 
restroom_id VARCHAR (4), 
primary key (doc_id), 
foreign key (dept_id) references section (dept_id), 
foreign key (restroom_id) references restroom(restroom_id) 
);

create table patient
(
pati_id varchar(4) not null,
pati_name varchar(30),
pati_birth date,
pati_telephone varchar(11),
chief_id varchar(4),
blood varchar(4),
primary key(pati_id),
foreign key(chief_id) references doctor(doc_id)
);