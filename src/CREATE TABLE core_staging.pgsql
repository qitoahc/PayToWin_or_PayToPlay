CREATE TABLE core_staging (
    "uuid" TEXT,
    "name" TEXT, 
    "rarity" TEXT, 
    "setCode" TEXT,
    "types" TEXT, 
    "keywords" TEXT, 
    "colorIdentity" TEXT, 
    "colors" TEXT, 
    "convertedManaCost" TEXT, 
    "loyalty" TEXT, 
    "manaCost" TEXT, 
    "subtypes" TEXT,
    "supertypes" TEXT, 
    "text" TEXT, 
    "type" TEXT, 
    "power" TEXT, 
    "toughness" TEXT
);

CREATE TABLE demand_staging (
    "uuid" TEXT,
    "edhrecRank" TEXT 
);

CREATE TABLE identifiers_staging (
    uuid TEXT,
    "identifiers" TEXT 
);

CREATE TABLE detritus_staging (
    uuid TEXT,
    "number" TEXT, 
    "frameEffects" TEXT, 
    "artist" TEXT, 
    "availability" TEXT, 
    "borderColor" TEXT, 
    "foreignData" TEXT, 
    "frameVersion" TEXT, 
    "hasFoil" TEXT, 
    "hasNonFoil" TEXT, 
    "isReprint" TEXT, 
    "layout" TEXT, 
    "leadershipSkills" TEXT, 
    "legalities" TEXT, 
    "printings" TEXT, 
    "purchaseUrls" TEXT, 
    "rulings" TEXT, 
    "variations" TEXT, 
    "flavorText" TEXT, 
    "isPromo" TEXT, 
    "isStarter" TEXT, 
    "promoTypes" TEXT, 
    "watermark" TEXT
);


    