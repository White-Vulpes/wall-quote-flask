import random
def get_themes(font_url):
    format = font_url.split('.')[1]
    colorTheme = ['FF204E', 'F2613F', '22092C', '346751', 'ED6663', '055E68', '76ABAE', 'ECB365']
    themes = [
    f"""@font-face {{
            font-family: 'Darkline';
            src:  url("{font_url}")  format('{'truetype' if format == 'ttf' else 'opentype'}');
            font-weight: normal;
            font-style: normal;
        }}
        body, html {{
            margin: 0;
            width: 1080px;
            height: 2340px;
            display: flex;
            text-align: center;
            justify-content: center;
            align-items: center;
            background-color: #{colorTheme[random.randint(-1, len(colorTheme) - 1)]};
            font-family: 'Darkline';
        }}
        div {{
            color: #fff; /* Set text color */
            mix-blend-mode: difference;
            font-size: 180px; /* Set text font size */
            padding: 70px;
            line-height: 210px;
        }}"""
    ]
    return themes[random.randint(-1, len(themes) - 1)]