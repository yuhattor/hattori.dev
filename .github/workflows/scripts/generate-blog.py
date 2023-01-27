import re
import sys
import json
import requests
from datetime import datetime

# Get Arguments 
api_key = sys.argv[1] # DeepL API key
repository = sys.argv[2] # GitHub repository name in the format of "username/repo"
issue_id = sys.argv[3] # GitHub issue id

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

# format the date, input: "Thu, 20 Feb 2020 17:00:00 +0000", output: "2020-02-20"
def format_date(published_date: str):
  date_string = published_date
  date_object = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %z")
  return date_object.strftime("%Y-%m-%d")

# Get Issue Body
text = requests.get(f"https://api.github.com/repos/{repository}/issues/{issue_id}").json()["body"]

# Get Items
title = re.search(re.compile(r"## Title\n(.+?)\n\n## Link") , text).group(1) # Get title from issue body
link = re.search(re.compile(r"## Link\n(.+?)\n\n## Published date") , text).group(1) # Get link from issue body
published_date = format_date(re.search(re.compile(r"## Published date\n(.+?)\n\n## Author") , text).group(1)) # Get published date from issue body
author = re.search(re.compile(r"## Author\n(.+?)\n\n## Description") , text).group(1) # Get author from issue body
description = re.search(re.compile(r"## Description\n(.+?)\n\n## Raw Content") , text).group(1) # Get description from issue body
content = re.search(r"## Raw Content(.*)```", text, re.DOTALL).group(1) # Get content from issue body

# format the content for blog
blog_content = f"""---
title: { translate_with_deepl(api_key, title) }
englishtitle: { title }
date: { published_date }
cardurl: { link }
description: { description }
author: { author }
---
{ translate_with_deepl(api_key, content, is_xml=True) }
"""

# write the content to a file
item = f"{published_date}-{re.sub(r'[^a-z0-9]', '-', title.lower())}"
with open(f"content/changelog/{item}.md", 'w') as f:
  f.write(blog_content)

print(item)
