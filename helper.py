def Hira(m):
    if(m=='a'):
        m ='あ'
    elif(m=='i'):
        m ='い'
    elif(m=='u'):
        m ='う'
    elif(m=='e'):
        m ='え'
    elif(m=='o'):
        m ='お'

    #This is ka ki ku ke ko
    elif(m=='ka'):
        m ='か'
    elif(m=='ki'):
        m ='き'
    elif(m=='ku'):
        m ='く'
    elif(m=='ke'):
        m ='け'
    elif(m=='ko'):
        m ='こ'
    #This is G
    elif(m=='ga'):
        m ='が'
    elif(m=='gi'):
        m ='ぎ'
    elif(m=='gu'):
        m ='ぐ'
    elif(m=='ge'):
        m ='げ'
    elif(m=='go'):
        m ='ご'
    #This is S
    elif(m=='sa'):
        m ='さ'
    elif(m=='shi'):
        m ='し'
    elif(m=='su'):
        m ='す'
    elif(m=='se'):
        m ='せ'
    elif(m=='so'):
        m ='そ'
    #This is T
    elif(m=='ta'):
        m ='た'
    elif(m=='chi'):
        m ='ち'
    elif(m=='tsu'):
        m ='つ'
    elif(m=='te'):
        m ='て'
    elif(m=='to'):
        m ='と'
    #This is D
    elif(m=='da'):
        m ='だ'
    elif(m=='de'):
        m ='で'
    elif(m=='do'):
        m ='ど'
    #This is N
    elif(m=='na'):
        m ='な'
    elif(m=='ni'):
        m ='に'
    elif(m=='nu'):
        m ='ぬ'
    elif(m=='ne'):
        m ='ね'
    elif(m=='no'):
        m ='の'
    #This is H
    elif(m=='ha'):
        m ='は'
    elif(m=='hi'):
        m ='ひ'
    elif(m=='fu'):
        m ='ふ'
    elif(m=='he'):
        m ='へ'
    elif(m=='ho'):
        m ='ほ'
    #This is B
    elif(m=='ba'):
        m ='ば'
    elif(m=='bi'):
        m ='び'
    elif(m=='bu'):
        m ='ぶ'
    elif(m=='be'):
        m ='べ'
    elif(m=='bo'):
        m ='ぼ'
    #This is P
    elif(m=='pa'):
        m ='ぱ'
    elif(m=='pi'):
        m ='ぴ'
    elif(m=='pu'):
        m ='ぷ'
    elif(m=='pe'):
        m ='ぺ'
    elif(m=='po'):
        m ='ぽ'
    #This is Z
    elif(m=='za'):
        m ='ざ'
    elif(m=='ji'):
        m ='じ'
    elif(m=='zu'):
        m ='ず'
    elif(m=='ze'):
        m ='ぜ'
    elif(m=='zo'):
        m ='ぞ'
    #This is M
    elif(m=='ma'):
        m ='ま'
    elif(m=='mi'):
        m ='み'
    elif(m=='mu'):
        m ='む'
    elif(m=='me'):
        m ='め'
    elif(m=='mo'):
        m ='も'
    #This is R
    elif(m=='ra'):
        m ='ら'
    elif(m=='ri'):
        m ='り'
    elif(m=='ru'):
        m ='る'
    elif(m=='re'):
        m ='れ'
    elif(m=='ro'):
        m ='ろ'
    #The Y
    elif(m=='ya'):
        m ='や'
    elif(m=='yu'):
        m ='ゆ'
    elif(m=='yo'):
        m ='よ'
    #The w
    elif(m=='wa'):
        m ='わ'
    elif(m=='wo'):
        m ='を'
    elif(m=='n'):
        m ='ん'
    return (m)

