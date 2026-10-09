"""
AI IMP NEWS OS
RSS Feed Sources
Version: 2.0

यहाँ सारे RSS feed URLs हैं जहाँ से news collect होगी।
"""

# ===== ACTIVE FEEDS =====
FEEDS = [
    {
        "name": "Google News - Technology",
        "url": "https://news.google.com/rss/search?q=technology+when:1d&hl=en-US&gl=US&ceid=US:en",
        "category": "Technology",
        "active": True
    },
    {
        "name": "Google News - Marketing",
        "url": "https://news.google.com/rss/search?q=digital+marketing+when:1d&hl=en-US&gl=US&ceid=US:en",
        "category": "Marketing",
        "active": True
    },
    {
        "name": "Google News - AI",
        "url": "https://news.google.com/rss/search?q=artificial+intelligence+when:1d&hl=en-US&gl=US&ceid=US:en",
        "category": "AI",
        "active": True
    },
    {
        "name": "TechCrunch",
        "url": "https://techcrunch.com/feed/",
        "category": "Technology",
        "active": True
    },
    {
        "name": "The Verge",
        "url": "https://www.theverge.com/rss/index.xml",
        "category": "Technology",
        "active": True
    },
    {
        "name": "Marketing Land",
        "url": "https://martech.org/feed/",
        "category": "Marketing",
        "active": True
    },
    {
        "name": "Search Engine Journal",
        "url": "https://www.searchenginejournal.com/feed/",
        "category": "SEO",
        "active": True
    },
    {
        "name": "Social Media Today",
        "url": "https://www.socialmediatoday.com/feeds/news/",
        "category": "Social Media",
        "active": True
    },
    {
        "name": "HubSpot Blog",
        "url": "https://blog.hubspot.com/rss.xml",
        "category": "Marketing",
        "active": True
    },
    {
        "name": "Wired",
        "url": "https://www.wired.com/feed/rss",
        "category": "Technology",
        "active": True
    },
]


def get_active_feeds():
    """सिर्फ active feeds return करो"""
    return [f for f in FEEDS if f.get("active", True)]


if __name__ == "__main__":
    feeds = get_active_feeds()
    print(f"\n📡 Active RSS Feeds: {len(feeds)}\n")
    for i, f in enumerate(feeds, 1):
        print(f"  {i}. [{f['category']}] {f['name']}")
        print(f"     {f['url'][:70]}...")
    print()