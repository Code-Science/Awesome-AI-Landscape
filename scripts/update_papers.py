import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re

def fetch_top_papers():
    url = "https://huggingface.co/papers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    papers = []
    for paper in soup.find_all('div', class_='paper-card')[:3]:
        title = paper.find('h4').text.strip()
        votes = paper.find('span', class_='votes').text.strip()
        category = paper.find('span', class_='category').text.strip()
        url = paper.find('a')['href']
        
        papers.append({
            'title': title,
            'votes': int(votes),
            'category': category,
            'url': f"https://huggingface.co{url}"
        })
    
    return papers

def update_readme(papers):
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 构建新的论文表格
    papers_md = "## 📰 Daily Top Papers\n> 🔄 Auto-updated daily from Hugging Face Papers\n\n"
    papers_md += "| Paper | Votes | Category |\n|-------|--------|-----------|\n"
    
    medals = ['🏆', '🥈', '🥉']
    for i, paper in enumerate(papers):
        papers_md += f"| {medals[i]} [{paper['title']}]({paper['url']}) | ⭐ {paper['votes']} | {paper['category']} |\n"
    
    papers_md += f"\n<sub>Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC</sub>\n"
    
    # 在 Weekly Highlights 部分之前插入
    pattern = r"## 🔥 Weekly Highlights"
    updated_content = re.sub(pattern, f"{papers_md}\n\n{pattern}", content)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(updated_content)

if __name__ == "__main__":
    papers = fetch_top_papers()
    update_readme(papers)