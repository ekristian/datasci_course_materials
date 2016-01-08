-- Matrix multiplication
--
drop table product;

create temp table product as
select 
    row_num,
    col_num,
    sum(product) as value
from (
select 
    a.row_num,
    b.col_num,
    (a.value * b.value) as product
from 
    a
inner join
    b
on
    (a.col_num = b.row_num)
)
group by
    row_num, col_num
order by
    row_num, col_num
;
.output part_g.txt
select value from product where row_num=2 and col_num=3;
.output stdout
