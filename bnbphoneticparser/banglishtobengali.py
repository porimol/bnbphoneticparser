# coding=utf-8
from .bengaliphoneticparser import *


class BanglishToBengali(BengaliPhoneticParser):

    def __change(self, txt, ch, nch):
        return txt.replace(ch, nch)


    def __change_sworborno(self, txt, ch):
        sx = ""
        sx += txt
        if (ch.lower() == "a"):
            asx = ""
            for i in range(0, len(txt)):
                if (i == 0):
                    if ("" + txt[i].lower() == "a"):
                        asx += "আ"
                    else:
                        asx += txt[i]
                else:
                    if (("" + txt[i].lower() == "a") and (("" + txt[i - 1] in self.shoroborno.values()) or
                                                              ("" + txt[i - 1] in self.shoroborno.keys()) or
                                                              ("" + txt[i - 1] in self.kar.keys()) or
                                                              ("" + txt[i - 1] in self.kar.values()))):
                        if (("" + txt[i - 1] == "আ") or ("" + txt[i - 1] == "া") or ("" + txt[i - 1] == "a") or (
                                        "" + txt[i - 1] == "A")):
                            asx += "আ"
                        else:
                            asx += "য়া"
                    elif (("" + txt[i].lower() == "a") and (("" + txt[i - 1] in self.byanjon_borno.values()) or
                                                                ("" + txt[i - 1] in self.byanjon_borno.keys()) or (
                                    "" + txt[i - 1] in self.byanjon_borno.keys())
                                                            or ("" + txt[i - 1] in self.byanjon_borno.values()))):
                        asx += "া"
                    else:
                        asx += "" + txt[i]
            return asx
        else:
            ofe = sx.find(ch, 0)
            ofs = 0
            while ofs < len(txt) and (ofe != -1):
                ofe = sx.find(ch, ofs)
                # print(ofe)
                if (ofe == -1):
                    break
                else:
                    if (ofe == 0):
                        # print(sx)
                        sx = sx.replace(sx[ofe:ofe + len(ch)], self.shoroborno[ch])
                    else:
                        if (ch == "o" and (("" + txt[ofe - 1] in self.shoroborno.values()) or (
                                        "" + txt[ofe - 1] in self.shoroborno.keys())
                                           or ("" + txt[ofe - 1] in self.kar.keys()) or (
                                        "" + txt[ofe - 1] in self.kar.values()))):
                            sx = sx.replace(sx[ofe:ofe + 1], "ও")
                        elif (("" + txt[ofe - 1] in self.shoroborno.values()) or (
                                        "" + txt[ofe - 1] in self.shoroborno.keys())
                              or ("" + txt[ofe - 1] in self.kar.keys()) or (
                                        "" + txt[ofe - 1] in self.kar.values()) or
                                  ("" + txt[ofe - 1] == "o")):
                            sx = sx.replace(sx[ofe:ofe + len(ch)], self.shoroborno[ch])
                        else:
                            if ("" + txt[ofe] != "o"):
                                sx = sx.replace(sx[ofe:ofe + len(ch)], self.kar[ch])
                ofs = ofe + 1
        return sx


    def __change_x(self, txt, ch):
        sx = ""
        for i in range(0, len(txt)):
            if (i == 0):
                if ("" + txt[i].lower() == "x"):
                    sx += "এক্স"
                else:
                    sx += txt[i]
            else:
                if ("" + txt[i].lower() == "x"):
                    if (self.__is_alphabet(txt[i - 1])):
                        sx += "ক্স"
                    else:
                        sx += "এক্স"
                else:
                    sx += txt[i]
        return sx


    def __is_alphabet(self, code):
        return code.isalpha()


    def __convert(self, text_to_convert):
        banglish_string = text_to_convert. \
            replace("A", "a"). \
            replace("B", "b"). \
            replace("C", "c"). \
            replace("E", "e"). \
            replace("F", "f"). \
            replace("G", "g"). \
            replace("H", "h"). \
            replace("J", "j"). \
            replace("K", "k"). \
            replace("L", "l"). \
            replace("M", "m"). \
            replace("P", "p"). \
            replace("Q", "q"). \
            replace("V", "v"). \
            replace("Y", "y"). \
            replace("X", "x")

        banglish_string = self.__change_x(banglish_string, "x")
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
        separated_word = banglish_text_to_parse.split(" ")
        converted_text = ""
        for i in range(0, len(separated_word)):
            converted_text = converted_text + self.__convert(separated_word[i]) + " "

        return converted_text.strip()


if __name__ == "__main__":
    b2b = BanglishToBengali()
    while True:
        str_token = input()
        print(b2b.parse(str_token))
