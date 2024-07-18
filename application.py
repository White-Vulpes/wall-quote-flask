from flask import Flask, request, render_template_string, url_for
from quotes import quotes
from themes import get_themes
import random
import os

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def home():
    font = os.listdir('./static/fonts')
    font = font[random.randint(-1, len(font) - 1)]
    font_url = url_for('static', filename=f'''fonts/{font}''')
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wall Quotes</title>
    <style>
        {get_themes(font_url=font_url)}
    </style>
    </head>
    <body>
        <div>
            {quotes[random.randrange(0, len(quotes))]}
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    application.run(debug=False)

