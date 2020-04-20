from json import loads, dumps
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.conf import settings
import requests
from words.models import Word
from registrations.models import User
from django.db.models import Q
from googletrans import Translator


PROXIES = {'http': 'socks5h://127.0.0.1:9170',
           'https': 'socks5h://127.0.0.1:9170'}
STR = '''
───────────────█────█───█───────────────
──────────██──███──███─████─███──██─────
─────████─█████─████─███─████─█─████─█──
──████──███──██──██───█───██──███─█████─
─██─███──██────────────────────█──██──█─
──█──█───────────────────────────────██─
──██─────────────────────────────────██─
──██─────────────────────────────────██─
───█─────────────────────────────────██─
───█─────────────────────────────────█──
───██───────────────────────────────██──
───██───────────────────────────────██──
───██───────────────────────────────██──
───██───────────────────────────────██──
───██───────────────────────────────██──
───██──────────────────────────────███──
───█──────████─────────────████────███──
──██───████───███───────███───████───██─
──██──██────────██─────█──────────██─██─
───███────────────█───█────────────███──
────█─────────────██─█──────────────██──
───██─────██───────█─█───────██─────██──
───██─────██───────█─██──────██─────██──
───██─────────────█───██───────────██───
────██───────────█─────██─────────████──
──██████────────█───────██──────██──███─
─██──█─███████████─────██─██████───█──██
─█──█────────────███████────────────█──█
─██─██─────────────────────────────██─██
──██─█─────────────────────────────█─██─
────────────────────────────────────────'''


def get_word_translation(word, lang):
    translator = Translator()
    print(lang)
    LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
        'fil': 'Filipino',
        'he': 'Hebrew'
    }
    if not LANGUAGES.get(lang):
        lang = 'en'
    return translator.translate(word, dest=lang).text


class TelegramBot(View):

    def post(self, request):
        try:
            r = loads(request.body)
        except TypeError:
            string = request.body.decode(encoding='utf-8')
            r = loads(string, encoding='utf-8')
        try:
            chat_id = r['message']['chat']['id']
            data = {'message': r['message']['text'].strip()}
        except BaseException:
            context = {
                'message': 'Error',
            }
            return JsonResponse(
                context, safe=False, json_dumps_params={
                    'ensure_ascii': False})
        print(chat_id, data)
        args = {'data': {'chat_id': f"{chat_id}"}}
        # self.delete_message(r)
        if User.objects.filter(chat_id=chat_id).first():
            if data['message'].split(' ')[0] == '/add':
                print('aa', data['message'].split(' '))
                if len(data['message'].split(' ')) == 3:
                    print('add')
                    user = User.objects.filter(chat_id=chat_id).first()
                    Word.objects.create(user=user, word_translation=data['message'].split(
                        ' ')[1].lower(), word_to_learn=data['message'].split(' ')[2].lower())

                    args['data']['text'] = f"add {data['message'].split(' ')[1]}"
                    self.telegram_send('sendMessage', args)
                else:
                    args['data']['text'] = f"add error"
                    self.telegram_send('sendMessage', args)

            elif data['message'].split(' ')[0] == '/all':
                # response = Text2SignView.as_view()(request=self.request, **data)
                # string = response.content.decode('utf-8')
                # json_obj = loads(string)
                # self.send_media(chat_id, json_obj['words'], json_obj['signs'])
                words = ' '.join(
                    ['/' + word.word_translation for word in Word.objects.filter(user__chat_id=chat_id)])
                args['data']['text'] = words
                self.telegram_send('sendMessage', args)
            elif data['message'].split(' ')[0] == '/trans' and len(data['message'].split(' ')) >= 3:
                # trans = Word.objects.filter(
                #     user__chat_id=chat_id).filter(
                #     Q(
                #         word_translation=(
                #             data['message'].split(' ')[1].lower())) | Q(
                #         word_to_learn=(
                #             data['message'].split(' ')[1].lower()))).first()
                text = data['message'].replace(data['message'].split(
                    ' ')[0] + ' ' + data['message'].split(' ')[1], '')
                if text:
                    args['data']['text'] = f"{text} : {get_word_translation(text, data['message'].split(' ')[1].lower())}"
                    self.telegram_send('sendMessage', args)
                    # args['data']['text'] = STR
                    # self.telegram_send('sendMessage', args)
                else:
                    args['data']['text'] = f"Error"
                    self.telegram_send('sendMessage', args)

            elif data['message'].split(' ')[0].startswith('/') and len(data['message'].split(' ')) == 1:
                trans = Word.objects.filter(
                    user__chat_id=chat_id).filter(
                    Q(
                        word_translation=(
                            data['message'].split('/')[1].lower())) | Q(
                        word_to_learn=(
                            data['message'].split('/')[1].lower()))).first()
                if trans:
                    args['data']['text'] = f"{trans.word_translation} : {trans.word_to_learn}"
                    self.telegram_send('sendMessage', args)
                    # args['data']['text'] = STR
                    # self.telegram_send('sendMessage', args)
                else:
                    args['data']['text'] = f"Error"
                    self.telegram_send('sendMessage', args)
            else:
                args['data']['text'] = 'моя твоя непонимать'
                self.telegram_send('sendMessage', args)
        else:
            if data['message'].split(' ')[0].startswith(
                    '/reg') and len(data['message'].split(' ')) == 3:
                self.registration_user(
                    chat_id=chat_id,
                    login=data['message'].split(' ')[1],
                    key=data['message'].split(' ')[2])
            else:
                args['data']['text'] = 'зарегайся'
                self.telegram_send('sendMessage', args)
        return JsonResponse(
            data, safe=False, json_dumps_params={
                'ensure_ascii': False})

    @staticmethod
    def telegram_send(method, args):
        url_send_media = f'{settings.URL_BOT}{method}'
        return requests.post(url_send_media, **args, proxies=PROXIES)

    @staticmethod
    def delete_message(r):
        chat_id = r['message']['chat']['id']
        message_id = r['message']['message_id']

        for id in range((message_id - 150), message_id):
            url_send_media = f'{settings.URL_BOT}deleteMessage?chat_id={chat_id}&message_id={id}'
            requests.post(url_send_media, proxies=PROXIES)

        return JsonResponse(
            {'delete': 'True'}, safe=False, json_dumps_params={
                'ensure_ascii': False})

    @staticmethod
    def registration_user(chat_id, login, key):
        user = User.objects.filter(username=login)
        args = {'data': {'chat_id': f"{chat_id}"}}
        if user:
            if user.first().reg_ok:
                args['data']['text'] = f"Вы уже зарегестрированы"
                TelegramBot.telegram_send('sendMessage', args)
            elif user.first().reg_key == key:
                user.update(chat_id=chat_id, reg_ok=True)
                args['data']['text'] = f"Reg ok"
                TelegramBot.telegram_send('sendMessage', args)
            else:
                args['data']['text'] = f"Error key"
                TelegramBot.telegram_send('sendMessage', args)
        else:
            args['data']['text'] = f"Registration error login"
            TelegramBot.telegram_send('sendMessage', args)
