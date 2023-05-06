import requests #dependency

url = "https://discord.com/api/webhooks/1104407527648677919/otG0tN0ue8tutzNlOZa4UZXAZf0TbuM81Zk01SUY92voTQ-z0suoCeHs1KbBgcyGm2MT" 


data = {
    "content" : "message content",
    "username" : "custom username"
}


data["embeds"] = [
    {
        "description" : "text in embed",
        "title" : "embed title"
    }
]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))

