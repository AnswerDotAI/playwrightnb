# playwrightnb

This is a Python module that lets you use sync mode Playwright interactively, inside a Jupyter notebook.

To use it:

```python
from playwrightnb import get_page
page = get_page()
page.goto('http://example.org');
# ... do things with `page`...
page.stop()
```

Unlike non-jupyter usage, you don't use a context manager, but instead use `stop` when you're done to close the browser session (or to be more precise -- internally we still use a context manager, but we patch it to not auto-close). `get_page` only returns the page object, not the browser or playwright objects. You should still be able to perform most common web scraping tasks effectively, such as:

- Navigating to pages using `page.goto()`
- Waiting for elements to load with `page.wait_for_selector()`
- Extracting data from the page using methods like `page.query_selector()`, `page.query_selector_all()`, `page.text_content()`, etc.
- Interacting with elements using `page.click()`, `page.type()`, `page.hover()`, and more
- Evaluating JavaScript with `page.evaluate()`

However, there are a few capabilities you might miss out on without direct access to the browser or playwright objects:

1. Launching multiple browser contexts or pages simultaneously
2. Configuring browser-specific settings or permissions
3. Accessing browser-level methods like `browser.new_page()` or `browser.close()`

For most scraping scenarios, having the page object alone should suffice. But if you need more advanced control, use the following code as a starting point (which is identical to the source of `get_page`):

```python
with sync_playwright() as p:
    browser = p.chromium.launch(*args, **kw)
    page = browser.new_context().new_page()
    page.stop = p.stop
```

