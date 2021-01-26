# Murphy's bot
Want to get a Murphy's law once a day in your tweeter feed? This is your tweeter bot: [Murphys_kick](https://twitter.com/KickMurphys)<br>
*Anything could have gone wrong, but this time it went right* :)
## What it is?
This is a twitter bot that tweets daily one of the famous Murphy's laws. It is automated with **Python** and a **Lambda Function** in **AWS**. 

I based this project, twitching and modifying it here and there, on [@_dylancastillo](https://twitter.com/_dylancastillo)'s bot, who wrote an excellent [template](https://github.com/dylanjcastillo/twitter-bot-python-aws-lambda) and a great [tutorial](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/) accompanying it. **All credit goes to him.**

## How it works?

+ First, there is a very basic web scrapping from a [plain static web](http://www.murphys-laws.com/murphy/murphy-laws.html) containing the desired messages to post. Then, after a simple preprocessing using regex, I created a file containing all the potential tweets. 

+ The main functions that retrieve the tweets and post them using the Twitter API are in [lambda_function.py](https://github.com/DavidCarricondo/murphys_bot/blob/main/src/lambda_function.py).

+ The [createlambdalayer.sh](https://github.com/DavidCarricondo/murphys_bot/blob/main/createlambdalayer.sh) creates a lambda layer with the libraries in requirements.txt and using a **Docker image**. This is the layer that will be uploaded to AWS.

+ The [buildpackage.sh](https://github.com/DavidCarricondo/murphys_bot/blob/main/buildpackage.sh) only wraps the function in a zip file to upload it as a lambda function. 

+ The lambda function is scheduled using **EventBridge**

