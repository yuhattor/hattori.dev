import re
import sys
import requests
from datetime import datetime

# Get Arguments 
api_key = sys.argv[1]
repository = sys.argv[2]
issue_id = sys.argv[3]

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
  result = requests.get("https://api-free.deepl.com/v2/translate", params=params) 
  data = result.json()
  return data["translations"][0]["text"]

def format_date(published_date: str):
  date_string = published_date
  date_object = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %z")
  return date_object.strftime("%Y-%m-%d")

# Get Issue Body
text = requests.get(f"https://api.github.com/repos/{repository}/issues/{issue_id}").json()["body"]

# Get Items
title = re.search(re.compile(r"## Title\n(.+?)\n\n## Link") , text).group(1)
link = re.search(re.compile(r"## Link\n(.+?)\n\n## Published date") , text).group(1)
published_date = format_date(re.search(re.compile(r"## Published date\n(.+?)\n\n## Author") , text).group(1))
author = re.search(re.compile(r"## Author\n(.+?)\n\n## Raw Content") , text).group(1)
content = re.search(r"## Raw Content(.*)```", text, re.DOTALL).group(1)

blog_content = f"""---
title: { translate_with_deepl(api_key, title) }
englishtitle: { title }
date: { published_date }
cardurl: { link }
author: { author }
---
{ translate_with_deepl(api_key, content, is_xml=True) }
"""
item = f"{published_date}-{re.sub(r'[^a-z0-9]', '-', title.lower())}"
with open(f"content/changelog/{item}.md", 'w') as f:
  f.write(blog_content)

print(item)
