import os
import argparse
import markdown2
from xml.etree.ElementTree import Element, SubElement, tostring
import yaml
import re
from datetime import date


def parse_frontmatter(content):
    # Split the content into frontmatter and body
    parts = re.split(r"---\s*", content, maxsplit=2)
    frontmatter = yaml.safe_load(parts[1])
    body = parts[2]
    return frontmatter, body


def create_rss_item(channel, title, link, description, pubDate):
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
    SubElement(channel, "title").text = "Your Publication Title"
    SubElement(channel, "link").text = "http://your-publication-url.com"
    SubElement(channel, "description").text = "Description of your publication"

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
                    f"http://your-publication-url.com/{filename.replace('.md', '.html')}",
                )
                description = frontmatter.get("description", html_content)
                pubDate = frontmatter.get("date", "No Date")

                create_rss_item(channel, title, link, description, pubDate)

    with open(output_file, "wb") as f:
        f.write(tostring(root))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Source directory")
    parser.add_argument("--output", required=True, help="Output RSS file")
    args = parser.parse_args()

    generate_rss(args.source, args.output)
