# coding=utf-8
from .bengaliphoneticparser import *


class BengaliToBanglish(BengaliPhoneticParser):

    def __init__(self):
        char_list1 = [v for k, v in self.shoroborno.items()]
        char_list2 = [v for k, v in self.kar.items()]
        char_list3 = [v for k, v in self.byanjon_borno.items()]
        char_list4 = [v for k, v in self.jukto_borno.items()]
        char_list = char_list1+char_list2+char_list3+char_list4
        self.onechar = [char for char in char_list if len(char) == 1]
        self.twochar = [char for char in char_list if len(char) == 2]
        self.threechar = [char for char in char_list if len(char) == 3]
        self.fourchar = [char for char in char_list if len(char) == 4]
        self.fivechar = [char for char in char_list if len(char) == 5]
        self.__shoroborno = dict((v.strip(), k.strip()) for k, v in self.shoroborno.items())
        self.__kar = dict((v.strip(), k.strip()) for k, v in self.kar.items())
        self.__byanjon_borno = dict((v.strip(), k.strip()) for k, v in self.byanjon_borno.items())
        self.__jukto_borno = dict((v.strip(), k.strip()) for k, v in self.jukto_borno.items())

    def __change_sworborno(self, txt, ch):
        sx = ""
        sx += txt
        if ch == "আ":
            asx = ""
            for i, _ch in enumerate(txt):
                if i == 0:
                    if _ch == "আ":
                        asx += "a"
                    else:
                        asx += _ch
                else:
                    _prev_ch = txt[i - 1]
                    if _ch == "আ" and self._is_sworborno(_prev_ch) or self._is_kar(_prev_ch):
                        if _prev_ch == "a" or _prev_ch == "আ" or _prev_ch == "অ":
                            asx += "a"
                        else:
                            asx += "ya"
                    elif _ch == "অ" and self._is_byanjonborno(_prev_ch):
                        asx += "আ"
                    elif self._is_kar(_ch):
                        asx += self.__kar[_ch]
                    else:
                        asx += _ch

            return asx
        else:
            ofe = sx.find(ch, 0)
            ofs = 0
            while ofs < len(txt) and (ofe != -1):
                ofe = sx.find(ch, ofs)
                if ofe == -1:
                    break
                else:
                    if ofe == 0:
                        sx = sx.replace(sx[ofe:ofe + len(ch)], self.__shoroborno[ch])
                    else:
                        _prev_och = txt[ofe - 1]
                        if ch == "ও" and self._is_sworborno(_prev_och) or self._is_kar(_prev_och):
                            sx = sx.replace(sx[ofe:ofe + 1], "ও")
                        elif self._is_sworborno(_prev_och) or self._is_kar(_prev_och) or _prev_och == "ও":
                            sx = sx.replace(sx[ofe:ofe + len(ch)], self.__shoroborno[ch])
                        else:
                            if txt[ofe] != "ও":
                                sx = sx.replace(sx[ofe:ofe + len(ch)], self.__kar[ch])
                ofs = ofe + 1

        return sx

    def __change_x(self, txt):
        sx = ""
        if txt == "এক্স":
            sx += "x"
        elif txt == "ক্স":
            sx += "x"
        else:
            sx += txt

        return sx

    def __is_alphabet(self, code):
        return code.isalpha()

    def __convert(self, bengali_string):

        bengali_string = self.__change_x(bengali_string)
        for a_five_char in self.fivechar:
            bengali_string = self._change_to(bengali_string, a_five_char, self.__jukto_borno[a_five_char])

        for a_four_char in self.fourchar:
            bengali_string = self._change_to(bengali_string, a_four_char, self.__jukto_borno[a_four_char])

        for a_three_char in self.threechar:
            bengali_string = self._change_to(bengali_string, a_three_char, self.__jukto_borno[a_three_char])
        bengali_string = self.__change_sworborno(bengali_string, "rri")

        for a_two_char in self.twochar:
            if self._is_sworborno(a_two_char):
                bengali_string = self.__change_sworborno(bengali_string, a_two_char)
            elif self._is_byanjonborno(a_two_char):
                bengali_string = self._change_to(bengali_string, a_two_char, self.__byanjon_borno[a_two_char])

        for a_one_char in self.onechar:
            if self._is_sworborno(a_one_char):
                bengali_string = self.__change_sworborno(bengali_string, a_one_char)
            elif self._is_byanjonborno(a_one_char):
                bengali_string = self._change_to(bengali_string, a_one_char, self.__byanjon_borno[a_one_char])
        bengali_string = self._change_to(bengali_string, "ও", "")

        return bengali_string

    def parse(self, bengali_text_to_parse):
        separated_word = bengali_text_to_parse.split(" ")
        converted_text = ""
        for i in range(0, len(separated_word)):
            converted_text = converted_text + self.__convert(separated_word[i]) + " "

        return converted_text.strip().lower()


if __name__ == "__main__":
    b2b = BengaliToBanglish()
    while True:
        str_token = input()
        print(b2b.parse(str_token.strip()))
