-- (f) two words: 
-- Write a SQL statement to count the number of unique documents that contain
-- both the word 'transactions' and the word 'world'.
--
-- Hint: Find the docs that contain one word and the docs that contain the other word
--       separately, then find the intersection.
--
-- What to turn in: 
-- Run your query against your local database and determine the number of
-- records returned as described above. Save that value in a file part_f.txt
-- and upload the file as your answer.
--
-- Solution: 
-- 1. select all documents where term in ('transactions', 'world')
-- 2. group R1 by docid, count(1) as term_count having term_count = 2
-- 3. count the number of rows returned.
--      OR
-- Find the intersection as hinted above.
--
--  My Way - in retrospect, not very elegant
-- although it could easily handle any number of terms without
--  needing to add multiple joins
--

-- select count(1)
-- from (
-- select
--     docid,
--     count(1) as term_count
-- from
-- (
--     select
--         docid,
--         term
--     from
--         frequency
--     where
--         term = 'transactions' 
--         or term = 'world'
-- )
-- group by
--     docid
-- having
--     count(1) > 1
-- )
-- ;

-- The suggested way.
--
.output part_f.txt
select count(1)
from
    (select distinct docid from frequency where term='transactions') as t
inner join
    (select distinct docid from frequency where term='world') as w
on
    t.docid = w.docid
;
.output stdout
