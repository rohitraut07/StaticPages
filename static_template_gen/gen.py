from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load
import requests
import json
import random

template_env = Environment(loader=FileSystemLoader(searchpath="./"))

response = requests.get("http://localhost/sapi/v1.0/contents")

with open("config.json", "w+") as config:
    json.dump(response.json(), config)

with open('config.json') as config_file:
    config = load(config_file)

random.shuffle(config['items'])

random.shuffle(config['items'])  # No assignment

x = 0
c = 0
j = 0

while x + 5 <= (len(config['items']) - len(config['items']) % 5):
    file_name = "layout_" + chr(65 + j % 4) + '_' + str(c) + ".html"
    try:
        if 'A' in file_name:
            template = template_env.get_template('Layouts/layout1.html')
            with open(f"Generated/Layout_A/{file_name}", "w") as output_file:
                output_file.write(
                    template.render(
                        items=config['items'][x:x + 5]
                    )
                )
                print("length", len(config['items'][x:x + 5]))
        elif 'B' in file_name:
            template = template_env.get_template('Layouts/layout2.html')
            with open(f"Generated/Layout_B/{file_name}", "w") as output_file:
                print(config['items'][x:x + 5])
                output_file.write(
                    template.render(
                        items=config['items'][x:x + 5]
                    )
                )
        elif 'C' in file_name:
            template = template_env.get_template('Layouts/layout3.html')
            with open(f"Generated/Layout_C/{file_name}", "w") as output_file:
                output_file.write(
                    template.render(
                        items=config['items'][x:x + 5]
                    )
                )
        elif 'D' in file_name:
            template = template_env.get_template('Layouts/layout4.html')
            with open(f"Generated/Layout_D/{file_name}", "w") as output_file:
                output_file.write(
                    template.render(
                        items=config['items'][x:x + 5]
                    )
                )
        else:
            pass
    except:
        pass
    x = x + 5
    j = j + 1
    print(j)
    if j % 4 == 0:
        c = c + 1
        print(x, j)
