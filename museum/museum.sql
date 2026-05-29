create table museum_master
(
an_id int,
antiq_name varchar(50),
doreg varchar(8),
museum_condition varchar(50),
source varchar(50),
estimated_cost int,
con_dept varchar(50),
con_person varchar(50),
mu_mem_id int,
mu_libmem_id int,
tkt_no int,
tkt_type varchar(10),
constraint anidpk primary key(an_id)
);

create table pottery
(
an_id int,
pottery_name varchar(50),
age int,
doreg varchar(8),
color varchar(10),
pottery_condition varchar(5),
est_cost int,
fut_life int,
type varchar(6),
source varchar(10),
con_person varchar(50),
constraint anidpk2 primary key(an_id)
);

create table stone
(
an_id int,
stone_name varchar(50),
doreg varchar(8),
color_of_stone varchar(10),
est_cost int,
weight int,
source varchar(10),
con_person varchar(50),
constraint anidpk3 primary key(an_id)

);

create table textiles
(
an_id int,
textile_name varchar(10),
doreg  varchar(8),
color  varchar(10),
length int,
fab_material  varchar(10),
source  varchar(10),
bidding  varchar(50),
textile_condition  varchar(6),
rel_period  varchar(20),
rec_from  varchar(20),
constraint anidpk4 primary key(an_id)
);

create table jewellery
(
an_id int,
jewellery_name varchar(10),
doreg varchar(8),
weight int,
material varchar(10),
source varchar(10),
est_cost int,
rel_period varchar(20),
rec_from varchar(20),
constraint anidpk5 primary key(an_id)
);

create table sculpture
(
an_id int,
name varchar(10),
topic varchar(50),
color varchar(10),
weight int,
height int,
width int,
artist_name varchar(10),
sculpture_condition varchar(6),
rel_period varchar(20),
con_dept varchar(50),
con_person varchar(50),
constraint anidpk6 primary key(an_id)
);

create table basic_tkt
(
s_no int,
no_of_adult int,
amt_one_ad_tkt int,
no_of_children int,
amt_one_ch_tkt int,
tot_amt int,
date_of_visit varchar(8),
time varchar(6),
constraint snopk7 primary key(s_no)
);

create table drama_tkt
(
s_no int,
drama_name varchar(10),
hall_no int,
no_of_children int,
amt_one_ch_tkt int,
no_of_adult int,
amt_one_ad_tkt int,
date_of_visit varchar(8),
time varchar(6),
seat_no int,
tot_amt int,
constraint snopk8 primary key(s_no)
);

create table combo_tkt
(
s_no int,
drama_name varchar(10),
hall_no int,
no_of_children int,
amt_one_ch_tkt int,
no_of_adult int,
amt_one_ad_tkt int,
date_of_visit varchar(8),
time varchar(6),
seat_no int,
tot_amt int,
constraint snopk9 primary key(s_no)
);

create table library_book_entry
(
s_no int,
b_id int,
book_name varchar(20),
author varchar(20),
publication varchar(20),
date_of_purchase varchar(8),
date_of_entry varchar(8),
amt int,
purchased_from varchar(10),
con_dept varchar(20),
constraint snopk10 primary key(s_no)
);

create table library_book_issue
(
s_no int,
b_id int,
issued_book_name varchar(20),
author varchar(20),
issued_to varchar(20),
mu_libmem_id int,
date_of_issue varchar(8),
rec_back_date varchar(9),
revd_back varchar(1),
penalty int,
book_condition varchar(10),
constraint snopk11 primary key(s_no)
);

create table library_lost_book
(
s_no int,
b_id int,
book_name varchar(20),
author varchar(20),
publication varchar(20),
price int,
constraint snopk12 primary key(s_no)
);

create table library_cds_entry
(
s_no int,
cd_id int,
cd_name varchar(20),
type varchar(20),
date_of_purchase varchar(8),
date_of_entry varchar(8),
amt int,
purchased_from varchar(10),
con_dept varchar(20),
constraint snopk13 primary key(s_no)
);

create table library_cd_issue
(
s_no int,
cd_id int,
cd_name varchar(20),
type varchar(20),
issued_to varchar(20),
mu_libmem_id int,
date_of_issue varchar(8),
rec_back_date varchar(9),
revd_back varchar(1),
penalty int,
cd_condition varchar(10),
constraint snopk14 primary key(s_no)
);

create table library_lost_cd
(
s_no int,
cd_id int,
cd_name varchar(20),
type varchar(20),
price int,
constraint snopk15 primary key(s_no)
);

create table library_membership
(
mu_libmem_id int,
mem_name varchar(50),
address varchar(20),
age int,
sex varchar(1),
phone_no int,
amt_of_mem_card int,
validity varchar(8),
membership_for varchar(5),
constraint mlibpk primary key(mu_libmem_id)
);

create table login
(
uname varchar(15),
pass varchar(15)
);

insert into login values('m','m');

create table museum_membership
(
mu_mem_id int,
mem_name varchar(50),
address varchar(20),
age int,
sex varchar(1),
phone_no int,
amt_of_mem_card int,
validity varchar(8),
membership_by varchar(10),
constraint mmpk primary key(mu_mem_id)
);

create table museum_exhibition
(
s_no int,
exhi_name varchar(10),
sub varchar(20),
hall_no int,
exhi_incharge varchar(20),
no_of_days int,
date_from varchar(8),
date_to varchar(8),
constraint snopk16 primary key(s_no)
);

