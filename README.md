# README

This repository (`https://github.com/serpcompany/rss`) is meant to generate RSS feeds that will be updated as content (written in markdown) is added to the `/content/` directory and committed to the remote repository, orchestrated by github actions & served with github pages.


## Content

Each subdirectory corresponds to a particular service that will listen for it:

- `/content/substack/serpai/`
- `/content/substack/devinschumacher/`
- `/content/medium/serpai/`
- `/content/medium/devinschumacher/`
- `/content/hashnode/serpai/`
- `/content/hashnode/devinschumacher/`


## RSS Feed Generators

There is a `/scripts/generate_rss.py` script that generates RSS feeds for each of the services, based on the structure of the directories above, and served from github pages, for example:

- `https://serpcompany.github.io/rss/substack/serpai/feed.xml`
- `https://serpcompany.github.io/rss/substack/devinschumacher/feed.xml`
- `https://serpcompany.github.io/rss/medium/serpai/feed.xml`
- `https://serpcompany.github.io/rss/medium/devinschumacher/feed.xml`
- `https://serpcompany.github.io/rss/hashnode/serpai/feed.xml`
- `https://serpcompany.github.io/rss/hashnode/devinschumacher/feed.xml`


## Github Actions

Github actions are intended to create/update the RSS feeds for each of the services as new markdown files are committed to the repository.

- `.github/workflows/rss-substack-serpai.yml`
- `.github/workflows/rss-substack-devinschumacher.yml`
- `.github/workflows/rss-medium-serpai.yml`
- `.github/workflows/rss-medium-devinschumacher.yml`
- `.github/workflows/rss-hashnode-serpai.yml`
- `.github/workflows/rss-hashnode-devinschumacher.yml`

