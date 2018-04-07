# coding=utf-8
import re

from .bengaliphoneticparser import BengaliPhoneticParser


class BanglishToBengali(BengaliPhoneticParser):

    def __change(self, txt, ch, nch):
        return txt.replace(ch, nch)

    def _get_char_type(self, ch):
        if ch in self.kar or ch in self.kar.values():
            return 'k'
        elif ch in self.shoroborno or ch in self.shoroborno.values():
            return 'sb'
        elif ch in self.byanjon_borno or ch in self.byanjon_borno.values():
            return 'bb'

    def __change_sworborno(self, txt, ch):
        sx = ""
        sx += txt
        if ch.lower() == "a":
            asx = ""
            for i in range(0, len(txt)):
                if i == 0:
                    if txt[i].lower() == "a":
                        asx += "আ"
                    else:
                        asx += txt[i]
                else:
                    if txt[i].lower() == "a":
                        prev_char_type = self._get_char_type(txt[i - 1])
                        is_prev_one_kar_or_sworborno = prev_char_type == 'k' or prev_char_type == 'sb'
                        is_prev_one_byanjon_borno = prev_char_type == 'bb'
                        if is_prev_one_kar_or_sworborno:
                            if txt[i - 1] == "আ" or txt[i - 1] == "া" or txt[i - 1] == "a" or txt[i - 1] == "A":
                                asx += "আ"
                            else:
                                asx += "য়া"
                        elif is_prev_one_byanjon_borno:
                            asx += "া"
                    else:
                        asx += txt[i]
            return asx
        else:
            ofe = sx.find(ch, 0)
            ofs = 0
            while ofs < len(txt) and ofe != -1:
                ofe = sx.find(ch, ofs)
                if ofe == -1:
                    break
                else:
                    if ofe == 0:
                        sx = sx.replace(sx[ofe:ofe + len(ch)], self.shoroborno[ch])
                    else:
                        prev_char_type = self._get_char_type(txt[ofe - 1])
                        is_prev_one_kar_or_sworborno = prev_char_type == 'k' or prev_char_type == 'sb'
                        if ch == "o" and is_prev_one_kar_or_sworborno:
                            sx = sx.replace(sx[ofe:ofe + 1], "ও")
                        elif txt[ofe - 1] == 'o' or is_prev_one_kar_or_sworborno:
                            sx = sx.replace(sx[ofe:ofe + len(ch)], self.shoroborno[ch])
                        else:
                            if txt[ofe] != 'o':
                                sx = sx.replace(sx[ofe:ofe + len(ch)], self.kar[ch])
                ofs = ofe + 1
        return sx

    def __change_x(self, txt):
        sx = ""
        for i in range(0, len(txt)):
            if i == 0:
                if "" + txt[i].lower() == "x":
                    sx += "এক্স"
                else:
                    sx += txt[i]
            else:
                if "" + txt[i].lower() == "x":
                    if self.__is_alphabet(txt[i - 1]):
                        sx += "ক্স"
                    else:
                        sx += "এক্স"
                else:
                    sx += txt[i]
        return sx

    def __is_alphabet(self, code):
        return code.isalpha()

    def __convert(self, text_to_convert):
        banglish_string = re.sub(r'[ABCEFGHJKLMPQVYX]', lambda x: x.group(0).lower(), text_to_convert)
        banglish_string = self.__change_x(banglish_string)

        for a_five_char in self.five_char:
            banglish_string = self.__change(banglish_string, a_five_char, self.jukto_borno[a_five_char])

        for a_four_char in self.four_char:
            banglish_string = self.__change(banglish_string, a_four_char, self.jukto_borno[a_four_char])

        for a_three_char in self.three_char:
            banglish_string = self.__change(banglish_string, a_three_char, self.jukto_borno[a_three_char])
        banglish_string = self.__change_sworborno(banglish_string, "rri")

        for a_two_char in self.two_char:
            if (a_two_char in self.shoroborno.keys()):
                banglish_string = self.__change_sworborno(banglish_string, a_two_char)
            elif (a_two_char in self.byanjon_borno.keys()):
                banglish_string = self.__change(banglish_string, a_two_char, self.byanjon_borno[a_two_char])
            elif (a_two_char in self.byanjon_borno.keys()):
                banglish_string = self.__change(banglish_string, a_two_char, self.byanjon_borno[a_two_char])

        for a_one_char in self.one_char:
            if (a_one_char in self.shoroborno.keys()):
                banglish_string = self.__change_sworborno(banglish_string, a_one_char)
            elif (a_one_char in self.byanjon_borno.keys()):
                banglish_string = self.__change(banglish_string, a_one_char, self.byanjon_borno[a_one_char])
        banglish_string = self.__change(banglish_string, "o", "")

        return banglish_string

    def parse(self, banglish_text_to_parse):
        converted_text = ""

        for word in banglish_text_to_parse.split(" "):
            converted_text += '{} '.format(self.__convert(word))

        return converted_text.strip()


if __name__ == "__main__":
    b2b = BanglishToBengali()
    while True:
        str_token = input()
        print(b2b.parse(str_token))
