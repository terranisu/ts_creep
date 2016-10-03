import cfscrape

class TicketSwapScrapper(object):
    def __init__(self, url):
        self.url = url
        self.scrapper = self.get_scrapper()

    def get_scrapper(self):
        return cfscrape.create_scraper()

    def get_content(self):
        return self.scrapper.get(self.url).content


#
#
# var reloadtime = Math.floor(Math.random() * 12000) + 11000;
#
# setTimeout(function () { location.reload(1); }, reloadtime);
# addCard();
#
# def start_requests(self):
#     cf_requests = []
#     for url in self.start_urls:
#       token, agent = cfscrape.get_tokens(url, 'https://www.ticketswap.nl/event/frank-carter-the-rattlesnakes-/dae96a33-5093-4218-b2fe-3db3b2681450')
#       cf_requests.append(Request(url=url,
#                       cookies=token,
#                       headers={'ticketswap': agent}))
#     return cf_requests
#
# function addCard() {
#     var cardOrder = $(".event_list").find(".type");
#     if($(".event_list")[0]){
#         $(".event_list").not(":has('.sold')").click();
#     }
# }
