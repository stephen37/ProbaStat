#!/usr/bin/env python -tt
import urllib.request, urllib.error, urllib.parse
from lxml.html import fromstring
import sys
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True,
                    type=argparse.FileType("wt", encoding="utf-8"))
args = parser.parse_args()
urlprefix = "http://www.winespectator.com/dailypicks/category/catid/{}/page/{}"
for catid, max_page in [(1, 830), (2, 816), (3, 806)]:
    for page in range(1, max_page + 1):
        out = "-> On page {} of {}....      {:.2%}%"
        print(out.format(page, max_page, page / max_page))
        try:
            response = urllib.request.urlopen(urlprefix.format(catid, page))
            html = response.read()
            dom = fromstring(html)
            sels = dom.xpath(’//div[(@class="paragraph")]’)
    except Exception as e:
        print(e)
        continue
    for review in sels:
        if review.text:
            args.output.write("BEGIN NOW " + review.text.strip() + " END\n")
            time.sleep(2)
        
