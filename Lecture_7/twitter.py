import re

def main():
    url = input("URL: ").strip()
    
    # username = url.replace("https://twitter.com/", "")
    # username = url.removeprefix("https://twitter.com/")
    
    # username = extract_username(url)
    # username = search_username(url)
    username = search_username_pythonic(url)
    
    print(f"Username: {username}")


def extract_username(url):
    return re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    
    
def search_username(url):
    if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
        return matches.group(3) # 3 is the index for the third (...) gorup where the username should bee
                                # the first group is for "https?://" and the second for "www\."
    return None


def search_username_pythonic(url):
    if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
        return matches.group(1) # the first and second groups are non-capturing versions (?:...)
                                # so are not counted in matches.group() like function above
    return None

    
if __name__ == "__main__":
    main()