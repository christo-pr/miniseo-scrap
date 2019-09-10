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
    meta_description = site.find("meta", {"name":"description"})
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
            "passed": _calculate_points(title, meta_description, canonical_tag)
        }
    }

def _get_links_results(site):
    """
        This method will search for
        * counts of links
        * no follow count
    """
    links = site.find_all('a')
    no_follow_links = None
    if links:
        no_follow_links = list(filter(lambda l: "nofollow" in l.get('rel', ""), links))

    return {
        "values": {},
        "meta": [
            { "links count": len(links) },
            { "nofollow links count": len(no_follow_links) }
        ],
        "points": {
            "total": 2,
            "passed": _calculate_points(links, len(no_follow_links))
        }
    }

def _get_og_results(site):
    """
        This method will search for og tags:
        * title
        * type
        * type
        * description
        * image
    """
    return {
        "values": {},
        "meta": [
            { "links count": "" },
            { "nofollow links count": "" }
        ],
        "points": ""
    }

def _get_headers_tags_results(site):
    """
        This method will search:
        * h1...h6 tags count
    """
    return {
        "values": {
            "h1": "",
            # ...
        },
        "meta": [
            { "h1 count": "" },
            # ..
        ],
        "points": ""
    }

def _get_images_results(site):
    """
        This method will search:
        * images count
        * images with alt attr count
    """
    return {
        "values": {},
        "meta": [
            { "images count": "" },
            { "images alt count": "" }
        ],
        "points": ""
    }


def _calculate_points(*args):
    """
        This method will calculate the points based on the params
        by just checking if the given param is not None
    """

    return len(list(filter(bool, args)))
