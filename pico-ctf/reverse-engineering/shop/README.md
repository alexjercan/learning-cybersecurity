# Shop

[Shop](https://play.picoctf.org/practice/challenge/134)

## Description

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net 42159.

## Solution

Playing around with the binary file I have noticed that it doesn't take into
account the case when you try to buy a negative amount of fruits. It still
checks however if you have enough money to buy one, but it gives you money for
the amount that you "sell".

So the idea is to sell some fruits to get enough money to buy the flag fruit.
So you can input `1`, then `-4`. This will sell 4 average apples and will grant
you with enough (100) money to buy the Fruitful Flag. So for the next input you
can enter `2` and then `1`.
