create table IF NOT EXISTS TA (
    row_num int,
    col_num int,
    value int
);

create table if not exists TB as
select * from ta;

insert into TB values(1,0,-2);
insert into TB values(0,1, 3);
insert into TB values(1,1,-1);
insert into TB values(2,1, 4);

insert into TA values(0,0,1);
insert into TA values(0,2,-2);
insert into TA values(1,1,3);
insert into TA values(1,2,-1);
