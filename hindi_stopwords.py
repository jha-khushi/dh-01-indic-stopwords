"""
============================================================
Topic: Indic Language Stop Words for Natural Language Processing
============================================================
Author Name(s): Khushi Jha
Short Description: This file contains a stop-word list for Hindi,
an Indo-Aryan language written in the Devanagari script. These words
may be used during text preprocessing in Natural Language Processing
(NLP), for example to remove high-frequency function words (pronouns,
postpositions, conjunctions, auxiliary verbs and particles) before
keyword extraction, topic modelling or frequency analysis.
Semester: Monsoon Semester 2026
Affiliation: Department of Humanities and Social Sciences,
Indian Institute of Technology (Indian School of Mines) Dhanbad

Note:
These lists contain illustrative examples only. Please modify them
accordingly.

Hindi spelling varies in practice (e.g. "गए" / "गये", "नहीं" / "नही",
"लिए" / "लिये"), so common variants are included. Negation words such
as "नहीं" and "न" change meaning; remove them from this list for tasks
like sentiment analysis.
============================================================
"""


# 1. Hindi Stop Words
# Language: Hindi
# Script: Devanagari

hindi_stopwords = [
    # Conjunctions and connectives
    "और", "एवं", "तथा", "व", "या", "अथवा", "लेकिन", "परंतु", "पर",
    "किंतु", "मगर", "बल्कि", "अगर", "यदि", "तो", "कि", "क्योंकि",
    "इसलिए", "इसलिये", "जबकि", "ताकि", "फिर", "भी", "यानी",

    # Personal pronouns
    "मैं", "हम", "तू", "तुम", "आप", "वह", "वे", "वो", "यह", "ये",
    "स्वयं", "खुद",

    # Oblique and object forms of pronouns
    "मुझे", "मुझसे", "हमें", "हमसे", "तुझे", "तुम्हें", "आपको",
    "आपसे", "उसे", "उसको", "उससे", "उन्हें", "उनको", "उनसे",
    "इसे", "इसको", "इससे", "इन्हें", "इनको", "इनसे", "उस", "उन",
    "इस", "इन", "उसने", "उन्होंने", "इसने", "इन्होंने",

    # Possessives
    "मेरा", "मेरी", "मेरे", "हमारा", "हमारी", "हमारे", "तेरा",
    "तेरी", "तेरे", "तुम्हारा", "तुम्हारी", "तुम्हारे", "आपका",
    "आपकी", "आपके", "उसका", "उसकी", "उसके", "उनका", "उनकी",
    "उनके", "इसका", "इसकी", "इसके", "इनका", "इनकी", "इनके",
    "अपना", "अपनी", "अपने",

    # Postpositions (case markers)
    "का", "की", "के", "को", "में", "से", "ने", "पे", "तक",
    "लिए", "लिये", "द्वारा", "साथ", "बाद", "पहले", "ऊपर", "नीचे",
    "अंदर", "बाहर", "पास", "बारे", "तरह", "जैसे", "जैसा", "जैसी",
    "बिना", "करके",

    # Relative and interrogative words
    "जो", "जिस", "जिसे", "जिसका", "जिसकी", "जिसके", "जिन", "जिन्हें",
    "जिन्होंने", "जब", "जहाँ", "क्या", "कौन", "किस", "किसे",
    "किसका", "किसकी", "किसके", "कहाँ", "कब", "कैसे", "कैसा",
    "कैसी", "क्यों", "कितना", "कितनी", "कितने",

    # Quantifiers and determiners
    "सब", "सभी", "सारा", "सारी", "सारे", "कुछ", "कोई", "किसी",
    "हर", "प्रत्येक", "एक", "दोनों", "केवल", "सिर्फ", "बहुत",
    "अधिक", "ज़्यादा", "ज्यादा", "कम", "अन्य", "दूसरा", "दूसरे",

    # Adverbs of place and time
    "यहाँ", "यहां", "वहाँ", "वहां", "अब", "तब", "आज", "अभी",
    "कभी", "हमेशा",

    # Auxiliary and copula verb forms
    "है", "हैं", "हूँ", "हूं", "हो", "था", "थी", "थे", "थीं",
    "होता", "होती", "होते", "होना", "होने", "हुआ", "हुई", "हुए",
    "रहा", "रही", "रहे", "गया", "गई", "गए", "गये", "सकता",
    "सकती", "सकते", "चाहिए", "चाहिये", "वाला", "वाली", "वाले",

    # Light verbs (high-frequency, low content)
    "करना", "करने", "करता", "करती", "करते", "किया", "किए", "किये",
    "की", "कर", "दिया", "दी", "दिए", "लिया", "ली",

    # Negation and particles
    "नहीं", "नही", "न", "ना", "मत", "ही", "जी", "हाँ",
    "हां",
]

# Remove repeated entries (a few words belong to two categories, e.g.
# "की" is both a postposition and a verb form) while keeping the order.
hindi_stopwords = list(dict.fromkeys(hindi_stopwords))


def remove_stopwords(text):
    """Return the words of `text` that are not Hindi stop words."""
    return [word for word in text.split() if word not in hindi_stopwords]


if __name__ == "__main__":
    sample = "मैं आज अपने दोस्त के साथ बाज़ार गई और वहाँ से किताबें खरीदीं"
    print("Number of stop words:", len(hindi_stopwords))
    print("Original sentence    :", sample)
    print("After removing stop words:", " ".join(remove_stopwords(sample)))
