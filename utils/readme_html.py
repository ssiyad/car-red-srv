from functools import cache

from markdown import markdown


@cache
def readme_html():
    with open('README.md') as f:
        return markdown(f.read(), extensions=['fenced_code'])

