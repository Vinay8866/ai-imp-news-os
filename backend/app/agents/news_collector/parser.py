"""
AI IMP NEWS OS
RSS Feed Parser
Version: 2.0

feedparser library से RSS parse करता है।
"""

import hashlib
import re
from datetime import datetime

import feedparser


def clean_html(text):
    """HTML tags हटाओ"""
    if not text:
        return ""
    # Remove HTML tags
    clean = re.sub(r"<[^>]+>", " ", text)
    # Remove extra whitespace
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean


def make_hash(title, link):
    """Unique hash बनाओ (duplicate detection के लिए)"""
    raw = f"{title}|{link}".encode("utf-8")
    return hashlib.md5(raw).hexdigest()


def extract_image(entry):
    """RSS entry से image URL निकालो"""
    # Try media_content
    if hasattr(entry, "media_content") and entry.media_content:
        for media in entry.media_content:
            if media.get("type", "").startswith("image") or media.get("url"):
                return media.get("url", "")

    # Try media_thumbnail
    if hasattr(entry, "media_thumbnail") and entry.media_thumbnail:
        return entry.media_thumbnail[0].get("url", "")

    # Try enclosures
    if hasattr(entry, "enclosures") and entry.enclosures:
        for enc in entry.enclosures:
            if enc.get("type", "").startswith("image"):
                return enc.get("href", "")

    # Try links
    if hasattr(entry, "links"):
        for link in entry.links:
            if link.get("type", "").startswith("image"):
                return link.get("href", "")

    return None


def parse_feed(feed_url, source_name="", category=""):
    """
    एक RSS feed parse करो और articles list return करो।

    Returns: list of dicts
    """
    articles = []

    try:
        print(f"  📡 Fetching: {source_name or feed_url[:50]}...")
        feed = feedparser.parse(feed_url)

        if feed.bozo and not feed.entries:
            print(f"  ⚠️  Parse warning for {source_name}: {feed.bozo_exception}")
            return articles

        for entry in feed.entries:
            title = clean_html(entry.get("title", ""))
            link = entry.get("link", "")

            if not title or not link:
                continue

            # Summary
            summary = ""
            if hasattr(entry, "summary"):
                summary = clean_html(entry.summary)
            elif hasattr(entry, "description"):
                summary = clean_html(entry.description)

            # Truncate long summary
            if len(summary) > 500:
                summary = summary[:500] + "..."

            # Published date
            published = ""
            if hasattr(entry, "published"):
                published = entry.published
            elif hasattr(entry, "updated"):
                published = entry.updated
            else:
                published = datetime.now().strftime("%Y-%m-%d")

            # Image
            image = extract_image(entry)

            article = {
                "title": title,
                "link": link,
                "summary": summary,
                "published": published,
                "source": source_name,
                "category": category,
                "hash": make_hash(title, link),
                "image": image,
                "score": 0
            }
            articles.append(article)

        print(f"  ✅ {source_name}: {len(articles)} articles found")

    except Exception as e:
        print(f"  ❌ Error parsing {source_name}: {e}")

    return articles


if __name__ == "__main__":
    # Test with one feed
    test_url = "https://techcrunch.com/feed/"
    results = parse_feed(test_url, "TechCrunch", "Technology")
    print(f"\n📊 Total: {len(results)} articles")
    if results:
        print(f"\nSample:")
        print(f"  Title : {results[0]['title'][:60]}")
        print(f"  Source: {results[0]['source']}")
        print(f"  Hash  : {results[0]['hash'][:16]}...")