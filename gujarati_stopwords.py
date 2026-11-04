"""
============================================================
Topic: Indic Language Stop Words for Natural Language Processing
============================================================
Author Name(s): Khushi Jha
Short Description: This file contains a stop-word list for Gujarati,
an Indo-Aryan language written in the Gujarati script. These words
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

In written Gujarati the case markers are usually joined to the word
("ઘરમાં" = in the house, "રામનું" = Ram's), so whitespace tokenisation
will not separate them. The postpositions below catch the cases where
they are written separately; for full coverage, split these suffixes
off before removing stop words. Negation words such as "નથી" and
"નહીં" change meaning; remove them from this list for tasks like
sentiment analysis.
============================================================
"""

import unicodedata


# 1. Gujarati Stop Words
# Language: Gujarati
# Script: Gujarati

gujarati_stopwords = [
    # Conjunctions and connectives
    "અને", "તથા", "તેમજ", "પણ", "પરંતુ", "કિંતુ", "અથવા", "કે", "જો",
    "તો", "કારણ", "કેમકે", "જેથી", "તેથી", "એટલે", "છતાં", "જ્યારે",
    "ત્યારે", "બલ્કે",

    # Personal pronouns
    "હું", "અમે", "આપણે", "તું", "તમે", "આપ", "તે", "તેઓ", "આ",
    "એ", "પોતે", "મેં",

    # Object and possessive forms of pronouns
    "મને", "મારું", "મારી", "મારા", "મારો", "અમને", "અમારું", "અમારી",
    "અમારા", "આપણું", "આપણી", "આપણા", "તને", "તારું", "તારી", "તારા",
    "તમને", "તમારું", "તમારી", "તમારા", "તેને", "તેનું", "તેની",
    "તેના", "તેમને", "તેમનું", "તેમની", "તેમના", "તેણે", "તેમણે",
    "એને", "એનું", "એની", "એના", "આને", "આનું", "આની", "આના",
    "પોતાનું", "પોતાની", "પોતાના",

    # Postpositions (case markers)
    "નું", "ની", "ના", "નો", "ને", "માં", "થી", "પર", "પાસે", "સાથે",
    "માટે", "વડે", "દ્વારા", "સુધી", "વિશે", "વિના", "બાદ", "પછી",
    "પહેલાં", "ઉપર", "નીચે", "અંદર", "બહાર", "તરફ", "જેવું", "જેવી",
    "જેવા", "પ્રમાણે",

    # Relative and interrogative words
    "જે", "જેને", "જેનું", "જેની", "જેના", "જેમ", "જ્યાં", "ત્યાં",
    "શું", "કોણ", "કોને", "કોનું", "કયું", "કઈ", "કયા", "ક્યાં",
    "ક્યારે", "કેમ", "કેવી", "કેવું", "કેટલું", "કેટલા", "કેટલી",

    # Quantifiers and determiners
    "બધું", "બધા", "બધી", "દરેક", "કંઈક", "કંઈ", "કોઈ", "કેટલાક",
    "એક", "બંને", "માત્ર", "ફક્ત", "ઘણું", "ઘણા", "ઘણી", "વધુ",
    "ઓછું", "અન્ય", "બીજું", "બીજા", "બીજી", "ખૂબ",

    # Adverbs of place and time
    "અહીં", "હવે", "આજે", "હમણાં", "ક્યારેક", "હંમેશા", "ફરી",

    # Auxiliary and copula verb forms
    "છે", "છું", "છીએ", "છો", "હતો", "હતી", "હતું", "હતા", "હશે",
    "થાય", "થયું", "થયો", "થઈ", "થયા", "થવું", "રહ્યો", "રહી",
    "રહ્યું", "રહ્યા", "ગયો", "ગઈ", "ગયું", "ગયા", "શકે", "જોઈએ",
    "વાળું", "વાળી", "વાળા",

    # Light verbs (high-frequency, low content)
    "કરવું", "કરે", "કરી", "કર્યું", "કર્યો", "કર્યા", "કરતા",
    "કરવા", "આપ્યું", "લીધું",

    # Negation and particles
    "નથી", "ન", "નહીં", "જ", "હા", "જી",
]

# Normalise to Unicode NFC and remove repeated entries, keeping the order.
gujarati_stopwords = list(dict.fromkeys(
    unicodedata.normalize("NFC", word) for word in gujarati_stopwords))


def remove_stopwords(text):
    """Return the words of `text` that are not Gujarati stop words."""
    stopwords = set(gujarati_stopwords)
    text = unicodedata.normalize("NFC", text)
    return [word for word in text.split() if word not in stopwords]


if __name__ == "__main__":
    sample = "હું આજે મારા મિત્ર સાથે બજારમાં ગઈ અને ત્યાંથી પુસ્તકો ખરીદ્યાં"
    print("Number of stop words:", len(gujarati_stopwords))
    print("Original sentence    :", sample)
    print("After removing stop words:", " ".join(remove_stopwords(sample)))
