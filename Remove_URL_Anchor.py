# Create function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"


url = "www.codewars.com"
def remove_url_anchor(url):
    splitted_url = url.split("#")
    new_url = splitted_url[0]
    return new_url

print(remove_url_anchor(url))