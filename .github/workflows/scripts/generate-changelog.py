import re
import sys
import json
import requests
from unidecode import unidecode
from datetime import datetime
from bs4 import BeautifulSoup

# Get Arguments 
api_key = sys.argv[1] # DeepL API key
repository = sys.argv[2] # GitHub repository name in the format of "username/repo"
issue_id = sys.argv[3] # GitHub issue id
openai_api_key = sys.argv[4] #OpenAI API key

# Translate with DeepL
def translate_with_deepl(api_key: str, content: str, is_xml: bool = False):
  params = { 
      "auth_key": api_key,
      "source_lang": "EN",
      "target_lang": "JA",
      "text": content,
  }
  if is_xml:
      params["tag_handling"] = "xml"
  result = requests.post("https://api-free.deepl.com/v2/translate", data=params) 
  data = result.json()
  return data["translations"][0]["text"]

# format the date, input: "Thu, 20 Feb 2020 17:00:00 +0000", output: "2020-02-20"
def format_date(published_date: str):
  date_string = published_date
  date_object = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %z")
  return date_object.strftime("%Y-%m-%d")

def get_cover_image_url(url):
  response = requests.get(url)
  html = response.content
  soup = BeautifulSoup(html, 'html.parser')
  images = soup.select("main.changelog img")
  if images:
    return images[0].get("src")
  return ""

# 文章を要約する関数
# summarize the article
def summarize(text, openai_api_key):
  # API Key の設定
  url = "https://api.openai.com/v1/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
  }
  data = {
    "model": "text-davinci-003",
    "prompt": ('Summarize this text in one sentence: ' + text),
    "temperature": 0.5,
    "max_tokens": 50
  }

  payload = json.dumps(data,ensure_ascii=False).encode('utf-8').decode('unicode-escape')
  response = requests.post(url, headers=headers, data=payload)

  if not 'choices' in response.json():
    return ""

  message = response.json()['choices'][0]['text']
  return message


# Get Issue Body
text = requests.get(f"https://api.github.com/repos/{repository}/issues/{issue_id}").json()["body"]

# Get Items
title = re.search(re.compile(r"## Title\n(.+?)\n\n## Link") , text).group(1) # Get title from issue body
link = re.search(re.compile(r"## Link\n(.+?)\n\n## Published date") , text).group(1) # Get link from issue body
published_date = format_date(re.search(re.compile(r"## Published date\n(.+?)\n\n## Author") , text).group(1)) # Get published date from issue body
author = re.search(re.compile(r"## Author\n(.+?)\n\n## Description") , text).group(1) # Get author from issue body
description = re.sub(r"\n", " ", re.search(r"## Description(.*)## Raw Content", text, re.DOTALL).group(1))[0:1400]
content = re.search(r"## Raw Content(.*)```", text, re.DOTALL).group(1) # Get content from issue body

# Summarize description
english_summary = re.sub(r"\n", " ", summarize(description, openai_api_key))
summary = translate_with_deepl(api_key, english_summary) 


# format the content for changelog
changelog_content = f"""---
title: "{ translate_with_deepl(api_key, title) }"
englishtitle: "{ title }"
date: "{ published_date }"
cardurl: "{ link }"
author: "{ author }"
description: "{ description }"
coverimage: "{ get_cover_image_url(link) }"
englishsummary: "{ english_summary }"
summary: "{ summary }"
---
{ translate_with_deepl(api_key, content, is_xml=True) }
"""

# write the content to a file
item = f"{published_date}-{re.sub(r'[^a-z0-9]', '-', title.lower())}"
with open(f"content/changelog/{item}.md", 'w') as f:
  f.write(changelog_content)

print(item)
