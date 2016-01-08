-- similarity matrix: 
-- Wtire a quert to compute the similarity of matrix DD^T
-- Hint:
-- Join on columns to columns instead of columns to rows.
--
-- We are only concerned with documents 10080_txt_crude and 17035_txt_earn
--
.output part_h.txt
select sum(f1.count * f2.count)
from 
    Frequency as f1
join
    Frequency as f2
on
    f1.term = f2.term
where 
    f1.docid='10080_txt_crude' 
    and f2.docid='17035_txt_earn'
;
.output stdout
