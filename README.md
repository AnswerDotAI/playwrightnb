# PlaywrightNB


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

`PlaywriteNB` provides some little quality-of-life helpers for
interactive use of the wonderful
[Playwright](https://playwright.dev/python/) library. It’s likely to be
particularly of interest to folks using Jupyter.

## Install

    pip install playwrightnb

## Overview

``` python
from playwrightnb import *
from html.parser import HTMLParser
```

`playwrightnb` provide two main functions: `read_page_async(url)`, and
`read_page(url)`. They are identical except the 1st is async.

They return a tuple of the main HTML page contents, and a dict mapping
iframe IDs to their HTML contents. They handle Javascript and other
trickiness largely automatically, however you can pass a `pause`
parameter (in milliseconds) if you need to insert some manual waits. You
can also pass a `timeout` (also in milliseconds).

For instance, the Dyalog APL help information is provided inside an
iframe that’s dynamically loaded by JS, but we are able to read it
directly:

``` python
sh_url = 'https://help.dyalog.com/19.0/#UserGuide/Installation%20and%20Configuration/Shell%20Scripts.htm'
```

``` python
cts,iframes = read_page(sh_url)
txt = iframes['topic']
```

``` python
class HTMLTextExtractor(HTMLParser):
    def handle_data(self, data): self.text.append(data.strip())

parser = HTMLTextExtractor()
parser.text = []
parser.feed(txt)
extracted_text = ' '.join(filter(None, parser.text))
print(extracted_text[:100])
```

    Shell Scripts Open topic with navigation Old Release Notes > Release Notes – Dyalog v18.2 > Shell Sc
