import requests
from bs4 import BeautifulSoup
import csv

# GitHub trending URL
url = "https://github.com/trending"
headers = {"User-Agent": "Mozilla/5.0"}

# Fetch HTML from GitHub Trending
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Parse top 5 repositories
repositories = soup.find_all('article', class_='Box-row')[:5]

# Extract name and link
repo_data = []
for repo in repositories:
    name = repo.h2.a.get_text(strip=True).replace('\n', '').replace(' ', '')
    link = f"https://github.com{repo.h2.a['href']}"
    repo_data.append([name, link])

# Save to CSV
with open('trending_repos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Repository Name', 'Link'])
    writer.writerows(repo_data)

print("✅ Top 5 GitHub trending repositories saved to trending_repos.csv")