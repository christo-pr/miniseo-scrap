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

    return {
        "values": {
            "title tag": "",
            "meta description": "",
            "canonical": ""
        },
        "meta": [],
        "points": ""
    }

def _get_links_results(site):
    """
        This method will search for
        * counts of links
        * no follow count
    """
    return {
        "values": {},
        "meta": [
            { "links count": "" },
            { "nofollow links count": "" }
        ],
        "points": ""
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
