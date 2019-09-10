from urllib.parse import urlparse

def validate_url(url):
    """
        Args: url
        Validate an url by using the urlpase function
        and validate it actually has a net location.
        {https://stackoverflow.com/a/50352868/10621985}

        http://www.cwi.nl:80/%7Eguido/Python.html
        scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html'
    """
    result = urlparse(url)
    return (all([result.scheme, result.netloc, result.path])
        and len(result.netloc.split(".")) > 1)

