import os
from flask import Flask, send_file
from discord_webhook import DiscordWebhook

app = Flask(__name__)

# Set the path to the directory you want to serve files from
serve_dir = '/data/data/com.termux/files/home/storage/emulated/*'

# Set your Discord webhook URL
webhook_url = 'https://discord.com/api/webhooks/1103730454231793796/svWcnsUU8hHpPtXPKwL9lF7fEM2Ec36EdLXnABaMV6TX2iRardGTOHnQW7C8DkEQykrV'


@app.route('/')
def index():
    # When the user connects to the root URL, send the index.html file
    return send_file(os.path.join(serve_dir, 'index.html'))


@app.route('/<path:path>')
def serve_file(path):
    # Serve any other files in the directory
    return send_file(os.path.join(serve_dir, path))


if __name__ == '__main__':
    # Start the web server
    app.run()

    # When the server starts, send a Discord webhook message
    webhook = DiscordWebhook(url=webhook_url, content='Web server started!')
    response = webhook.execute()
