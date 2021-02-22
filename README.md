# PayToWin_or_PayToPlay
An exploration into Magic: The Gathering and the truthiness of the 'whoever dumps the most money into a deck, always wins' perspective

Overview: As someone who enjoys MTG socially/casually I’ve often heard people talk about enjoying it as well but ultimately leaving because it’s just a “whoever dumps the most cash has the best deck and thus always wins”.  The ultimate goal of this project is to explore this perspective.

## Analysis
-  Key MVP:
   - Avg. price per World Title Competitor Deck (16 entrants) vs. Avg. price for ‘6-win streak’ decks from MTG Arena players in top ‘unranked’ tiers
   - Could also do avg. price per card across them - have to think about what impacts to power the two approaches could have (if any)
     - Hypothesis is that World Champ deck costs are equal or less than more casual player top decks
   - Correlation between price and card rank on popular MTG forum
   - Card price by rarity category
 - Secondary/supporting analyses:
    Deck mix comparisons between two groups (World Title / Arena)
    Card types/mix and colors
    Card price by release set across 6 sets included in tournament rules
 - MVP+
    Explore concept of ‘power’ of a card 
    Starting with pulling out categories of skills/effects (some are explicitly identified in data set, some will require mining text fields from cards)
    Explore price and power correlations
    Individual elements of power vs. price, as well as ‘count of elements’ and price
    Develop way to identify ‘price efficiency’ of cards

## Data
 - 6-win streak decks, platinum or above on Arena, current
    https://magic.gg/decklists/traditional-standard-ranked-decklists-february-8-2021
    MVP - download representative sample (16 to match tournament decks) of deck lists to match World Title Deck 
    MVP+ - leverage screen scraping tools to automatically navigate deck downloading across all posted 
 - Top 16 world champion contenders
    https://magic.gg/events/magic-world-championship-xxvi#top-8
 - Comprehensive card data extracts
    https://mtgjson.com/downloads/all-files/
    Card lists (essentially everything visible on the card + limited external data such as the rank from a populare MTG forum)
    For purposes of pipeline demonstration, plan to download files per release set and then build total library for tournament play across the ~6 releases included
 - Prices for cards
    Data set contains more than one pricing source
    MVP - look at price only from one source
    MVP+ - explore price variation by storefront and/or use aggregate pricing
