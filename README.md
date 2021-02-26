# Magic: The Gathering -- Pay To Win or Pay To Play?

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/banner.png)

# Table of Contents
1. [Intro and Motivation](#intro-and-motivation)
2. [Magic Overview](#magic-overview)
3. [Areas of exploration](#areas-of-exploration)
4. [Data Sources](#data-sources)
5. [Data Processing, Cleaning, and Storage](#data-processing,-cleaning,-and-storage)
6. [Extraction and Visualization](#extraction-and-visualization)
7. [Testing the Hypothesis](#testing-the-hypothesis)
8. [Light Featurization and More Visualization](#light-featurization-and-more-visualization)
9. [Close out](#close-out)
10.[Credits](#credits)

## **Intro and Motivation**: 
As someone who enjoys Magic: The Gathering (MTG) as a causal activity with friends, I’ve often heard people talk about enjoying it, but feeling like it's a money pit and whoever spends the most on a given deck always wins.  On the flip side, I've both built and seen decks that leverage low cost cards in creative ways to achieve a solid win rate.  So I thought...why not take a stab at learning more about if there's truth in the statement that it's just a 'pay to win' game.

## **Magic Overview**:
From Wikipedia, the free encyclopedia:
  - "Magic: The Gathering (colloquially known as Magic or MTG) is a collectible and digital collectible card game created by Richard Garfield.[1] Released in 1993 by Wizards of the Coast (now a subsidiary of Hasbro), Magic was the first trading card game and has approximately thirty-five million players as of December 2018,[2][3][4] and over twenty billion Magic cards produced in the period from 2008 to 2016, during which time it grew in popularity.[5][6]"

  - "A player in Magic takes the role of a Planeswalker, doing battle with other players as Planeswalkers by casting spells, using artifacts, and summoning creatures as depicted on individual cards drawn from their individual decks. A player defeats their opponents typically, but not always, by draining them of their starting life total. Although the original concept of the game drew heavily from the motifs of traditional fantasy role-playing games such as Dungeons & Dragons, the gameplay bears little similarity to pencil-and-paper adventure games, while simultaneously having substantially more cards and more complex rules than many other card games. "

MTG produces four sets of cards annually.  Each set consists of approximately 350 cards.  There is a category of deck creation called 'standard' that limits players to the most recent 6 sets released.  Each deck must have a minimum of 60 cards in their deck and are allowed a 15 card 'sideboard'.  The sideboard is a small pool of cards that can be used to refine their deck in between games at a tournament.  This 'standard' format is the focus of this analysis as that's the type of competition that each of the types of players described above participate in.

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/arean_game_play.png)

## **Areas of Exploration**:
As touched on in the introduction, my primary goal for the first phase of this project is to be able to compare the deck costs for the top 16 MTG players in the world against a collection of decks from 'skilled amateurs' of the game.  Ultimately I was looking to test my friends' hypothesis that this was a 'pay to win' game, and thus my null hypothesis would be that there was no difference between the world tournament competitor decks and the skilled amateur decks.  For this test I'd like to feel pretty confident in the results and will set our alpha level at .05%.  

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
  - This was the first data set that was tackled, and as such the took the most time.  This was the data set where I developed a basic approach for digging into a large and highly nested JSON format.  While the source website provided some basic information, it was unclear just how some of the data would be presented and translated from the cards.  Additionally, the presence of ~10 translations resulted in large swaths (literally rows and rows per card of screen-width text in other languages I have no understanding of) of hard to digest information.  Ultimately I was able to work through to the actual card-specific data, and from there explore the formats and types of data to build the table schema to start working with (as roughly shown in the diagram above).  To give an example of the variation that can occur, please see the image at the bottom of this section that puts a sample card from each of the 5 main types (artifact, planeswalker, spell - instant being just one of a handful of subtypes, land, and creature),  side by side (**foreshadowing...***) 
  - As you may guess... this variation resulted in most of the data needing to be of a string or collection of strings data type.  Additionally, there turned out to be a very slight variation in data elements provided between the sets requiring me to add a column or two with each run to accomodate the full 'all-set' data.   
  - Ultimately though, the data process was somewhat straightforward once I had the schema and understanding, and was handled by splitting the data into dataframes for each of the applicable tables (card data, set data, and detritus table) and then inserting into the appropriate DB tables.  Table creation was performed initially through SQL queries directly within the DB.  
  - The detritus table was a design i developed to enable me to ingest all of the data in the files, maintain linkage via the UUID, but keep the core tables and data for my analysis as lean and normalized as possible.  In the future, the data is there and can be unpacked as needed.  The biggest issue was with some of the nested collections I had to develop a process for converting them to strings so that the table would accept the data.
  - The [notebook](insert link) has been cleaned up as far as leveraging helper functions stored in an importable .py [file](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/src/mtg_helpers.py), but has been left with examples of the data and research conducted for those who would look to see more specifics of how it was navigated.

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/sample_card_types.png)

- Card prices
  - This data set went much faster than the card data, in part because I better understood how to work through JSON files and had helper functions established to facilitate sql connections, prepping for load, and inserting into the DB.  Additionally, this data set was completely housed in one file, so only required one load.
  - As stated the pricing data had prices from three different sources (one european, two US), three card formats (Arena Online, MTG Online, and paper), and a few other variations (foil cards vs non-foil).  Research indicated there was variation across the sources both in completeness of data and actual card price.  For the sake of moving forward with phase 1, I opted to go with the 'standard' approach of taking a single source (US-based CardKingdom, HQ'ed in my own Seattle neighborhood!) for paper, non-foil prices.  From what I could tell, this would give me the best total price coverage and I opted to avoid blending or mixing/matching sources at this point.  The approach left 168 cards without prices out of a total of over 3500 cards.
  - Additionally, because in general cards become less valuable the further from their release date they are (because they rotate out of standard amongst other reasons), I took the 'oldest' price value present per card to better approximate the prices when they were 'fresh' and in demand so as to avoid any skewing towards decks made out of older cards.
  - As I moved through the analysis phase of the project, I determined that of the 168 cards with missing prices, 28 of them were included in the deck lists. I dug further into this and identified that they were all non-standard cards in that they either had 'dual' domains or were in fact dual-sided.  Examples of these instances are provided at the end of this section for reference.  My hypothesis is that some of the data in the data sets was obtained through screen scraping and/or web-crawling and that these complex cards causee issues with what data is gathered about the cards that is in turn used to query pricing sources.  Because it was only 28, I manually looked them up on cardkingdom and ran an augmentation file run to update all cards needed for deck analysis.

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/complex_cards.png)

- Decklists
  - This data set while 'simple' in that the files were small, presented a few intriguing challenges for the project:
    1. They were in a relatively unstructured format with 3 different formats across the decks
    2. There were only card names as far as card identifiers go (see the pricing section and the image above for examples of wrinkles this could present)
    3. They contained integers corresponding to the number of each card present in a given deck
    4. There were relatively more of them (44) compared to the other data sets
  -  Item 1 was handled by reading the files in and processing line by line to parse, trap for header/section rows, and store in an appropriately structured dataframe.  There was a bug in my initial code related to a 'unique' element of a few deck lists that was caught in my analysis phase, and I was able to refine my code and reprocess everything.
  -  Item 2 required two steps, the first was a direct name match which achieved 90% match rate.  For the unmatched ones, after some research discovered that a good amount of these were related to the complex cards previously mentioned and that the names in the deck lists were often a substring of the name in the master card data.  Was able to get 100% match rate by building a process to look and match on the presence of the substring within the master name.
  -  Item 3 was handled by carrying the numbers forward and in analysis steps just using them to multiply things like price when looking at total deck analyses.
  -  Item 4 was handled by building my file processing script to access the folder and then iterate through each file present.

## **Extraction and Visualization**:
Once everything was cleaned and loaded to the postgresql DB, data extraction for analysis was managed within jupyter notebooks using psycopg2 and sql alchemy to pull the necessary data directly into dataframes.  From there I simply grouped data into the deck categories, created deck-level card and cost totals, and calculated the average cost per card in a deck.

When thining about possible approaches to the hypothesis test, I knew that I needed to assess how the core deck vs. sideboard compared to make a decision about inclusion/exclusion.  I also needed to get a sense for how the costs were distributed both within the player categories but also relative to each other.  I also made the decision to look at the average price per card as the cost metric as a way to frame it in a more approachable manner.  Below are histograms and boxplots looking at the distributions:

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/histo_decks_avg_price_of_card_sideboard_and_core_by_category.png)

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/deck_pricepercard_by_core_and_side_and_category.png)

These charts highlight a few key things: (1) the sideboards and core decks are quite different, especially within the world competitor group (2) the world comp core decks are clearly not normal (3) the two sets of core decks are not from the same distribution.  This info, coupled with the notion that the core decks are really where people put their best and primary cards, led me to decide to exclude the sideboards from the rest of the deck-comparison analysis.  

In the spirit of highlighting the impact of analysis/visualization on confirming the success of data cleaning and processing activities, I offer an example that helped call out the two issues mentioned above (bug in deck list processing and need to fill in the 28 missing prices).  Here's the 'before' graph that helped really identify the impacts of what had seemed like minor issues:

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/Priced_deck_size_by_category%20-%20original.png)

And the after:

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/priced_deck_size_by_category%20-%20after%20issue%20fix.png)

The black lines indicated what I'd been considering as far as a 'cutoff line' so that I was only using adequately complete decks.  
This is a great example of how what seemed like minor issues when building my data pipeline happend to present significant issues to my targeted analysis.  It also shows the value of continued review and data inspection throughout the analysis process.
### Three cheers to QC and reuasable code!


## **Testing the Hypothesis**:
Based on the analysis so far, it was time to conduct the hypothesis test.  Based on the play categories not being from the same distribution, not having enough samples to invoke the Central Limit Theorem, not appearing to be normal, but being independent from each other... I decided to conduct a Mann-Whitney U test.  At a high level, this test consists of comparing each value from one category against each value from the other category and tabulating a metric that reflects how many 'victories' the first category has over the second.  This statistic result is ultimately used to assess the result of the test and produce a p value.  [Wikipedia](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test) offers a good deep dive for those inclined to digging deeper.

Given that my hypothesis was linked to my friends' assertions that winning was just about how much money you spent, I set up the null hypothesis to be comparing the world competitor group with the assumption that their costs were not higher than that of the skilled amateurs.  The ## p-value returned from the test was .19 (much higher than my desired threshold of .05), indicating that I could not reject my null hypothesis ## and that there did not appear to be clear difference in price between these groups...which in turn leads me to infer that there really is some skill at play with how the cards are selected, decks built, and ultimately the game played.

This result aligns to what the box plots showed up above, in that there was a significant amount of overlap between the two inner quartiles.

## **Light Featurization and More Visualization**:
Now that I had my answer, I wanted to begin to dig into the data a bit deeper and work towards learning more about card-level price correlations and eventually models to identify cost-efficient cards and deck tuning.  I knew it would be important to be able to categorize cards by color and by types as  starting point.  There's something called 'devotion' in Magic that refers to how many icons of a given mana type or color is present.  My data on card color was messy in that it was a string field with curly braces surrounding a single letter for each color and a number for any uncolored mana.  As an example, here's what the data field might look like:  4{W}{B} corresponding to 4 uncolored, 1 white, and 1 black mana.  I built a helper function and migrated this data to card-level counts for each color in a color specific column. So the 4{W}{B} becomes a value of 1 in each of the 'White' and 'Black' columns.  This would allow future color-based analysis, but as an initial use case let me look at calculating a mono-color devotion for each deck.  I did this by summing the tallies of each card in a deck and taking the color with the max value.  Below is a chart showing this devotional color by player category and the prices of each.

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/Card_prices_by_devotion_category.png)

Of particular interest is that there is not a single world competitor deck that is predominantly green!

The next item to look at was card type.  This was another field that was 'rich' in information... as well as noise.  The field would have things like 'Legendary Planeswalker - Chandra', when what I really wanted was just the simple five categories from above: artifact, planeswalker, spell, land, and creature.  To give a bit of a sense of what was in the raw data, here's a wordcloud:

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/card_type_cloud_initial.png)

I was able to tackle this by creating a new column and populating it leveraging a helper function that tested for the categories I wanted within 'sterilized' verions of the raw category data.  More specifically, the helper function standardized the case, removed punctuation, and then matched the 5 categories against presence in the modified data set.  Since some cards can have multiple categories and I really just wanted to assign a single one, I did establish a priority in my assignment as: planeswalker, creature, spell, land, artifact.  From this work I was now able to make a simple pie chart for both the total card sets as well as the decks.  

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/pie_charts_yummy.png)

The distribution of the 'all cards' makes sense, as there aren't many lands produced outside of the 5 basic types that correspond to the five colors.  
When first getting into the game, I was told a 'balanced' deck was typically 40% land, 40% creatures, and 20% spells/artifacts.  It's interesting to see the strong skew towards spells/artifacts present in the combined world comp and skilled amateur view.  Maybe something to consider when I make my next deck...   

## **Close out**:

All in all this was a great project as it allowed me to get a lot of hands on experience with JSON file formats, bulk file processing, pipeline creation, postgreSQL, and matplotlib visualization... but also helped me build a solid rebuttal against my friends' perpsective on skill in Magic!  

One of the areas of interest i have for future work is looking at characteristics that make a good deck and/or a valuable card.  Based on the outcome of this project, I now how to look at both groups of deck builders... finding commonalities that might be 'universal best practices' but then drill in further to identify any differences that might highlight that 'special sauce' the world competition stage players bring.

A final thought was that I also discovered my enjoyment with data engineering in addition to the more data sciencey aspects of this project.. and appreciate that I now have a replicable process for continuing to ingest and build out the repository and analysis I've built.
  
## **Credits**

Overviews for Magic and Stats: https://en.wikipedia.org/
Card data: https://mtgjson.com
Deck list data: https://magic.wizards.com
Images: https://magic.wizards.com


