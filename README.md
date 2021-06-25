# fedi-quote-bot

Simple python bot that posts a random quote to a Mastodon/Pleroma/Misskey/etc account from a text file    

You can see a live version of this bot [here](https://disqordia.space/stirner_bot)    

## Setting up 
- Install python3  
- Copy `config.py.example` to `config.py` and configure with your bot's credentials and your preferences.   
- Create a file where your quotes will be stored. By default, `example-quotes.txt` is used which contains Max Stirner quotes

## Usage

- Generate and post a quote with `python3 ./main.py`  
- Add a quote with `python3 ./main.py --quote` (or `-q`)   
- Add multiple quotes with `python3 ./main.py --multi` (or `-m`) to enter a quote on each new line  
  - Type "quit" to exit multi-quote mode  

## Automatic posting 

- Edit crontab with `crontab -e`  
- Add a new line such as  
`*/30 * * * cd /home/me/mybotfolder/ && /usr/bin/python3 ./main.py`  

This will post every 30 minutes 

