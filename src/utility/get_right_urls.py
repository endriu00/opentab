from src.utility.get_group_urls import get_group_urls
from src.utility.is_url_correct import is_url_correct

# Ritorna le urls corrette oppure null
def get_right_urls(group, urls, dic):
    # prende le urls che appartengono ad un gruppo
    group_urls = get_group_urls(group, dic)
    print(group_urls)
    correct_url = list()
    # if there is no such group, every URL is 
    if group_urls == []:
        for url in urls:
            print(url)
            # vediamo se la url è corretta
            if is_url_correct(url):
                correct_url.append(url)
        return correct_url

    for url in urls:
        # vediamo se la url è corretta
        if is_url_correct(url) and url not in group_urls:
            correct_url.append(url)

    print(correct_url)
    return correct_url