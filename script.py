from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load
import requests
import json
import random


template_env = Environment(loader=FileSystemLoader(searchpath="./"))
template = template_env.get_template('layout.html')

# response = requests.get("https://api.cr.com/api/v1.0/contents")

# with open("config.json","w+") as config:
#     json.dump(response.json(), config)

with open('config.json') as config_file:
    config = load(config_file)
    
random.shuffle(config['items'])  # No assignment


with open('article.md') as markdown_file:
    article = markdown(markdown_file.read())


with open("index.html", "w") as output_file:
    output_file.write(
        template.render(
            article=article,
            items = config
        )
)