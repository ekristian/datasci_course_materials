select count(1) 
from 
    (
        select distinct 
            docid 
        from 
            frequency 
        where 
            term='law' or term='legal'
    )
;
.output stdout
