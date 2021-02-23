WITH newestsetdate AS (
    SELECT name, MAX(setreleasedate) as max_date
    FROM core
    JOIN setdetails ON "setCode" = "setcode"
    GROUP BY name
    )
    ,
    newestset AS (
    SELECT name, setcode
    FROM newestsetdate
    JOIN setdetails ON newestsetdate.max_date = setdetails.setreleasedate
    )
    
SELECT core.uuid, newestset.name
FROM core
INNER JOIN newestset ON newestset.name = core.name AND newestset.setcode = core."setCode";
