# IPL-streak-analysis
Looking for aa specific pattern of streaks at any point in the IPL group stages

Specifically, this looks for the times when the three-match streaks of each IPL team is different.
That is their streaks are {WWW, WWL, WLW, WLL, LWW, LWL, LLW, LLL}

I have also added my initial attempt to simulate a large number of IPL seasons to find probability of such a streak. But, it turns out that the small scheduling quirks due to logisitcal issues (which I couldn't simulate,) hugely decreases probability of such a streak pattern.

In my second attempt I got my hands on a database of all IPL mathces and their results. I then deduced the streak after every match to see how often it happened. I kind of didn't clean the code in the end, so even though it works for ipl08, I did not modify it to test for all seasons (I lost motivation after I knew my logic works lol).

I have included the modified database I used for analysis too.
