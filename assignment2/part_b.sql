-- (b) select project: Write a SQL statement that is equivalent to the 
-- following relational algebra expression.
--
-- πterm(σdocid=10398_txt_earn and count=1(frequency))
--
-- What to turn in: Run your query against your local database and determine 
-- the number of records returned. Save that value in a file part_b.txt and 
-- upload the file as your answer.
select count(1)
from (
select
    term
from
    frequency
where
    docid='10398_txt_earn'
    and count=1
)
;
.output stdout
