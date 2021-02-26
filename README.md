# Magic: The Gathering -- Pay To Win or Pay To Play?

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/banner.png)

# Table of Contents
1. [Intro and Motivation](#intro-and-motivation)
2. [Magic Overview](#magic-overview)
3. [Areas of exploration](#areas-of-exploration)
4. [Data Sources](#data-sources)
5. [Data Processing and Cleaning](#data-processing-and-cleaning)
6. [Visualization](#visualization)
7. [Testing the Hypothesis](#testing-the-hypothesis)
8. [Conclusion](#conclusion)
9. [Photo and Data Credits](#photo-and-data-credits)

## **Intro and Motivation**: 
As someone who enjoys Magic: The Gathering (MTG) as a causal activity with friends, I’ve often heard people talk about enjoying it, but feeling like it's a money pit and whoever spends the most on a given deck always wins.  On the flip side, I've both built and seen decks that leverage low cost cards in creative ways to achieve a solid win rate.  So I thought...why not take a stab at learning more about if there's truth in the statement that it's just a 'pay to win' game.

## **Magic Overview**:
From Wikipedia, the free encyclopedia:
  - "Magic: The Gathering (colloquially known as Magic or MTG) is a collectible and digital collectible card game created by Richard Garfield.[1] Released in 1993 by Wizards of the Coast (now a subsidiary of Hasbro), Magic was the first trading card game and has approximately thirty-five million players as of December 2018,[2][3][4] and over twenty billion Magic cards produced in the period from 2008 to 2016, during which time it grew in popularity.[5][6]"

  - "A player in Magic takes the role of a Planeswalker, doing battle with other players as Planeswalkers by casting spells, using artifacts, and summoning creatures as depicted on individual cards drawn from their individual decks. A player defeats their opponents typically, but not always, by draining them of their starting life total. Although the original concept of the game drew heavily from the motifs of traditional fantasy role-playing games such as Dungeons & Dragons, the gameplay bears little similarity to pencil-and-paper adventure games, while simultaneously having substantially more cards and more complex rules than many other card games. "

MTG produces four sets of cards annually.  Each set consists of approximately 350 cards.  There is a category of deck creation called 'standard' that limits players to the most recent 6 sets released.  This 'standard' format is the focus of this analysis as that's the type of competition that each of the types of players described above participate in.

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/arean_game_play.png)

## **Areas of Exploration**:
As touched on in the introduction, my primary goal for the first phase of this project is to be able to compare the deck costs for the top 16 MTG players in the world against a collection of decks from 'skilled amateurs' of the game.  Ultimately my hypothesis is that there is not a stastitically significant difference in the costs between the two groups of decks.

## **Data Sources**:
There were four distinct categories of data sets across two primary sources:
 - Skilled Amateur Deck Lists
    - Wizards of the Coast publish 'featured' deck lists from their online gaming platform, The Arena.  These decks are selected based on the criteria that the players are playing at a platinum tier or higher on The Arena and the decks have achieved a 6-game win streak at that tier.  28 decks were available at the time of this projec, available as individual text file downloads.
    - https://magic.gg/decklists/traditional-standard-ranked-decklists-february-8-2021
 - Top 16 World Champion Contenders Deck Lists
    - Wizards of the Coast recently published the deck lists from the 2020 World Champion tournament, available through individual text file downloads.
    - https://magic.gg/events/magic-world-championship-xxvi#top-8
 - Comprehensive Card Detail Data
    - There is a site (mtgjson.com) that is managed by a group of dedicated individuals that collects and aggregates comprehensive MTG card data and then publishes regularly updated JSON files.  For the purposes of this project, files for eight individual sets were downloaded and included in the processing and analyzing steps to align with the sets included in standard competition, which was the type of competition the selected deck lists participated in.  The site maintains a variety of other download options in addition to set-specific.  Each set file contains all of the cards for that set including comprehensive data from the card such as: name, card type, casting costs, every text element on the card, language translations, etc.  Each card also has a UUID assigned.
    - https://mtgjson.com/downloads/all-files/
 - Card Prices
    - MTGJSON.com maintains a separate data extract that contains roughly two months (if applicable) of pricing data for all cards across multiple sources.  For each source, there can also be multiple prices available depending on the format of the card (online, paper, etc.) and 'finish' (foil, normal, etc.).  Each card contains a UUID and the data is available through a single large JSON file.
    - https://mtgjson.com/downloads/all-files/

## **Data Processing, Cleaning, and Storage**:
Given the data sets obtained, the primary objective, and a desire to be able to continue to build on this project, I decided that building a data processing pipeline that incorporated storage within a database would be a critical part of this first phase.  Not only would this enable 'ongoing' data processing, it would also give a solid data architecture to facilitate the current and future analyses as I'd be able to pull sets for analysis scaled to the questions at hand.

The diagram below provides a visual summary of what was built for this first phase and gives a high-level view into the PostgreSQL structure used.  Highlights around each file type are provided below along with the appropriate links to the python notebooks used to establish this first 'manual-powered' phase.    

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/MTG_flow_erd.png)

- Card component data
  - This was the first data set that was tackled, and as such the took the most time.  This was the data set where I developed a basic approach for digging into a large and highly nested JSON format.  While the source website provided some basic information, it was unclear just how some of the data would be presented and translated from the cards.  Additionally, the presence of ~10 translations resulted in large swaths (literally rows and rows per card of screen-width text in other languages I have no understanding of) of hard to digest information.  Ultimately I was able to work through to the actual card-specific data, and from there explore the formats and types of data to build the table schema to start working with (as roughly shown in the diagram above).  To give an example of the variation that can occur, please see the image below that puts a sample card from each of the 5 main types (artifact, planeswalker, spell - instant being just one of a handful of subtypes, land, and creature),  side by side (**foreshadowing...***) 

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/sample_card_types.png)
  - As you may guess... this variation resulted in most of the data needing to be of a string or collection of strings data type.  Additionally, there turned out to be a very slight variation in data elements provided between the sets requiring me to add a column or two with each run to accomodate the full 'all-set' data.   
  - Ultimately though, the data process was somewhat straightforward once I had the schema and understanding, and was handled by splitting the data into four dataframes for each of the applicable tables (card data, set data, and detritus table) and then inserting into the tables created for the purpose in my PostgreSQL DB that I'd created.  
  - THe detritus table was a design i developed to enable me to ingest all of the data in the files, maintain linkage via the UUID, but keep the core tables and data for my analysis as lean and normalized as possible.  In the future, the data is there and can be unpacked as needed.  The biggest issue was with some of the nested collections I had to develop a process for converting them to strings so that the table would accept the data.
  - The [notebook](insert link) has been cleaned up as far as leveraging helper functions stored in an importable .py [file](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/src/mtg_helpers.py), but has been left with examples of the data and research conducted for those who would look to see more specifics.

- Card prices
  - This data set went much faster than the card data, in part because I better understood how to work through JSON files and had helper functions established to facilitate sql connections, prepping for load, and inserting into the DB.  Additionally, this data set was completely housed in one file, so only required one load.
  - As stated the pricing data had prices from three different sources (one european, two US), three card formats (Arena Online, MTG Online, and paper), and a few other variations (foil cards vs non-foil).  Research indicated there was variation across the sources both in completeness of data and actual card price.  For the sake of moving forward with phase 1, I opted to go with the 'standard' approach of taking a single source (US-based CardKingdom, HQ'ed in my own Seattle neighborhood!) for paper, non-foil prices.  From what I could tell, this would give me the best total price coverage and I opted to avoid blending or mixing/matching as ultimately I would only have 168 cards without prices out of a total of over 3500 cards.
  - Additionally, because in general cards become less valuable the further from their release date they are (because they rotate out of standard amongst other reasons), I took the 'oldest' price value present per card to better approximate the prices when they were 'fresh' and in demand so as to avoid any skewing towards decks made out of older cards.

- Decklists

## **Extraction and Visualization**:

## **Testing the Hypothesis**:

## **Close-out**:
  something about how while yes, the world champ-level players do have more costly decks than skilled amateurs... the distributions are such that it's not an overwhelming
  
## Analysis:
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
    
    
```bash
'Adults (ages 15+) living with HIV'
'Age at first marriage, female'
'Wanted fertility rate (births per woman)'
```
https://en.wikipedia.org/wiki/Magic:_The_Gathering
