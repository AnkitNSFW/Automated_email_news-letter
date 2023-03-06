from api import api_news
from pprint import pprint



def embeded_image(news_dist):
    head = """<html>\n<body>"""
    bottom = """</body>\n</html>"""
    html_structure = """"""
    article_no = 1


    # Converting the fetched News into html code 
    for news in news_dist:
        html_structure += f"""<hr width:100%>\n<p>Article no: {article_no}</p>\n"""

        if news["image_url"]:
            html_structure += f""" <img src="{news["image_url"]}", width="50%", align="center">\n"""

        if news["creator"]: creator = news["creator"]
        else: creator = "Unknown"

        html_structure += f"""<a href="{news["link"]}", style="color:black;"><h1>{news["title"]}</h1></a>\n"""
        

        if str(news["description"]) in str(news["content"]):
            content_tag = "h3"
        else:
            content_tag = "p"
            html_structure += f"""<h3>{news["description"]}</h3>\n"""

        if len(news["content"])>1000:
            html_structure += f"""<{content_tag}>{news["content"][:1000]}...<a href="{news["link"]}" >read more</a></{content_tag}>\n"""
        else:
            html_structure += f""""<{content_tag}>{news["content"]}</{content_tag}>\n"""

        html_structure += f"""<p>Published at {news["pubDate"]},  Creator: {creator},  Location: {news["country"]}</p>\n"""

        article_no += 1


    return head+html_structure+"<hr>\n"+bottom
    

if __name__ =="__main__":
    pprint(embeded_image(api_news()))
