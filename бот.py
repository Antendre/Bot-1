import requests
import vk_api

vk_session = vk_api.VkApi(token='c3bcd108f4be0716e61a4b0dbf28771e0d171337217aa8dc1a2625002e50e8b8173c66cec696f41685c13')

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:			
        if event.text == 'БАН' or event.text == 'бан' or event.text == 'Бан': #Если написали заданную фразу
            vk.messages.send( #Отправляем сообщение
            user_id=event.user_id,
			random_id=event.random_id,
            message='По причине пидорас'
			)
			

