from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api

vk_implicit = vk_api.VkApi(token="39ee176cb42ab689b2bd31b02463a06db84087661fde24a9b1bb58927620ffdf9122d954db604b5a06f2a")
vk_implicit._auth_token()

vk = vk_api.VkApi(token="2736511374fb87d1ff9a1943b86e469ee1db9bbff867283f7bffe6d10b0d4bfa3fcaad7a398e7ef65f057")
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 195576338)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id == 598391185:
                userText = event.object.text
                textToWords = userText.split(" ")


                if textToWords[0] == "/server":
                    try:
                        if textToWords[1] == "add":
                            try:
                                text = vk_implicit.method("wall.get", {"owner_id": -195576338})["items"][0]["text"]
                                id = vk_implicit.method("wall.get", {"owner_id": -195576338})["items"][0]["id"]

                                vk_implicit.method("wall.delete", {"owner_id": -195576338, "post_id": id})
                                vk_implicit.method("wall.post", {"owner_id": -195576338, "from_group": 1, "message": text + "\n" + textToWords[2]})
                                vk.method("messages.send", {"peer_id": 598391185, "message": "Лицензия активирована", "random_id": 0})
                            except IndexError:
                                vk.method("messages.send", {"peer_id": 598391185,
                                                            "message": "Неверная команда. Используйте: /server add [HWID]",
                                                            "random_id": 0})
                                vk_implicit.method("wall.post", {"owner_id": -195576338, "from_group": 1, "message": text})
                        elif textToWords[1] == "remove":
                            try:
                                text = vk_implicit.method("wall.get", {"owner_id": -195576338})["items"][0]["text"]
                                id = vk_implicit.method("wall.get", {"owner_id": -195576338})["items"][0]["id"]

                                vk_implicit.method("wall.delete", {"owner_id": -195576338, "post_id": id})
                                vk_implicit.method("wall.post", {"owner_id": -195576338, "from_group": 1, "message": text.replace("\n" + textToWords[2], "")})
                                vk.method("messages.send", {"peer_id": 598391185, "message": "Лицензия удалена", "random_id": 0})
                            except IndexError:
                                vk.method("messages.send", {"peer_id": 598391185,
                                                            "message": "Неверная команда. Используйте: /server remove [HWID]",
                                                            "random_id": 0})
                        else:
                            vk.method("messages.send", {"peer_id": 598391185,
                                                        "message": "Неверная команда. Используйте: /server [add|remove] [HWID]",
                                                        "random_id": 0})
                    except IndexError:
                        vk.method("messages.send", {"peer_id": 598391185,
                                                    "message": "Неверная команда. Используйте: /server [add|remove] [HWID]",
                                                    "random_id": 0})

