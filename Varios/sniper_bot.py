from requests_html import HTMLSession, AsyncHTMLSession

url = "https://www.youtube.com/watch?v=sgWVA-0zezA"

session = HTMLSession()
t =  session.get(url)
t.html.find("")