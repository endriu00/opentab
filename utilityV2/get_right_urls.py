from get_group_urls import get_group_urls
from is_url_correct import is_url_correct

# Ritorna le urls corrette oppure null
def get_right_urls(group, *urls):
    # prende le urls che appartengono ad un gruppo
    dic_urls = get_group_urls(group)
    corret_url = list()
    # se il gruppo non esiste tutte le urls vanno bene
    if not dic_urls:
        for url in urls:
            # vediamo se la url è corretta
            if is_url_correct(url):
                corret_url.append(url)
        return corret_url

    for url in urls:
        # vediamo se la url è corretta
        if is_url_correct(url) and url not in dic_urls:
            corret_url.append(url)

    return corret_url