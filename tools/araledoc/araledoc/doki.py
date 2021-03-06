#!/usr/bin/env python

import re
import misaka as m
from tornado import escape
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

__all__ = ['markdown']

_emoji_list = [
    "-1", "0", "1", "109", "2", "3", "4", "5", "6", "7", "8", "8ball", "9",
    "a", "ab", "airplane", "alien", "ambulance", "angel", "anger", "angry",
    "apple", "aquarius", "aries", "arrow_backward", "arrow_down",
    "arrow_forward", "arrow_left", "arrow_lower_left", "arrow_lower_right",
    "arrow_right", "arrow_up", "arrow_upper_left", "arrow_upper_right",
    "art", "astonished", "atm", "b", "baby", "baby_chick", "baby_symbol",
    "balloon", "bamboo", "bank", "barber", "baseball", "basketball", "bath",
    "bear", "beer", "beers", "beginner", "bell", "bento", "bike", "bikini",
    "bird", "birthday", "black_square", "blue_car", "blue_heart", "blush",
    "boar", "boat", "bomb", "book", "boot", "bouquet", "bow", "bowtie",
    "boy", "bread", "briefcase", "broken_heart", "bug", "bulb",
    "bullettrain_front", "bullettrain_side", "bus", "busstop", "cactus",
    "cake", "calling", "camel", "camera", "cancer", "capricorn", "car",
    "cat", "cd", "chart", "checkered_flag", "cherry_blossom", "chicken",
    "christmas_tree", "church", "cinema", "city_sunrise", "city_sunset",
    "clap", "clapper", "clock1", "clock10", "clock11", "clock12", "clock2",
    "clock3", "clock4", "clock5", "clock6", "clock7", "clock8", "clock9",
    "closed_umbrella", "cloud", "clubs", "cn", "cocktail", "coffee",
    "cold_sweat", "computer", "confounded", "congratulations",
    "construction", "construction_worker", "convenience_store", "cool",
    "cop", "copyright", "couple", "couple_with_heart", "couplekiss", "cow",
    "crossed_flags", "crown", "cry", "cupid", "currency_exchange", "curry",
    "cyclone", "dancer", "dancers", "dango", "dart", "dash", "de",
    "department_store", "diamonds", "disappointed", "dog", "dolls",
    "dolphin", "dress", "dvd", "ear", "ear_of_rice", "egg", "eggplant",
    "egplant", "eight_pointed_black_star", "eight_spoked_asterisk",
    "elephant", "email", "es", "european_castle", "exclamation", "eyes",
    "factory", "fallen_leaf", "fast_forward", "fax", "fearful", "feelsgood",
    "feet", "ferris_wheel", "finnadie", "fire", "fire_engine", "fireworks",
    "fish", "fist", "flags", "flushed", "football", "fork_and_knife",
    "fountain", "four_leaf_clover", "fr", "fries", "frog", "fuelpump", "gb",
    "gem", "gemini", "ghost", "gift", "gift_heart", "girl", "goberserk",
    "godmode", "golf", "green_heart", "grey_exclamation", "grey_question",
    "grin", "guardsman", "guitar", "gun", "haircut", "hamburger", "hammer",
    "hamster", "hand", "handbag", "hankey", "hash", "headphones", "heart",
    "heart_decoration", "heart_eyes", "heartbeat", "heartpulse", "hearts",
    "hibiscus", "high_heel", "horse", "hospital", "hotel", "hotsprings",
    "house", "hurtrealbad", "icecream", "id", "ideograph_advantage", "imp",
    "information_desk_person", "iphone", "it", "jack_o_lantern",
    "japanese_castle", "joy", "jp", "key", "kimono", "kiss", "kissing_face",
    "kissing_heart", "koala", "koko", "kr", "leaves", "leo", "libra", "lips",
    "lipstick", "lock", "loop", "loudspeaker", "love_hotel", "mag",
    "mahjong", "mailbox", "man", "man_with_gua_pi_mao", "man_with_turban",
    "maple_leaf", "mask", "massage", "mega", "memo", "mens", "metal",
    "metro", "microphone", "minidisc", "mobile_phone_off", "moneybag",
    "monkey", "monkey_face", "moon", "mortar_board", "mount_fuji", "mouse",
    "movie_camera", "muscle", "musical_note", "nail_care", "necktie", "new",
    "no_good", "no_smoking", "nose", "notes", "o", "o2", "ocean", "octocat",
    "octopus", "oden", "office", "ok", "ok_hand", "ok_woman", "older_man",
    "older_woman", "open_hands", "ophiuchus", "palm_tree", "parking",
    "part_alternation_mark", "pencil", "penguin", "pensive", "persevere",
    "person_with_blond_hair", "phone", "pig", "pill", "pisces", "plus1",
    "point_down", "point_left", "point_right", "point_up", "point_up_2",
    "police_car", "poop", "post_office", "postbox", "pray", "princess",
    "punch", "purple_heart", "question", "rabbit", "racehorse", "radio",
    "rage", "rage1", "rage2", "rage3", "rage4", "rainbow", "raised_hands",
    "ramen", "red_car", "red_circle", "registered", "relaxed", "relieved",
    "restroom", "rewind", "ribbon", "rice", "rice_ball", "rice_cracker",
    "rice_scene", "ring", "rocket", "roller_coaster", "rose", "ru", "runner",
    "sa", "sagittarius", "sailboat", "sake", "sandal", "santa", "satellite",
    "satisfied", "saxophone", "school", "school_satchel", "scissors",
    "scorpius", "scream", "seat", "secret", "shaved_ice", "sheep", "shell",
    "ship", "shipit", "shirt", "shit", "shoe", "signal_strength",
    "six_pointed_star", "ski", "skull", "sleepy", "slot_machine", "smile",
    "smiley", "smirk", "smoking", "snake", "snowman", "sob", "soccer",
    "space_invader", "spades", "spaghetti", "sparkler", "sparkles",
    "speaker", "speedboat", "squirrel", "star", "star2", "stars", "station",
    "statue_of_liberty", "stew", "strawberry", "sunflower", "sunny",
    "sunrise", "sunrise_over_mountains", "surfer", "sushi", "suspect",
    "sweat", "sweat_drops", "swimmer", "syringe", "tada", "tangerine",
    "taurus", "taxi", "tea", "telephone", "tennis", "tent", "thumbsdown",
    "thumbsup", "ticket", "tiger", "tm", "toilet", "tokyo_tower", "tomato",
    "tongue", "top", "tophat", "traffic_light", "train", "trident",
    "trollface", "trophy", "tropical_fish", "truck", "trumpet", "tshirt",
    "tulip", "tv", "u5272", "u55b6", "u6307", "u6708", "u6709", "u6e80",
    "u7121", "u7533", "u7a7a", "umbrella", "unamused", "underage", "unlock",
    "up", "us", "v", "vhs", "vibration_mode", "virgo", "vs", "walking",
    "warning", "watermelon", "wave", "wc", "wedding", "whale", "wheelchair",
    "white_square", "wind_chime", "wink", "wink2", "wolf", "woman",
    "womans_hat", "womens", "x", "yellow_heart", "zap", "zzz", "+1"
]


