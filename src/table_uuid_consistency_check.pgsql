SELECT COUNT(*) FROM core;

SELECT COUNT(*) FROM demand LIMIT 5;

SELECT COUNT(*) FROM detritus LIMIT 5;

SELECT COUNT(*) FROM identifiers LIMIT 5;

SELECT COUNT(*) FROM core
JOIN demand ON core.uuid = demand.uuid 
JOIN detritus ON core.uuid = detritus.uuid
JOIN identifiers ON core.uuid = identifiers.uuid;


   
 

    

