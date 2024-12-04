from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
# article_tag = soup.find(name="a", class_="storylink")
# article_text = article_tag.getText()
# print(article_text)
# article_link = article_tag.get("href")
# print(article_link)
# article_upvote = soup.find(name="span", class_="score")
# upvote_score = article_upvote.getText()
# print(upvote_score)

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# print(article_texts)
# print(article_links)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_upvote)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# print(int(article_upvote[0].split()[0]))

# import lxml

# with open(r"C:\HTML\bs4-start\website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "lxml")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)

# # print(soup)
# # print(soup.prettify())

# # print(soup.a)
# all_anchor_tags = soup.findAll(name="a")
# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# # print(section_heading.name)
# # print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# # print(company_url)

# name = soup.select_one(selector="#name")
# # print(name)

# headings = soup.select(".heading")
# print(headings)