def _emoji(text):
    emoji_url = 'http://python-china.b0.upaiyun.com/emojis/'

    pattern = re.compile(':([a-z0-9\+\-_]+):')

    def make_emoji(m):
        name = m.group(1)
        if name not in _emoji_list:
            return ':%s:' % name
        tpl = ('<img class="emoji" title="%(name)s" alt="%(name)s" height="20"'
               ' width="20" src="%(url)s%(name)s.png" align="top">')
        return tpl % {'name': name, 'url': emoji_url}

    text = pattern.sub(make_emoji, text)
    return text


class JuneRender(m.HtmlRenderer, m.SmartyPants):
    def set_pygments_options(self, noclasses=False, lang=None):
        self._pygments_noclasses = noclasses
        self._pygments_lang = lang

    def set_defaults(self, options):
        self._options = options

    def block_code(self, text, lang):
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
        elif self._pygments_lang:
            lexer = get_lexer_by_name(self._pygments_lang, stripall=True)
        else:
            return '\n<pre><code>%s</code></pre>\n' %\
                    escape.xhtml_escape(text.strip())
        formatter = HtmlFormatter(noclasses=self._pygments_noclasses)
        return highlight(text, lexer, formatter)

    def autolink(self, link, is_email):
        title = link.replace('http://', '').replace('https://', '')

        #: youtube.com
        pattern = r'http://www.youtube.com/watch\?v=([a-zA-Z0-9\-\_]+)'
        match = re.match(pattern, link)
        if not match:
            pattern = r'http://youtu.be/([a-zA-Z0-9\-\_]+)'
            match = re.match(pattern, link)
        if match:
            value = ('<iframe width="560" height="315" src='
                     '"http://www.youtube.com/embed/%(id)s" '
                     'frameborder="0" allowfullscreen></iframe>'
                     '<div><a rel="nofollow" href="%(link)s">'
                     '%(title)s</a></div>'
                    ) % {'id': match.group(1), 'link': link, 'title': title}
            return value

        #: gist support
        pattern = r'(https?://gist.github.com/[\d]+)'
        match = re.match(pattern, link)
        if match:
            value = ('<script src="%(link)s.js"></script>'
                     '<div><a rel="nofollow" href="%(link)s">'
                     '%(title)s</a></div>'
                    ) % {'link': match.group(1), 'title': title}
            return value

        #: vimeo.com
        pattern = r'http://vimeo.com/([\d]+)'
        match = re.match(pattern, link)
        if match:
            value = ('<iframe width="500" height="281" frameborder="0" '
                     'src="http://player.vimeo.com/video/%(id)s" '
                     'allowFullScreen></iframe>'
                     '<div><a rel="nofollow" href="%(link)s">'
                     '%(title)s</a></div>'
                    ) % {'id': match.group(1), 'link': link, 'title': title}
            return value
        if is_email:
            return '<a href="mailto:%(link)s">%(link)s</a>' % {'link': link}

        return '<a href="%s">%s</a>' % (link, title)


def markdown(text, noclasses=False, lang=None):
    if not isinstance(text, (unicode, type(None))):
        text = text.decode('utf-8')
    render = JuneRender(flags=m.HTML_USE_XHTML)
    render.set_pygments_options(noclasses=noclasses, lang=lang)
    md = m.Markdown(
        render,
        extensions=m.EXT_FENCED_CODE | m.EXT_AUTOLINK,
    )
    return md.render(text)


if __name__ == '__main__':
    import os
    import argparse
    parser = argparse.ArgumentParser(prog='doki')
    parser.add_argument('file', nargs='*', type=str)
    parser.add_argument('-i', '--inline', dest='inline', action='store_true',
                        help='inline style for code')
    parser.add_argument('-t', '--template', dest='template')
    parser.add_argument('-l', '--language', dest='language')

    args = parser.parse_args()
    if args.template and args.template == 'default':
        path = os.path.join(os.path.dirname(__file__), 'template.html')
        template = open(os.path.abspath(path)).read()
    elif args.template:
        template = open(args.template).read()
    else:
        template = "{{text}}"

    if args.inline:
        noclasses = True
    else:
        noclasses = False
    text = ''
    for f in args.file:
        text += markdown(open(f).read(), noclasses, args.language)

    text = template.replace('{{text}}', text)
    print(text.encode('utf-8'))
