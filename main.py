from mastodon import Mastodon
from xml.sax import saxutils as su
import config
import random
import argparse

parser = argparse.ArgumentParser(description="Random quote bot for the fediverse")
parser.add_argument('-q', '--quote', help="Add a new quote", action="store_true")
parser.add_argument('-m', '--multiple', help="Add multiple quotes until you type quit", action="store_true")

args = parser.parse_args()
quote_file = config.QUOTEFILE

if args.quote:
    with open(quote_file, 'a+') as reader:
        reader.seek(0)
        data = reader.read()
        print(f"\nAdding new quote to file: {quote_file}\n")
        args.quote = su.escape(input("Your quote: "))
        if len(data) > 0 :
            reader.write(args.quote + "\n")
            print("\nQuote added!\n")
            exit()

elif args.multiple:
    with open(quote_file, 'a+') as multi:
        multi.seek(0)
        data = multi.read()
        print(f"\nEntering multi-quote mode. File: {quote_file}\n\nAdd one quote per line. Type quit to exit.\n")
        while args.multiple != "quit":
            args.multiple = su.escape(input("> "))
            if ((len(data) > 0) and (args.multiple != "quit")):
                multi.write(args.multiple + "\n")
                print("\nQuote added!\n")
            if args.multiple == "quit":
                exit()

else:
    quote_data = open(quote_file, "r").readlines()
    fedi_status = su.unescape(random.choice(list(quote_data)))

    print(f"Generating quote for fedi...\n\n{fedi_status}\n")

    Mastodon.create_app (
        'quote-bot',
        scopes=['read', 'write'],
        api_base_url = config.URL,
        to_file = 'quotebot_clientcred.secret'
    )

    mastodon = Mastodon (
        client_id = 'quotebot_clientcred.secret',
        api_base_url = config.URL
    )

    mastodon.access_token = mastodon.log_in (
        username = config.USERNAME,
        password = config.PASSWORD,
        scopes = ['read', 'write']
    )

    mastodon.status_post (fedi_status, visibility=config.VISIBILITY)
    print("Posted!")
