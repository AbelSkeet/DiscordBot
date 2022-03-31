# DiscordBot
Bot for server on Discord

## Introduction

This is a project to create your own discord botserver, and here are (so far) some notes on how to assemble the bot.



## Techs

As we develop the project, update which technologies we are using

* [Python](https://www.python.org/): Simple syntax programming language;
* [Mongodb](https://www.mongodb.com/): Non-relational database for information storage, the database is being used directly on the site;
* [Discord Developer Portal](https://discord.com/developers/applications): website to register your application/bot;
* [Discord.py](https://discordpy.readthedocs.io/en/latest/): Library for discord integration;

## Requirements

* Have installed Python version 3.5 (during development we started with version 3.5, so we cannot guarantee that older versions will work);
* Create a Token.py file, fill in the following data:
```py
class TokenDiscord:
  def uploadToken():
    return {
      "database": "Connection link to mongodb",
      "idpresentacao":"is a long that represents the id of one of the channels where you will have points for reactions",
      "idaviso":"is a long that represents the id of one of the channels where you will have points for reactions",
      "token":"bot access token, generated on the Discord Developer Portal website"
    }
    
    ```

## GAMIFICATION

Bot gamification is done through 2 types, xp and levels, xp is divided into weekly and by channel, levels are calculated in general;

### XP

The xp calculation will follow these rules:
* By message:
  * Minimum of 2 words;
  * Maximum per message, 40 points;
  * Number of non-repeating characters / 3;
* Reactions to messages:
  * Available on some channels;
  * Badlist of emojis, remove points, 200 points, remove reaction;
  * Goodlist of emojis, 5 emojis, 2x points, 100 basis points;
* Voice channels time:
  * Check what information we receive to evaluate the points
* Screen sharing:
  * Check what information we receive to evaluate the points
  
  #### pymongo operations

This information that is being shown is just to understand how pymongo should be used

* **Insert**
```py
date = {
  'name': 'Jef',
  'age': 45
}

responseData = collection.insert_one(data)
# responseData is of type InsertOneResult, I just saw that it has the inserted_id so far
```
[InsertOneResult info](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertOneResult)

* **Replace**
```py
date = {
  'name': 'Jef',
  'age': 45
}

responseData = collection.replace_one({'name': 'Matthew'}, data)
# responseData is of type UpdateResult, I just saw that it has matched_count,modified_count and upserted_id of relevant information
```
[UpdateResult info](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult)

* **Update**
```py

responseData = collection.update_one({'name': 'Matthew'}, {'$inc': {'age': 2}}, upsert)
# responseData is of type UpdateResult, I just saw that it has matched_count,modified_count and upserted_id of relevant information
# increment the age value by 2
# upsert is a boolean value, which will define whether to insert the object or not
```
[UpdateResult info](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult)
* Other interesting operators:
  * $set: will set a specific value
  * $mul: will multiply the property by the specified value
  * $rename: will change the field
  * $setOnInsert: if the query does not result in anything, and the object has to be inserted, add the fields
  * $unset: remove the field
* For arrays:
  * $: updates the first one found in the condition
  * $[]: updates all elements found
  * $[\<identifiers\>]: updates all that match the condition inside the parentheses

[Update Operators Info](https://docs.mongodb.com/manual/reference/operator/update/#std-label-update-operators)

* **update_many**
```py
responseData = collection.update_many(
    {'value': 10}, {'$set': {'test2':'new'}})
# look for everywhere where value is equal to 10, and change/add the field test2 = new
```
[UpdateResult info](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult)
