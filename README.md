# Crawler for logo images

### How it works
Crawler creates instances of all enities - Downloader, Logo_finder, Seed, etc

Seed - yields urls for crawling
Downloader - It's job is to get html page from url, it sends HTTP request and checks responses,
            not implemented advanced features like cache, user_agents, proxy, etc.
LogoFinder -  Searches for Signatures on HTML page
Signature - Some rule for tag, which helps identify logo


### Scaling
More scalabble and better suited version for production will be splitted to smaller parts which will be communicating 
with each other by Message Queue (some additional service is needed, RabbitMq for example).

Downloader will be taking url from message queue, processing it and putting downloaded page to another message queue.

LogoFinder will be taking downloaded page from queue process it and put for message queue for saving to csv, db, etc.

By this approach we could have many instances of Downloader and LogoFinder working in parallel


### How to run
```python3 logo_crawler/crawler.py domains.csv```
where domains.csv is a list with urls


### Dependencies
requests - since it recommended in official docs
beutifulsoup4 - easiest way to navigating, searching, and modifying the parse tree

