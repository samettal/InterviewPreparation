def lengthOfLastWord(s: str) -> int:
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    s_list = list(s)
    harf_gordum = False
    sondan_harf = 0
    bastan_harf = 0
    harften_sonra_bosluk_gordum = False
    for i in range(len(s_list)-1, -1, -1):
        if s_list[i] in letters_list and harf_gordum == False: # son kelimenin son harfini görünce çalışır
            harf_gordum = True
            sondan_harf = i
        if s_list[i] == " " and harf_gordum == True: # sondan gelirken harflerin ardından gelen ilk boşukta çalışır
            bastan_harf = i + 1
            harften_sonra_bosluk_gordum = True
            return sondan_harf - bastan_harf + 1
        if i == 0 and harften_sonra_bosluk_gordum == False:
            return sondan_harf + 1
        
print(lengthOfLastWord("s"))