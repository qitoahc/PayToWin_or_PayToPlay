WITH deck_card_prices AS (
    SELECT card_count, sideboard, deckname, core.name, price
    FROM decklists
    JOIN core ON decklists.uuid = core.uuid
    LEFT JOIN fixed_prices ON decklists.uuid = fixed_prices.uuid
    )

SELECT deckname, SUM(card_count * price), SUM(card_count)
FROM deck_card_prices
WHERE deck_card_prices.sideboard = FALSE
GROUP BY deckname;


