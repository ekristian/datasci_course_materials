drop view if exists dc_taxes;

create view dc_taxes as
--select * from frequency
--union
select 'q' as docid, 'washington' as term, 1 as count
union
select 'q' as docid, 'taxes' as term, 1 as count
union
select 'q' as docid, 'treasury' as term, 1 as count
;

.output part_i.txt
select max(sim) as max_sim
from (
select 
    D.docid, sum(D.count * DT.count) as sim
from
    frequency as D
join
    dc_taxes as DT
on
    D.term = DT.term
where
    dt.docid = 'q'
group by
    d.docid
);

.output stdout
