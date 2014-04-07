LifeLogger
==========

A webapp for logging and analyzing data generated by our daily lives so that we can optimize for what matters to us.

>*Towards a better tomorrow, today!*

Essentially a tool to aid in [instrumental rationality](https://en.wikipedia.org/wiki/Instrumental_rationality), giving the user the ability to log, analyze and act upon the results to optimize for things like productivity, mood but also help the user grow good habits and get rid of bad ones.


## Planned features

 - **Mood, productivity, alertness logging**  
   Logging of subjective measurements of mood, productivity, alertness several times daily.
 - **Sleep logging**  
   Lets the user input their bed- and wakeup-times in order keep track of total sleep time, sleep regularity and, if data is available, deep sleep time.
 - **Habits**  
   Lets the user log their good and bad habits in a way that encourages users to keep doing the good ones and stop doing the bad ones.
   - Implements streaks (also known as the ["Seinfeld method"](http://lifehacker.com/281626/jerry-seinfelds-productivity-secret)) making the user aware of their progress, good or bad, essentially creating a feedback loop.
   - Gives the user the ability to log physical activity and see how it affects their lives.
 - **Cognitive performance logging**  
   By importing results from services like [Quantified Mind](http://www.quantified-mind.com/) one can get an indicator of cognitive performance.
 - **Drugs & supplements logging**  
   Enter information about the intake of psychoactives such as caffeine, nicotine, alcohol or supplements to see how it affects the user.
 - **Body stats**  
   Log more long-term changes such as weight, body fat, body composition and measurements to see how they change over time.
 - **Analyze the data to find out what logged variables and habits leads to what outcome**  
   This is a difficult task, but one we hope to be able to do better and better with time.
 - And a lot more...

## FAQ
 - **Sounds like it takes a lot of time?**  
   It doesn't really take that much time, and we live in a world where more and more of our data could be delivered automagically which is something we hope to be able to do more and more as humanity makes technological progress.

 - **Is it worth the effort?**  
   This question is yet to be answered fully, but we think so yes (we wouldn't do it otherwise). Much work remains to be done and we believe that this can improve to the point where it becomes standard practice.

 - **This sounds like an incredible data-source to mine, will this be done?**  
   We too see the potential to use users logs to get access to data otherwise expensive and timeconsuming to create, it poses a significant data privacy threat however, one which we take _very_ seriously. So this is an open question, we hope that we can do this without violating the privacy of our users, if we can't we wont.

## Technologies used:
These are currently only propositions, and are subject to change.
 - Python 3.2+
 - Flask, an excellent microframework (might change in the future)
 - peewee, ORM used together with Flask thanks to flask-peewee
 - peewee-compatible database (SQLite, MySQL or PostgreSQL)
 - MongoDB, to store users logdata (might change in the future)
 - Bootstrap, for efficient and decent web-design
 - Backbone.js
 - Vagrant, for easy testing and deployment
 - Chef or Puppet, for configuration management

-----
Erik Bjäreholt <erik@bjareho.lt>
