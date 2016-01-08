-- (e) big documents Write a SQL statement to find all documents that have more
-- than 300 total terms, including duplicate terms. 
--
-- Hint: You can use the HAVING clause, or you can use a nested query. 
-- Another hint: Remember that the count column contains the term frequencies,
-- and you want to consider duplicates. 
-- (docid, term_count)
-- 
-- Solution: sum the count column by docid to get the total number of terms
--           per docid. Use the HAVING clause to select those docid value
--           with more that 300 terms. Duplicate or otherwise.
--
-- What to turn in:  The count of records returned.
.output part_e.txt
select count(1) 
from (
select 
    docid, 
    count(1) as total_terms
from
    frequency
group by
    docid
having
    count(1) > 300
)
;
.output stdout
