overall_dict = {}
queue = []
count = 0
games_url_base = "games/?tab=all"
friends_url_base = "friends/"

while(len(queue)!= 0):
    scrape_website(overall_dict,queue)
# Function that scrapes steam and returns
# 1) Game name list (game_list)
# 2) Game hours list (game_hours_list)
# 3) Friends url (friends_url)
def scrape_website(overall_dict,queue):
    import urllib2
    import re
    from bs4 import BeautifulSoup
    games_page = 'http://steamcommunity.com/id/stabstabstab/games/?tab=all'
    page = urllib2.urlopen(games_page)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find('script',attrs={'language': 'javascript'})
    name = name_box.text
    print(name)
    p = re.compile('"name":"(.*?)"')
    game_list = p.findall(name)
    print(game_list)
    p = re.compile('"hours_forever":"(.*?)"')
    game_hours_list = p.findall(name)
    for i in range(0,len(game_hours_list)):
        game_hours_list[i] = float(str(game_hours_list[i]).replace(",",""))
    print(game_hours_list)
    friends_page = "http://steamcommunity.com/id/stabstabstab/friends/"
    page = urllib2.urlopen(friends_page)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find("div" ,id="BG_bottom")
    print(name_box)
    name = name_box.find_all('a')
    print(name)
    p = re.compile('href="(.*?)"')
    friends_url = p.findall(str(name))
    print(friends_url)
# Create  hash table with all urls
# Call function for each url
# Add to hash table for each friends url

# Create a ratio of total hours played for a game
# over sum of total hours played by all games by a
# user.

# Create 10C2 of top 10 games played and pair them
# with another game (for 45? combinations). Make a
# count of the highest paired games
