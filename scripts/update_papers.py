import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
from tenacity import retry, stop_after_attempt, wait_exponential
import logging
import sys
import re

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('update_papers.log')
    ]
)
logger = logging.getLogger(__name__)

class PaperUpdater:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True
    )
    def fetch_papers(self):
        try:
            url = "https://huggingface.co/papers"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            papers = []
            
            articles = soup.find_all('article')
            
            for article in articles:
                try:
                    # 获取论文标题和链接
                    title_elem = article.find('h3').find('a')
                    title = title_elem.get_text(strip=True)
                    link = f"https://huggingface.co{title_elem['href']}"
                    
                    # 获取投票数 - 直接查找包含投票数的div
                    votes_count = 0
                    votes_div = article.find('div', class_='shadow-alternate')
                    if votes_div:
                        votes_text_div = votes_div.find('div', class_='leading-none')
                        if votes_text_div:
                            votes_text = votes_text_div.get_text(strip=True)
                            votes_count = 0 if votes_text == "-" else int(votes_text)
                    
                    papers.append({
                        'title': title,
                        'url': link,
                        'votes': votes_count
                    })
                    
                except Exception as e:
                    logger.error(f"Error parsing paper: {e}")
                    continue
            
            return papers
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching papers: {e}")
            raise


    def update_readme(self, papers):
        """更新 README.md 文件"""
        try:
            with open('README.md', 'r', encoding='utf-8') as f:
                content = f.read()

            # 准备新的论文表格
            papers_md = "## 📰 Daily Top Papers\n"
            papers_md += "> 🔄 Auto-updated daily from Hugging Face Papers\n\n"
            papers_md += "| Paper | Votes | Category |\n"
            papers_md += "|-------|--------|-----------|"

            # 添加论文信息
            for i, paper in enumerate(papers[:3], 1):
                medal = {1: '🏆', 2: '🥈', 3: '🥉'}[i]
                papers_md += f"\n| {medal} [{paper['title']}]({paper['url']}) "
                papers_md += f"| ⭐ {paper['votes']} | AI |"

            # 添加更新时间
            current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
            papers_md += f"\n\n<sub>Last updated: {current_time}</sub>"

            # 更新文件内容
            new_content = self._replace_section(content, papers_md)
            
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(new_content)

            logger.info("README.md updated successfully")
            
        except Exception as e:
            logger.error(f"Error updating README: {e}")
            raise

    def _replace_section(self, content, new_section):
        """替换特定部分的内容"""
        try:
            start_marker = "## 📰 Daily Top Papers"
            end_marker = "<sub>Last updated:"
            
            start_idx = content.find(start_marker)
            if start_idx == -1:
                # 如果找不到标记，追加到文件末尾
                return content + "\n\n" + new_section
                
            end_idx = content.find(end_marker)
            if end_idx == -1:
                end_idx = content.find("\n## ", start_idx + 1)
                
            if end_idx == -1:
                end_idx = len(content)
                
            return content[:start_idx] + new_section + content[end_idx:]
            
        except Exception as e:
            logger.error(f"Error replacing section: {e}")
            raise

    def run(self):
        """主运行函数"""
        try:
            logger.info("Starting paper update process")
            
            # 获取论文数据
            papers = self.fetch_papers()
            
            # 按投票数排序
            papers.sort(key=lambda x: x['votes'], reverse=True)
            
            # 更新 README
            self.update_readme(papers)
            
            logger.info("Paper update process completed successfully")
            
        except Exception as e:
            logger.error(f"Fatal error in main process: {e}")
            raise

if __name__ == "__main__":
    try:
        updater = PaperUpdater()
        updater.run()
    except Exception as e:
        logger.critical(f"Program terminated with error: {e}")
        sys.exit(1)
