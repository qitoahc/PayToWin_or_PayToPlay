# Magic: The Gathering -- Pay To Win or Pay To Play?

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/banner.png)

# Table of Contents
1. [Intro and Motivation](#intro-and-motivation)
2. [Magic: The Gathering - What is it exactly?](#magic:-the-gathering---what-is-it-exactly?)
3. [Areas of exploration](#areas-of-exploration)
4. [Data Sources](#data-sources)
5. [Data Processing and Cleaning](#data-processing-and-cleaning)
6. [Visualization](#visualization)
7. [Testing the Hypothesis](#testing-the-hypothesis)
8. [Conclusion](#conclusion)
9. [Photo and Data Credits](#photo-and-data-credits)

## **Intro and Motivation**: 
As someone who enjoys Magic: The Gathering (MTG) as a causal activity with friends, I’ve often heard people talk about enjoying it, but feeling like it's a money pit and whoever spends the most on a given deck always wins.  On the flip side, I've both built and seen decks that leverage low cost cards in creative ways to achieve a solid win rate.  So I thought...why not take a stab at learning more about if there's truth in the statement that it's just a 'pay to win' game.

## **Magic: The Gathering - What is it exactly?**:
From Wikipedia, the free encyclopedia:
  - "Magic: The Gathering (colloquially known as Magic or MTG) is a collectible and digital collectible card game created by Richard Garfield.[1] Released in 1993 by Wizards of the Coast (now a subsidiary of Hasbro), Magic was the first trading card game and has approximately thirty-five million players as of December 2018,[2][3][4] and over twenty billion Magic cards produced in the period from 2008 to 2016, during which time it grew in popularity.[5][6]"

  - "A player in Magic takes the role of a Planeswalker, doing battle with other players as Planeswalkers by casting spells, using artifacts, and summoning creatures as depicted on individual cards drawn from their individual decks. A player defeats their opponents typically, but not always, by draining them of their starting life total. Although the original concept of the game drew heavily from the motifs of traditional fantasy role-playing games such as Dungeons & Dragons, the gameplay bears little similarity to pencil-and-paper adventure games, while simultaneously having substantially more cards and more complex rules than many other card games. "

![alt text](https://github.com/qitoahc/PayToWin_or_PayToPlay/blob/main/images/arean_game_play.png)

## **Areas of Exploration**:
As touched on in the introduction, my primary goal for the first phase of this project is to be able to compare the deck costs for the top 16 MTG players in the world against a collection of decks from 'skilled amateurs' of the game.  Ultimately my hypothesis is that there is not a stastitically significant difference in the costs between the two groups of decks.

## **Data Sources**:


## **Data Processing and Cleaning**:

## **Visualization**:

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
