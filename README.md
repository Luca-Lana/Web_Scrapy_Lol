# Web Scrapy League of Legends Info 🕸

## Description 

This script will do a web scrapy in the website op.gg to get information like runes, speels and build of same champion in the lane typed and it will be used in a future project of a discord bot to bring information about what champion or lane typed in the command.

The python language was chosen beacause in addtion to be my favorite language i want to practice my studies and test my knowledge.

The "hardest" part of this project was when I had to analyze the code, but after some time analyzing the code I can see the best way to get the information.


## Libraries 📚

- [Requests](https://pypi.org/project/requests/)

- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

- [html.parser]()


## Installation 💻

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries.

```bash
pip install requests

pip install beautifulsoup4

pip install html.parser
```


## How to Use the Project

After installing the necessary libraries for the script to work, it is necessary to instantiate the class and type a champion and a role after that call some function!

### Usage 📢

```python
import InfoLol

info = InfoLol('champion', 'lane')

# returns speels of the champion in that lane
info.get_speel()

# returns runes of the champion in that lane
info.get_runes()

```

## License
[MIT](https://choosealicense.com/licenses/mit/)