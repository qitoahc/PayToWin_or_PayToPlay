SELECT decklists.deckname, core.uuid, core.name, decklists.card_count, decklists.sideboard, core.rarity, core."setCode", core."keywords", core."convertedManaCost", core.type, core.power, core.toughness, core.subtypes, core.supertypes, setdetails.setname, setdetails.setreleasedate, fixed_prices.price, fixed_prices."price_date"
FROM core
LEFT JOIN fixed_prices ON core.uuid = fixed_prices.uuid
JOIN setdetails  ON core."setCode" = setdetails.setcode
JOIN decklists ON core.uuid = decklists.uuid