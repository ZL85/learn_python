from pathlib import Path

import requests
import plotly.express as px


url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+jason"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
# print(response_dict.keys())
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict["items"]
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)

fig.show()
out_path = Path("htmls/python_repos_visual_01.html")
fig.write_html(out_path)
