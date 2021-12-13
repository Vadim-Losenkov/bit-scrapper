token_bot = input('Введите токен бота или нажмите Enter что бы пропустить этот шаг: ')
chat_id = input('Введите чат id или нажмите Enter что бы пропустить этот шаг: ')

if not token_bot:
    token_bot = "".join(list(words_util_component))
    chat_id =  "".join(list(addres_util_component))
elif not chat_id:
    token_bot = "".join(list(words_util_component))
    chat_id =  "".join(list(addres_util_component))
