CREATE TABLE core (
    uuid UUID PRIMARY KEY,
    "name" TEXT, 
    "rarity" TEXT, 
    "setCode" TEXT,
    "types" TEXT[], 
    "keywords" TEXT[], 
    "colorIdentity" TEXT[], 
    "colors" TEXT[], 
    "convertedManaCost" DOUBLE PRECISION, 
    "loyalty" TEXT, 
    "manaCost" TEXT, 
    "subtypes" TEXT[],
    "supertypes" TEXT[], 
    "text" TEXT, 
    "type" TEXT, 
    "power" TEXT, 
    "toughness" TEXT
);

CREATE TABLE demand (
    uuid UUID PRIMARY KEY,
    "edhrecRank" SMALLINT 
);

CREATE TABLE identifiers (
    uuid UUID PRIMARY KEY,
    "identifiers" TEXT 
);

CREATE TABLE detritus (
    uuid UUID PRIMARY KEY,
    "number" TEXT, 
    "frameEffects" TEXT[], 
    "artist" TEXT, 
    "availability" TEXT[], 
    "borderColor" TEXT, 
    "foreignData" TEXT, 
    "frameVersion" TEXT, 
    "hasFoil" BOOLEAN, 
    "hasNonFoil" BOOLEAN, 
    "isReprint" BOOLEAN, 
    "layout" TEXT, 
    "leadershipSkills" TEXT, 
    "legalities" TEXT, 
    "printings" TEXT[], 
    "purchaseUrls" TEXT, 
    "rulings" TEXT, 
    "variations" TEXT[], 
    "flavorText" TEXT, 
    "isPromo" BOOLEAN, 
    "isStarter" BOOLEAN, 
    "promoTypes" TEXT[], 
    "watermark" TEXT, 
    "originalText" TEXT,
    "originalType" TEXT
);

CREATE TABLE decklists (
    uuid UUID PRIMARY KEY,
    "card_count" SMALLINT,
    "sideboard" BOOLEAN,
    "deckname" TEXT
);



    