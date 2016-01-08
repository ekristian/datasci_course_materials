-- (a) select: Write a query that is equivalent to the following relational
-- algebra expression.
-- σdocid=10398_txt_earn(frequency)
--
-- What to turn in: 
-- Run your query against your local database and determine the number of
-- records returned. Save that value in a file part_a.txt and upload the file
-- as your answer.
select 
    count(1) 
from 
    (select * from frequency where docid='10398_txt_earn')
;
.output stdout
