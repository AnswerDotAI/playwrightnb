import nest_asyncio,asyncio
from playwright.sync_api import PlaywrightContextManager, sync_playwright
from fastcore.utils import patch

nest_asyncio.apply()

PlaywrightContextManager.orig_pcm = PlaywrightContextManager.__enter__
_orig_exit = PlaywrightContextManager.__exit__

@patch
def __enter__(self:PlaywrightContextManager):
    def _exit(): _orig_exit(self)
    orig = asyncio.BaseEventLoop.is_running
    asyncio.BaseEventLoop.is_running = lambda self: False
    try:
        res = self.orig_pcm()
        res.stop = _exit
        return res
    finally: asyncio.BaseEventLoop.is_running = orig

@patch
def __exit__(self:PlaywrightContextManager, *args, **kwargs): pass

def get_page(*args, **kw):
    "Get a new page in a Chromium browser, passing any arguments to `launch`"
    with sync_playwright() as p:
        page = p.chromium.launch(*args, **kw).new_context().new_page()
        page.stop = p.stop
        return page

