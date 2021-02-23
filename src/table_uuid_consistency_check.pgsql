SELECT COUNT(*) as core_count FROM core;

SELECT COUNT(*) as demand_count  FROM demand LIMIT 5;

SELECT COUNT(*) as detritus_count  FROM detritus LIMIT 5;

SELECT COUNT(*) as identifiers_count  FROM identifiers LIMIT 5;

SELECT COUNT(*) as combo FROM core
JOIN demand ON core.uuid = demand.uuid 
JOIN detritus ON core.uuid = detritus.uuid
JOIN identifiers ON core.uuid = identifiers.uuid;


   
 

    

