import requests



user=""

user_anime_list=[]
API=""
CLIENT_ID=API



def request():
    response = requests.get(url, headers = {
        'X-MAL-CLIENT-ID': CLIENT_ID
        })

    response.raise_for_status()
    global anime_list
    anime_list = response.json()

    response.close()

def init():
    global url
    url = f'https://api.myanimelist.net/v2/users/{user}/animelist?fields=id,title,mean'
    #delete list_of_animes.txt
    with open("list_of_animes.txt","w") as f:
        f.write("")
def main():
    global url
    while True:
        request()
        for i in range(len(anime_list["data"])):
            anime= anime_list["data"][i]["node"]["title"]
            print(anime)
            with open("list_of_animes.txt","a", encoding="utf-8") as f:
                f.write(f"{anime}\n")
        #print(user_anime_list)
        if "next" not in anime_list["paging"]:
            break
        url=anime_list["paging"]["next"]

if __name__=="__main__":
    init()
    main()






