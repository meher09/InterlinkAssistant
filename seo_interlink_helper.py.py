import requests
import asyncio
import aiohttp
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)
while True:
    try:
        SIMILARITY_THRESHOLD = float(input("Enter the similarity threshold as a percentage (e.g., 10 for 10%): "))
        if 0 <= SIMILARITY_THRESHOLD <= 100:
            SIMILARITY_THRESHOLD /= 100  # Convert to decimal
            break
        else:
            print("Please enter a value between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid percentage.")



async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        logging.error(f"Error fetching content from {url}: {e}")
        return None


# Step 1: Fetch content from provided URLs
async def fetch_content(urls):
    contents = {}
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        fetched_contents = await asyncio.gather(*tasks)

    for url, content in zip(urls, fetched_contents):
        if content:
            contents[url] = content

    return contents


# Extract meaningful content from raw HTML using BeautifulSoup
def extract_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(['script', 'style']):
        tag.decompose()
    return ' '.join(soup.stripped_strings)


# Step 2: Compute TF-IDF vectors and cosine similarity
def compute_similarity(contents):
    processed_contents = [extract_content(html) for html in contents.values()]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(processed_contents)
    return cosine_similarity(tfidf_matrix)


# Step 3: Suggest interlinks based on similarity
def suggest_interlinks(urls, num_suggestions=1):
    loop = asyncio.get_event_loop()
    contents = loop.run_until_complete(fetch_content(urls))
    similarities = compute_similarity(contents)

    suggestions = {}
    no_suggestions = []   # List to keep URLs without suggestions

    for idx, url in enumerate(contents.keys()):
        sorted_indices = similarities[idx].argsort()[::-1]
        relevant_indices = [i for i in sorted_indices if similarities[idx][i] > SIMILARITY_THRESHOLD]
        suggested_urls = [list(contents.keys())[i] for i in relevant_indices[1:num_suggestions+1]]

        # Check if the URL has any suggested links, if not, add to no_suggestions list
        if not suggested_urls:
            no_suggestions.append(url)
        else:
            suggestions[url] = suggested_urls

    return suggestions, no_suggestions



def save_no_suggestions_to_file(urls, filename="no_suggestions.txt"):
    """Save URLs without suggestions to a separate file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')


# Save suggestions to CSV
def save_to_csv(suggestions, output_file, num_suggestions):
    headers = ["URL"] + [f"Suggested Link {i+1}" for i in range(num_suggestions)]
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for url, links in suggestions.items():
            row = [url] + links
            writer.writerow(row)


# Load URLs from text file
with open('urls.txt', 'r') as file:
    urls = [line.strip() for line in file]

while True:
    try:
        num_suggestions = int(input("Enter the number of suggested links you'd like for each URL (max 5): "))
        if 1 <= num_suggestions <= 5:
            break
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")

suggestions, no_suggestions = suggest_interlinks(urls, num_suggestions)
save_to_csv(suggestions, 'interlink_suggestions.csv', num_suggestions)
if no_suggestions:
    save_no_suggestions_to_file(no_suggestions, 'no_suggestions.txt')