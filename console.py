
def start(user_name: str, all_posts: int, new_posts: int) -> str:
    return f"〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"+\
        f"ውድ { user_name } እንኳን በሰላም መጡ፡፡\n\nበዛሬው እለት { new_posts }"\
        + f" አዳዲስ ማስታዎቂያ(ዎች) ተለጥፈዋል፡፡ በጥቅሉ { all_posts }"\
        + f" ማስታዎቂያ(ዎች) የመረጃ ቋታችን ላይ ያገኛሉ፡፡ \n\nእባክዎ በምን መልኩ ማየት እንደሚፈልጉ ይምረጡ?\n"+\
          f"\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"


btn_options = {
    'posted_on_the_board': 'ቦርድ ላይ የተለጠፉ',
    'outside_board': 'ቦርድ ላይ ያልተለጠፉ',
    'on_board_all_ads': '⏳ ሁሉንም አሳየኝ',
    'on_board_new_ads': '☀️ የእለቱን አሳየኝ',
    'categories': '🎯 በምድብ አሳየኝ',
    'all_vacancy': '⏳ ሁሉንም የክፍት ስራ ማስታዎቂያ',
    'new_vacancy': '☀️ የእለቱን የክፍት ስራ ማስታዎቂያ',
    'all_bid': '⏳ ሁሉንም የጨረታ ማስታወቂያ',
    'new_bid': '☀️ የእለቱ የጨረታ ማስታወቂያ',
    'all_call': '⏳ ሁሉንም የጥሪ ማስታወቂያ',
    'new_call': '☀️ የእለቱን የጥሪ ማስታወቂያ',
    'other_ads': '📌 ሌሎች',

    # Categories
    'vacancy': 'የክፍት ስራ ማስታዎቂያ',
    'bid': 'የጨረታ ማስታወቂያ',
    'call': 'የጥሪ ማስታወቂያ',
    'missing': 'የአፋልጉኝ ማስታዎቂያ',
    'assistance': 'የርዳታ ማስታዎቂያ',
    'social': 'የተለያዩ ዐብይ ማኅንራዊ መልክቶች',
    'product': 'የድርጅት የምርት ማስታወቂያ',
    'exhibition': 'የእግዚብሽን ማስታወቂያ',
    'lottery': 'የሎተሪ ማስታወቂያ',
    'educational': 'የትምህርት ማስታወቂያ',
    'art': 'የኪነ-ጥበብ ማስታወቂያ',
    'other': 'ሌሎች ማስታወቂያዎች',
    'ads': '',
    # End categories

    'outside_board_all_ads': '⏳ ሁሉንም አሳየኝ',
    'outside_board_new_ads': '☀️ የእለቱን አሳየኝ',
    'top_menu': '🔗 ወደ ዋናው ማውጫ',
    'stop': '❌ አገልግሎቱን አቋርጥ',
    'restart': '🔗 ወደ ዋናው ማውጫ'
}


reply_titles = {
    'posted_on_the_board': '# ቦርድ ላይ የተለጠፉ ማስታወቂያዎች',
    'outside_board': '# ቦርድ ላይ ያልተለጠፉ ማስታወቂያዎች',
    'categories': '# ማስታወቂያዎች በምድብ',
    'other_ads': '# ሌሎች ማስታወቂያዎች',
    'vacancy': '# የክፍት ስራ ማስታዎቂያ',
    'bid': '# የጨረታ ማስታወቂያ',
    'call': '# የጥሪ ማስታወቂያ',
    'top_menu': '# የማስታዎቂያዎች ዋና ማውጫ',
    'other': '# ሌሎች ማስታወቂያዎች',

    'on_board_all_ads': '# የቦርድ ላይ የተለጠፉ ሁሉም ማስታወቂያዎች',
    'on_board_new_ads': '# ቦርድ ላይ የተለጠፉ የእለቱ ማስታወቂያዎች',
    'missing': '# የአፋልጉኝ ማስታወቂያዎች',
    'assistance': '# የርዳታ ማስታወቂያዎች',
    'social': '# የተለያዩ ዐብይ ማኅንራዊ መልክቶች',
    'product': '# የድርጅት የምርት ማስታወቂያዎች',
    'exhibition': '# የእግዚብሽን ማስታወቂያዎች',
    'lottery': '# የሎተሪ ማስታወቂያዎች',
    'educational': '# የትምህርት ማስታወቂያዎች',
    'art': '# የኪነ-ጥበብ ማስታወቂያዎች',
    'all_vacancy': '# ሁሉም የክፍት ስራ ማስታወቂያዎች',
    'new_vacancy': '# የእለቱ የክፍት ስራ ማስታወቂያዎች',
    'all_bid': '# ሁሉም የጨረታ ማስታወቂያዎች',
    'new_bid': '# የእለቱ የጨረታ ማስታወቂያዎች',
    'all_call': '# ሁሉም የጥሪ ማስታወቂያዎች',
    'new_call': '# የእለቱ የጥሪ ማስታወቂያዎች',
    'outside_board_all_ads': '# ሁሉም ቦርድ ላይ ያልተለጠፉ ማስታዎቂያዎች',
    'outside_board_new_ads': '# የእለቱ ቦርድ ላይ ያልተለጠፉ ማስታዎቂያዎች',
    'stop': 'በአገልግሎቱ እንደተደሰቱ ተስፋ እናደርጋልን፡፡\n\nእባክዎ ሃሳብ ወይም አስተያየት ካልዎት በ @hulumboard ያግኙን፡፡ \n\nመልካም ቀን፡፡',

    }