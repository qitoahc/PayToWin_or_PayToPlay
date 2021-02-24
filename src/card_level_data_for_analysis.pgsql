SELECT core.uuid, core.name, core.rarity, core."setCode", core."keywords", core."convertedManaCost", core.type, core.power, core.toughness, core.subtypes, core.supertypes, setdetails.setname, setdetails.setreleasedate, fixed_prices.price, fixed_prices."price_date"
FROM core
JOIN fixed_prices ON core.uuid = fixed_prices.uuid
JOIN setdetails  ON core."setCode" = setdetails.setcode
