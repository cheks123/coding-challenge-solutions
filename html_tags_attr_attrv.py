from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]

html ='''<!--[if IE 9]>IE9-specific content
<![endif]-->
<div height='9px'>Welcom to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->'''

parser = MyHTMLParser()
parser.feed(html)
parser.close()