def Letter(m):
    accepted_words = ['a','i','e','o','u',\
    'ka','ki','ku','ke','ko',\
    'ga','gi','gu','ge','go',\
    'sa','shi','su','se','so',\
    'za','ji','zu','ze','zo',\
    'ta','chi','tsu','te','to',\
    'da','de','do',\
    'na','ni','nu','ne','no',\
    'ha','hi','fu','he','ho',\
    'ba','bi','bu','be','bo',\
    'pa','pi','pu','pe','po',\
    'ma','mi','mu','me','mo',\
    'ra','ri','ru','re','ro',\
    'ya','yu','yo',\
    'wa','wo','n']
    for a in accepted_words:
        if(m==a):
            return (a)

def Katakana(m):
    if(m=='a'):
        m='ア'
    elif(m=='i'):
        m='イ'
    elif(m=='u'):
        m='ウ'
    elif(m=='e'):
        m='エ'
    elif(m=='o'):
        m='オ'

    #This is ka ki ku ke ko
    elif(m=='ka'):
        m='カ'
    elif(m=='ki'):
        m='キ'
    elif(m=='ku'):
        m='ク'
    elif(m=='ke'):
        m='ケ'
    elif(m=='ko'):
        m='コ'
    #This is G
    elif(m=='ga'):
        m='ガ'
    elif(m=='gi'):
        m='ギ'
    elif(m=='gu'):
        m='グ'
    elif(m=='ge'):
        m='ゲ'
    elif(m=='go'):
        m='ゴ'
    #This is S
    elif(m=='sa'):
        m='サ'
    elif(m=='shi'):
        m='シ'
    elif(m=='su'):
        m='ス'
    elif(m=='se'):
        m='セ'
    elif(m=='so'):
        m='ソ'
    #This is T
    elif(m=='ta'):
        m='タ'
    elif(m=='chi'):
        m='チ'
    elif(m=='tsu'):
        m='ツ'
    elif(m=='te'):
        m='テ'
    elif(m=='to'):
        m='ト'
    #This is D
    elif(m=='da'):
        m='ダ'
    elif(m=='de'):
        m='デ'
    elif(m=='do'):
        m='ド'
    #This is N
    elif(m=='na'):
        m='ナ'
    elif(m=='ni'):
        m='ニ'
    elif(m=='nu'):
        m='ヌ'
    elif(m=='ne'):
        m='ネ'
    elif(m=='no'):
        m='ノ'
    #This is H
    elif(m=='ha'):
        m='ハ'
    elif(m=='hi'):
        m='ヒ'
    elif(m=='fu'):
        m='フ'
    elif(m=='he'):
        m='ヘ'
    elif(m=='ho'):
        m='ホ'
    #This is B
    elif(m=='ba'):
        m='バ'
    elif(m=='bi'):
        m='ビ'
    elif(m=='bu'):
        m='ブ'
    elif(m=='be'):
        m='ベ'
    elif(m=='bo'):
        m='ボ'
    #This is P
    elif(m=='pa'):
        m='パ'
    elif(m=='pi'):
        m='ピ'
    elif(m=='pu'):
        m='プ'
    elif(m=='pe'):
        m='ペ'
    elif(m=='po'):
        m='ポ'
    #This is Z
    elif(m=='za'):
        m='ザ'
    elif(m=='ji'):
        m='ジ'
    elif(m=='zu'):
        m='ズ'
    elif(m=='ze'):
        m='ゼ'
    elif(m=='zo'):
        m='ゾ'
    #This is M
    elif(m=='ma'):
        m='マ'
    elif(m=='mi'):
        m='ミ'
    elif(m=='mu'):
        m='ム'
    elif(m=='me'):
        m='メ'
    elif(m=='mo'):
        m='モ'
    #This is R
    elif(m=='ra'):
        m='ラ'
    elif(m=='ri'):
        m='リ'
    elif(m=='ru'):
        m='ル'
    elif(m=='re'):
        m='レ'
    elif(m=='ro'):
        m='ロ'
    #The Y
    elif(m=='ya'):
        m='ヤ'
    elif(m=='yu'):
        m='ユ'
    elif(m=='yo'):
        m='ヨ'
    #The w
    elif(m=='wa'):
        m='ワ'
    elif(m=='wo'):
        m='ヲ'
    elif(m=='n'):
        m='ン'
    return(m)
