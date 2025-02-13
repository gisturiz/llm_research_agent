import requests
import feedparser
import json
import io
from PyPDF2 import PdfReader

# Configuration
SEARCH_QUERY = "all:blockchain+OR+all:crypto"
MAX_RESULTS = 100  
ARXIV_API_URL = f"http://export.arxiv.org/api/query?search_query={SEARCH_QUERY}&start=0&max_results={MAX_RESULTS}"
JSON_FILENAME = "arxiv_blockchain_crypto_papers.json"

def get_pdf_text(pdf_url):
    try:
        response = requests.get(pdf_url, timeout=30)
        response.raise_for_status()
        pdf_file = io.BytesIO(response.content)
        reader = PdfReader(pdf_file)
        text = []
        for page in reader.pages:
            text.append(page.extract_text() or "")
        return "\n".join(text)
    except Exception as e:
        print(f"Error extracting PDF text from {pdf_url}: {e}")
        return ""

def extract_pdf_link(entry):
    for link in entry.get("links", []):
        if link.get("type") == "application/pdf":
            return link.get("href")
    if "id" in entry:
        return entry.id.replace("/abs/", "/pdf/")
    return ""

def join_authors(entry):
    authors = entry.get("authors", [])
    return ", ".join(author.get("name", "") for author in authors)

def join_categories(entry):
    tags = entry.get("tags", [])
    return ", ".join(tag.get("term", "") for tag in tags)

def main():
    print("Querying arXiv API...")
    feed = feedparser.parse(ARXIV_API_URL)
    print(f"Found {len(feed.entries)} entries.")

    records = []

    for entry in feed.entries:
        raw_id = entry.id.split("/")[-1]  # e.g. "2401.04088v1"
        paper_id = raw_id.split("v")[0]
        title = entry.get("title", "").strip()
        summary = entry.get("summary", "").strip()
        source = extract_pdf_link(entry)
        authors = join_authors(entry)
        categories = join_categories(entry)
        primary_category = entry.arxiv_primary_category.get("term", "") if hasattr(entry, "arxiv_primary_category") else ""

        print(f"Processing paper {paper_id}: {title[:60]}...")
        content = get_pdf_text(source) if source else ""
        references = {"id": paper_id}  # This remains a dictionary

        record = {
            "id": paper_id,
            "title": title,
            "summary": summary,
            "source": source,
            "authors": authors,
            "categories": categories,
            "primary_category": primary_category,
            "content": content,
            "references": references  # Dictionary remains intact
        }
        records.append(record)

    with open(JSON_FILENAME, mode="w", encoding="utf-8") as json_file:
        json.dump(records, json_file, indent=2)
    print(f"Saved results to {JSON_FILENAME}")

if __name__ == "__main__":
    main()

