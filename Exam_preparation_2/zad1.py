from collections import deque
from typing import Deque

suggested_links: Deque[int] = deque(int(x) for x in input().split())
featured_articles: list[int] = [int(x) for x in input().split()]
target_engagement_value: int = int(input())

final_feed: list[int] = []

while suggested_links and featured_articles:
    link: int = suggested_links.popleft()
    article: int = featured_articles.pop()

    if link == article:
        final_feed.append(0)

    elif link > article:
        remainder = link % article
        final_feed.append(-remainder)

        if remainder != 0:
            suggested_links.append(remainder * 2)

    else:
        remainder = article % link
        final_feed.append(remainder)

        if remainder != 0:
            featured_articles.append(remainder * 2)

print("Final Feed: ", end="")
print(*final_feed, sep= ", ")

if sum(final_feed) >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {sum(final_feed)}")
else:
    print(f"Goal not achieved! Short by: {target_engagement_value - sum(final_feed)}")