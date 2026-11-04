"""
============================================================
Topic: Indic Language Stop Words for Natural Language Processing
============================================================
Author Name(s): Khushi Jha
Short Description: This file contains a stop-word list for Tamil, a
Dravidian language written in the Tamil script. These words may be
used during text preprocessing in Natural Language Processing (NLP),
for example to remove high-frequency function words (pronouns,
demonstratives, postpositions, conjunctions, auxiliary verbs and
particles) before keyword extraction, topic modelling or frequency
analysis.
Semester: Monsoon Semester 2026
Affiliation: Department of Humanities and Social Sciences,
Indian Institute of Technology (Indian School of Mines) Dhanbad

Note:
These lists contain illustrative examples only. Please modify them
accordingly.

Tamil is agglutinative: case endings and many particles are joined to
the word ("வீட்டில்" = in the house, "அவனும்" = he too), so a
whitespace-separated stop-word list catches only free-standing
function words. For fuller coverage, use a morphological analyser or
stemmer before removing stop words. Negation words such as "இல்லை"
and "அல்ல" change meaning; remove them from this list for tasks like
sentiment analysis.
============================================================
"""

import unicodedata


# 1. Tamil Stop Words
# Language: Tamil
# Script: Tamil

tamil_stopwords = [
    # Conjunctions and connectives
    "மற்றும்", "ஆனால்", "அல்லது", "எனவே", "ஆகவே", "ஏனெனில்",
    "என்றால்", "எனில்", "ஆனாலும்", "இருந்தாலும்", "அதனால்", "மேலும்",
    "அதாவது", "பின்னர்",

    # Quotative and linking forms ("that", "called", "as")
    "என்று", "என", "என்ற", "எனும்", "என்பது", "என்பதை", "எனப்படும்",

    # Personal pronouns
    "நான்", "நாம்", "நாங்கள்", "நீ", "நீங்கள்", "அவன்", "அவள்",
    "அவர்", "அவர்கள்", "இவன்", "இவள்", "இவர்", "இவர்கள்", "அது",
    "இது", "அவை", "இவை", "தான்", "தாம்", "தங்கள்",

    # Object, dative and possessive forms of pronouns
    "என்னை", "எனக்கு", "என்", "என்னுடைய", "நம்மை", "நமக்கு", "நம்",
    "நமது", "எங்களை", "எங்களுக்கு", "எங்கள்", "உன்னை", "உனக்கு", "உன்",
    "உங்களை", "உங்களுக்கு", "உங்கள்", "அவனை", "அவனுக்கு", "அவளை",
    "அவளுக்கு", "அவரை", "அவருக்கு", "அவரது", "அவர்களை", "அவர்களுக்கு",
    "அதை", "அதற்கு", "அதன்", "இதை", "இதற்கு", "இதன்", "அவற்றை",
    "தனது", "தன்",

    # Demonstratives and adverbs of place and manner
    "அந்த", "இந்த", "எந்த", "அங்கு", "இங்கு", "எங்கு", "அங்கே",
    "இங்கே", "எங்கே", "அப்படி", "இப்படி", "எப்படி",

    # Postpositions
    "உடன்", "கூட", "இருந்து", "வரை", "பற்றி", "மூலம்", "போல",
    "போன்ற", "பின்", "முன்", "மேல்", "கீழ்", "உள்ளே", "வெளியே",
    "குறித்து", "சேர்ந்த", "விட", "ஆகிய",

    # Interrogative words
    "என்ன", "யார்", "ஏன்", "எது", "எவை", "எத்தனை", "எவ்வளவு",
    "யாரை", "யாருக்கு",

    # Quantifiers and determiners
    "எல்லா", "எல்லாம்", "அனைத்து", "அனைவரும்", "சில", "பல", "ஒரு",
    "ஒன்று", "இரண்டு", "மட்டும்", "மிக", "மிகவும்", "நிறைய",
    "கொஞ்சம்", "வேறு", "மற்ற", "ஒவ்வொரு", "யாரும்", "ஏதோ",
    "ஏதாவது", "எதுவும்",

    # Adverbs of time
    "அப்போது", "இப்போது", "எப்போது", "போது", "இன்று", "இனி",
    "இன்னும்", "ஏற்கனவே", "எப்போதும்", "மீண்டும்", "பிறகு",

    # Auxiliary and copula verb forms
    "உள்ளது", "உள்ளன", "உள்ள", "இருக்கிறது", "இருக்கின்றன",
    "இருந்தது", "இருந்தன", "இருக்கும்", "இருந்த", "இருக்க",
    "இருப்பது", "ஆகும்", "ஆனது", "ஆன", "ஆக", "ஆகிறது", "வேண்டும்",
    "முடியும்", "படும்", "பட்ட",

    # Light verbs (high-frequency, low content)
    "செய்து", "செய்ய", "செய்த", "செய்யும்", "கொண்டு", "கொண்ட",
    "விட்டு",

    # Negation and particles
    "இல்லை", "அல்ல", "இல்லாத", "கூடாது", "ஆம்",
]

# Normalise to Unicode NFC and remove repeated entries, keeping the order.
tamil_stopwords = list(dict.fromkeys(
    unicodedata.normalize("NFC", word) for word in tamil_stopwords))


def remove_stopwords(text):
    """Return the words of `text` that are not Tamil stop words."""
    stopwords = set(tamil_stopwords)
    text = unicodedata.normalize("NFC", text)
    return [word for word in text.split() if word not in stopwords]


if __name__ == "__main__":
    sample = "நான் இன்று என் நண்பருடன் சந்தைக்குச் சென்றேன் மற்றும் அங்கு சில புத்தகங்கள் வாங்கினேன்"
    print("Number of stop words:", len(tamil_stopwords))
    print("Original sentence    :", sample)
    print("After removing stop words:", " ".join(remove_stopwords(sample)))
