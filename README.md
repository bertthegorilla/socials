# socials
Webhook for socials - This is a package that can be installed and run locally by your machine

For Twitter:
1. Set up a developer account at https://www.developer.twitter.com/
2. Save your credentials somewhere safe
3. Add the following environment variables to your machine:
  
    a) BEARER_TOKEN: YOUR BEARER TOKEN
  
    b) TWITTER_ID: YOUR TWITTER ID YOU WANT TO PULL FROM
  
    c) TWEET_FILE: THE PATH TO THE CSV
  
    d) WEBHOOK: THE WEBHOOK URL GIVEN BY YOUR DISCORD SERVER

4. Ensure the .bat file, .csv file, and .py file are all in the same folder
5. Either run manually by executing the .bat file, or use a scheduling program to run it as often as you need. Note that there is a 500k limit per month for this endpoint.
