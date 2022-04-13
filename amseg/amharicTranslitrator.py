#romanization
class AmharicTranslitrator:
    def transliterate (norm):
        norm = norm.replace("chwa", "ቿ")
        norm = norm.replace("chua", "ቿ")
        norm = norm.replace("chie", "ቼ")
        norm = norm.replace("che", "ቸ")
        norm = norm.replace("chu", "ቹ")
        norm = norm.replace("chi", "ቺ")
        norm = norm.replace("cha", "ቻ")
        norm = norm.replace("cho", "ቾ")
        norm = norm.replace("hwa", "ኋ")
        norm = norm.replace("hua", "ኋ")
        norm = norm.replace("hie", "ሄ")
        norm = norm.replace("shwa", "ሿ")
        norm = norm.replace("shua", "ሿ")
        norm = norm.replace("she", "ሸ")
        norm = norm.replace("shu", "ሹ")
        norm = norm.replace("shi", "ሺ")
        norm = norm.replace("sha", "ሻ")
        norm = norm.replace("sho", "ሾ")
        norm = norm.replace("sh", "ሺ")
        norm = norm.replace("ha", "ሀ")
        norm = norm.replace("hu", "ሁ")
        norm = norm.replace("hi", "ሂ")
        norm = norm.replace("he", "ሄ")
        norm = norm.replace("ho", "ሆ")
        norm = norm.replace("lwa", "ሏ")
        norm = norm.replace("lua", "ሏ")
        norm = norm.replace("le", "ለ")
        norm = norm.replace("lu", "ሉ")
        norm = norm.replace("li", "ሊ")
        norm = norm.replace("la", "ላ")
        norm = norm.replace("le", "ሌ")
        norm = norm.replace("lo", "ሎ")
        norm = norm.replace("ll", "ል")
        norm = norm.replace("l", "ል")
        norm = norm.replace("mwa", "ሟ")
        norm = norm.replace("mua", "ሟ")
        norm = norm.replace("mie", "ሜ")
        norm = norm.replace("me", "መ")
        norm = norm.replace("mu", "ሙ")
        norm = norm.replace("mi", "ሚ")
        norm = norm.replace("ma", "ማ")
        norm = norm.replace("mo", "ሞ")
        norm = norm.replace("m", "ም")
        norm = norm.replace("rwa", "ሯ")
        norm = norm.replace("rua", "ሯ")
        norm = norm.replace("rie", "ሬ")
        norm = norm.replace("re", "ረ")
        norm = norm.replace("ru", "ሩ")
        norm = norm.replace("ri", "ሪ")
        norm = norm.replace("ra", "ራ")
        norm = norm.replace("ro", "ሮ")
        norm = norm.replace("rr", "ር")
        norm = norm.replace("r", "ር")
        norm = norm.replace("swa", "ሷ")
        norm = norm.replace("sua", "ሷ")
        norm = norm.replace("sie", "ሴ")
        norm = norm.replace("se", "ሰ")
        norm = norm.replace("su", "ሱ")
        norm = norm.replace("si", "ሲ")
        norm = norm.replace("sa", "ሳ")
        norm = norm.replace("so", "ሶ")
        norm = norm.replace("qwa", "ቋ")
        norm = norm.replace("qua", "ቋ")
        norm = norm.replace("qie", "ቄ")
        norm = norm.replace("qe", "ቀ")
        norm = norm.replace("qu", "ቁ")
        norm = norm.replace("qi", "ቂ")
        norm = norm.replace("qa", "ቃ")
        norm = norm.replace("qo", "ቆ")
        norm = norm.replace("q", "ቅ")
        norm = norm.replace("bwa", "ቧ")
        norm = norm.replace("bua", "ቧ")
        norm = norm.replace("bie", "ቤ")
        norm = norm.replace("be", "በ")
        norm = norm.replace("bu", "ቡ")
        norm = norm.replace("bi", "ቢ")
        norm = norm.replace("ba", "ባ")
        norm = norm.replace("bo", "ቦ")
        norm = norm.replace("b", "ብ")
        norm = norm.replace("vwa", "ቯ")
        norm = norm.replace("vua", "ቯ")
        norm = norm.replace("vie", "ቬ")
        norm = norm.replace("ve", "ቨ")
        norm = norm.replace("vu", "ቩ")
        norm = norm.replace("vi", "ቪ")
        norm = norm.replace("va", "ቫ")
        norm = norm.replace("vo", "ቮ")
        norm = norm.replace("v", "ቭ")
        norm = norm.replace("twa", "ቷ")
        norm = norm.replace("tua", "ቷ")
        norm = norm.replace("tie", "ቴ")
        norm = norm.replace("te", "ተ")
        norm = norm.replace("tu", "ቱ")
        norm = norm.replace("ti", "ቲ")
        norm = norm.replace("ta", "ታ")
        norm = norm.replace("to", "ቶ")
        norm = norm.replace("gnwa", "ኟ")
        norm = norm.replace("gnua", "ኟ")
        norm = norm.replace("gne", "ኘ")
        norm = norm.replace("gnu", "ኙ")
        norm = norm.replace("gni", "ኚ")
        norm = norm.replace("gna", "ኛ")
        norm = norm.replace("gno", "ኞ")
        norm = norm.replace("gn", "ኝ")
        norm = norm.replace("nwa", "ኗ")
        norm = norm.replace("nua", "ኗ")
        norm = norm.replace("nie", "ኔ")
        norm = norm.replace("ne", "ነ")
        norm = norm.replace("nu", "ኑ")
        norm = norm.replace("ni", "ኒ")
        norm = norm.replace("na", "ና")
        norm = norm.replace("no", "ኖ")
        norm = norm.replace("n", "ን")
        norm = norm.replace("kwa", "ኳ")
        norm = norm.replace("kua", "ኳ")
        norm = norm.replace("kie", "ኬ")
        norm = norm.replace("ke", "ከ")
        norm = norm.replace("ku", "ኩ")
        norm = norm.replace("ki", "ኪ")
        norm = norm.replace("ka", "ካ")
        norm = norm.replace("ko", "ኮ")
        norm = norm.replace("k", "ክ")
        norm = norm.replace("wie", "ዌ")
        norm = norm.replace("we", "ወ")
        norm = norm.replace("wu", "ው")
        norm = norm.replace("wi", "ዊ")
        norm = norm.replace("wa", "ዋ")
        norm = norm.replace("wo", "ወ")
        norm = norm.replace("w", "ው")
        norm = norm.replace("zwa", "ዟ")
        norm = norm.replace("zua", "ዟ")
        norm = norm.replace("zie", "ዜ")
        norm = norm.replace("ze", "ዘ")
        norm = norm.replace("zu", "ዙ")
        norm = norm.replace("zi", "ዚ")
        norm = norm.replace("za", "ዛ")
        norm = norm.replace("zo", "ዞ")
        norm = norm.replace("zhwa", "ዧ")
        norm = norm.replace("zhua", "ዧ")
        norm = norm.replace("zhie", "ዤ")
        norm = norm.replace("zhe", "ዠ")
        norm = norm.replace("zhu", "ዡ")
        norm = norm.replace("zhi", "ዢ")
        norm = norm.replace("zha", "ዣ")
        norm = norm.replace("zho", "ዦ")
        norm = norm.replace("zh", "ዥ")
        norm = norm.replace("z", "ዝ")
        norm = norm.replace("ye", "የ")
        norm = norm.replace("yu", "ዩ")
        norm = norm.replace("yi", "ዪ")
        norm = norm.replace("ya", "ያ")
        norm = norm.replace("yo", "ዮ")
        norm = norm.replace("y", "ይ")
        norm = norm.replace("dwa", "ዷ")
        norm = norm.replace("dua", "ዷ")
        norm = norm.replace("die", "ዴ")
        norm = norm.replace("de", "ደ")
        norm = norm.replace("du", "ዱ")
        norm = norm.replace("di", "ዲ")
        norm = norm.replace("da", "ዳ")
        norm = norm.replace("do", "ዶ")
        norm = norm.replace("d", "ድ")
        norm = norm.replace("jwa", "ጇ")
        norm = norm.replace("jua", "ጇ")
        norm = norm.replace("je", "ጀ")
        norm = norm.replace("ju", "ጁ")
        norm = norm.replace("ji", "ጂ")
        norm = norm.replace("ja", "ጃ")
        norm = norm.replace("jo", "ጆ")
        norm = norm.replace("j", "ጅ")
        norm = norm.replace("gwa", "ጓ")
        norm = norm.replace("gua", "ጓ")
        norm = norm.replace("gie", "ጌ")        
        norm = norm.replace("ge", "ገ")
        norm = norm.replace("gu", "ጉ")
        norm = norm.replace("gi", "ጊ")
        norm = norm.replace("ga", "ጋ")
        norm = norm.replace("go", "ጎ")
        norm = norm.replace("g", "ግ")
        norm = norm.replace("chwa", "ጯ")
        norm = norm.replace("chua", "ጯ")
        norm = norm.replace("che", "ጨ")
        norm = norm.replace("chu", "ጩ")
        norm = norm.replace("chi", "ጪ")
        norm = norm.replace("cha", "ጫ")
        norm = norm.replace("cho", "ጮ")
        norm = norm.replace("ch", "ች")
        norm = norm.replace("h", "ህ")
        norm = norm.replace("tswa", "ጿ")
        norm = norm.replace("tsua", "ጿ")
        norm = norm.replace("tsie", "ፄ")
        norm = norm.replace("tse", "ፀ")
        norm = norm.replace("tsu", "ፁ")
        norm = norm.replace("tsi", "ፂ")
        norm = norm.replace("tsa", "ፃ")
        norm = norm.replace("tso", "ፆ")
        norm = norm.replace("ts", "ፅ")
        norm = norm.replace("t", "ት")
        norm = norm.replace("ss", "ስ")
        norm = norm.replace("fwa", "ፏ")
        norm = norm.replace("fua", "ፏ")
        norm = norm.replace("fie", "ፌ")
        norm = norm.replace("fe", "ፈ")
        norm = norm.replace("fu", "ፉ")
        norm = norm.replace("fi", "ፊ")
        norm = norm.replace("fa", "ፋ")
        norm = norm.replace("fo", "ፎ")
        norm = norm.replace("f", "ፍ")
        norm = norm.replace("pwa", "ፗ")
        norm = norm.replace("pua", "ፗ")
        norm = norm.replace("pie", "ፔ")
        norm = norm.replace("pe", "ፐ")
        norm = norm.replace("pu", "ፑ")
        norm = norm.replace("pi", "ፒ")
        norm = norm.replace("pa", "ፓ")
        norm = norm.replace("po", "ፖ")
        norm = norm.replace("p", "ፕ")
        norm = norm.replace("ca", "ካ")
        norm = norm.replace("ci", "ሲ")
        norm = norm.replace("ce", "ሰ")
        norm = norm.replace("cu", "ኩ")
        norm = norm.replace("c ", "ክ")
        norm = norm.replace(" gn ", "ግን")
        norm = norm.replace("c", "ቸ")
        norm = norm.replace("xe", "ዘ")
        norm = norm.replace("xu", "ዙ")
        norm = norm.replace("xi", "ዚ")
        norm = norm.replace("xa", "ዛ")
        norm = norm.replace("xo", "ዞ")
        norm = norm.replace("x", "ክስ")
        norm = norm.replace("xs", "ክስ")
        norm = norm.replace("s", "ስ")
        norm = norm.replace("a", "አ")
        norm = norm.replace("u", "ኡ")
        norm = norm.replace("i", "ኢ")
        norm = norm.replace("e", "እ")
        norm = norm.replace("o", "ኦ")
        norm = norm.replace(". ", "፡፡")
        norm = norm.replace(";", "፤")
        norm = norm.replace(": ", "፥")
        norm = norm.replace(",", "፣")
        return norm