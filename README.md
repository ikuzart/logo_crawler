# Crawler for logo images

### How it works
Crawler creates instances of all enities - Downloader, Logo_finder, Seed, etc

Seed - yields urls for crawling
Downloader - It's job is to get html page from url, it sends HTTP request and checks responses,
            not implemented advanced features like cache, user_agents, proxy, etc.
LogoFinder -  Searches for Signatures on HTML page
Signature - Some rule for tag, which helps identify logo


### How to run
```python3 logo_crawler.crawler.py domains.csv```
where domains.csv is a list with urls


### Dependencies
requests - since it recommended in official docs
beutifulsoup4 - easiest way to navigating, searching, and modifying the parse tree

