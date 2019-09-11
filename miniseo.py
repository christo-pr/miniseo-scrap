import re
from collections import Counter

def collect(site):
    """
        Args: site
        Scrapp all the site
    """

    data = { "metrics": {} }

    data["metrics"]["head"] = _get_head_results(site)
    data["metrics"]["links"] = _get_links_results(site)
    data["metrics"]["og_tags"] = _get_og_results(site)
    data["metrics"]["headers_tags"] = _get_headers_tags_results(site)
    data["metrics"]["images"] = _get_images_results(site)

    return data

def _get_head_results(site):
    """
        This method will search for
        * Title tag
        * Meta description tag
        * Canonical tag
    """
    title = site.title
    meta_description = site.find("meta", { "name":"description" })
    canonical_tag = site.find("link", rel="canonical")

    return {
        "values": {
            "title tag": title.text if title else "",
            "meta description": meta_description.get("content", "") if meta_description else "",
            "canonical": canonical_tag.get("href", "") if canonical_tag else ""
        },
        "meta": [],
        "points": {
            "total": 3,
            "passed": len(list(filter(bool, [title, meta_description, canonical_tag])))
        }
    }

def _get_links_results(site):
    """
        This method will search for
        * counts of links
        * no follow count
    """
    links = site.find_all('a')
    no_follow_links = list(filter(lambda l: "nofollow" in l.get('rel', ""), links if links else []))

    return {
        "values": {},
        "meta": [
            { "links count": len(links) },
            { "nofollow links count": len(no_follow_links) }
        ],
        "points": {
            "total": 1,
            "passed": len(no_follow_links)
        }
    }

def _get_og_results(site):
    """
        This method will search for og tags:
        * title
        * type
        * description
        * image
        * url
    """
    og_tags = site.find_all("meta", { "property": re.compile("og:*")}, limit=5)
    values = { tag["property"]: tag["content"] for tag in og_tags }

    return {
        "values": values,
        "meta": [],
        "points": {
            "total": 5,
            "passed": len(og_tags)
        }
    }

def _get_headers_tags_results(site):
    """
        This method will search:
        * h1...h6 tags count
    """
    headers = site.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    h1_tag = site.find('h1')
    headers_counter = Counter(list(map(lambda h:  h.name, headers)))

    return {
        "values": {
            "h1": h1_tag.text if h1_tag else "",
        },
        "meta": [{tag: count} for tag, count in headers_counter.most_common()],
        "points": {
            "total": 1,
            "passed": 1 if headers_counter["h1"] > 0 and headers_counter["h1"] < 2 else 0
        }
    }

def _get_images_results(site):
    """
        This method will search:
        * images count
        * images with alt attr count
    """
    images = site.find_all('img')
    images_count = len(images)
    images_alt_count = len(list(filter(lambda i: i.get('alt', False), images)))
    return {
        "values": {},
        "meta": [
            { "images count": images_count },
            { "images alt count": images_alt_count  }
        ],
        "points": {
            "total": images_count,
            "passed": images_alt_count
        }
    }
