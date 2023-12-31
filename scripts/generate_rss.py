import os
import markdown2
from xml.etree.ElementTree import Element, SubElement, tostring
import yaml
import re
from datetime import date

PUBLICATION_TITLE = "SerpCompany"
PUBLICATION_DESCRIPTION = "Description of SerpCompany"
GH_PAGES_URL = "https://serpcompany.github.io/rss/"

def parse_frontmatter(content):
    # Split the content into frontmatter and body
    parts = re.split(r"---\s*", content, maxsplit=2)
    frontmatter = yaml.safe_load(parts[1])
    body = parts[2]
    return frontmatter, body


def create_rss_item(channel, title, link, description, pubDate):
    print("Creating RSS item for " + title)
    item = SubElement(channel, "item")
    SubElement(item, "title").text = title
    SubElement(item, "link").text = link
    SubElement(item, "description").text = description

    if isinstance(pubDate, date):
        pubDate = pubDate.strftime("%Y-%m-%d")

    SubElement(item, "pubDate").text = pubDate


def generate_rss(directory, output_file):
    root = Element("rss")
    root.set("version", "2.0")
    channel = SubElement(root, "channel")

    # Add general channel elements
    SubElement(channel, "title").text = PUBLICATION_TITLE
    SubElement(channel, "link").text = GH_PAGES_URL
    SubElement(channel, "description").text = PUBLICATION_DESCRIPTION

    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

                frontmatter, body = parse_frontmatter(content)
                html_content = markdown2.markdown(body)

                title = frontmatter.get("title", "No Title")
                link = frontmatter.get(
                    "link",
                    f"{GH_PAGES_URL}{filename.replace('.md', '.html')}",
                )
                description = frontmatter.get("description", html_content)
                pubDate = frontmatter.get("date", "No Date")

                create_rss_item(channel, title, link, description, pubDate)

    # Create directories and files if they don't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "wb") as f:
        f.write(tostring(root))


if __name__ == "__main__":
    print("Generating RSS feeds")
    # For every source
    for source in os.listdir("./content"):
        # For every author
        for author in os.listdir("./content/" + source):
            # Generate RSS in the RSS folder
            print("Generating " + author + " RSS feed")
            generate_rss("./content/" + source + "/" + author, "./rss/" + source + "/" + author + "/feed.xml")
