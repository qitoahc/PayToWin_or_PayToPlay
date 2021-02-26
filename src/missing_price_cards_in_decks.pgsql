SELECT core.uuid, name
FROM core
LEFT JOIN fixed_prices ON fixed_prices.uuid = core.uuid
JOIN decklists ON decklists.uuid = core.uuid
WHERE fixed_prices.price is Null
GROUP BY name, core.uuid
ORDER BY name ASC