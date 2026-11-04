"""
============================================================
Topic: Indic Language Stop Words for Natural Language Processing
============================================================
Author Name(s): Khushi Jha
Short Description: This file contains a stop-word list for Bengali
(Bangla), an Indo-Aryan language written in the Bengali script. These
words may be used during text preprocessing in Natural Language
Processing (NLP), for example to remove high-frequency function words
(pronouns, postpositions, conjunctions, auxiliary verbs and particles)
before keyword extraction, topic modelling or frequency analysis.
Semester: Monsoon Semester 2026
Affiliation: Department of Humanities and Social Sciences,
Indian Institute of Technology (Indian School of Mines) Dhanbad

Note:
These lists contain illustrative examples only. Please modify them
accordingly.

Bengali has both a formal (sadhu bhasha) and a colloquial (cholito
bhasha) register; this list follows modern colloquial Bengali, with a
few common variant spellings ("কখনো" / "কখনও", "আরো" / "আরও").
The letter "য়" can be typed as one character or as "য" + nukta, so
both the list and the input text are normalised (Unicode NFC) before
comparison. Negation words such as "না" and "নয়" change meaning;
remove them from this list for tasks like sentiment analysis.
============================================================
"""

import unicodedata


# 1. Bengali Stop Words
# Language: Bengali
# Script: Bengali

bengali_stopwords = [
    # Conjunctions and connectives
    "এবং", "ও", "আর", "কিন্তু", "অথবা", "বা", "কিংবা", "যদি", "তবে",
    "তাহলে", "যদিও", "তবুও", "কারণ", "যেহেতু", "সুতরাং", "তাই",
    "অতএব", "অর্থাৎ", "নাকি", "যে", "বরং", "এমনকি",

    # Personal pronouns
    "আমি", "আমরা", "তুমি", "তোমরা", "আপনি", "আপনারা", "তুই", "তোরা",
    "সে", "তারা", "তিনি", "তাঁরা", "ইনি", "উনি", "এরা", "ওরা",
    "নিজে", "নিজের",

    # Object and possessive forms of pronouns
    "আমাকে", "আমার", "আমাদের", "তোমাকে", "তোমার", "তোমাদের",
    "আপনাকে", "আপনার", "আপনাদের", "তোকে", "তোর", "তাকে", "তার",
    "তাদের", "তাঁকে", "তাঁর", "তাঁদের", "একে", "এর", "এদের", "ওকে",
    "ওর", "ওদের", "এঁর", "ওঁর",

    # Demonstratives
    "এ", "এই", "ওই", "সেই", "এটা", "ওটা", "সেটা", "এটি", "ওটি",
    "সেটি", "এগুলো", "ওগুলো", "সেগুলো", "এখানে", "ওখানে", "সেখানে",

    # Postpositions
    "থেকে", "হতে", "দিয়ে", "দ্বারা", "জন্য", "জন্যে", "সঙ্গে", "সাথে",
    "কাছে", "মধ্যে", "ভিতরে", "ভেতরে", "বাইরে", "উপর", "ওপর", "উপরে",
    "নিচে", "পরে", "আগে", "পর্যন্ত", "প্রতি", "মতো", "মত", "বিনা",
    "ছাড়া", "নিয়ে", "সম্পর্কে", "দিকে", "পাশে",

    # Relative and interrogative words
    "যা", "যিনি", "যারা", "যাকে", "যার", "যাদের", "যখন", "তখন",
    "যেখানে", "কী", "কি", "কে", "কাকে", "কার", "কারা", "কোন",
    "কোথায়", "কখন", "কেন", "কেমন", "কীভাবে", "কত", "কতটা",

    # Quantifiers and determiners
    "সব", "সবাই", "সকল", "সমস্ত", "কিছু", "কোনো", "কেউ", "প্রত্যেক",
    "প্রতিটি", "এক", "একটি", "একটা", "দুই", "অনেক", "বেশি", "কম",
    "অন্য", "আরও", "আরো", "শুধু", "কেবল", "খুব", "অল্প",

    # Adverbs of time
    "এখন", "আজ", "কখনো", "কখনও", "সবসময়", "আবার", "ইতিমধ্যে",

    # Auxiliary and copula verb forms
    "হয়", "হয়ে", "হয়েছে", "হয়েছিল", "হবে", "হল", "হলো", "হচ্ছে",
    "হওয়া", "হলে", "ছিল", "ছিলেন", "ছিলাম", "আছে", "আছেন", "আছি",
    "থাকে", "থাকা", "নেই", "পারে", "পারেন", "উচিত",

    # Light verbs (high-frequency, low content)
    "করা", "করে", "করেন", "করেছে", "করেছেন", "করেছিল", "করবে",
    "করতে", "করছে", "দেওয়া", "দেয়", "নেওয়া", "গেছে", "গিয়ে", "যায়",
    "যাওয়া", "বলে",

    # Negation and particles
    "না", "নি", "নয়", "নাই", "তো", "যেন", "বুঝি", "হ্যাঁ",
]

# Normalise to Unicode NFC and remove repeated entries, keeping the order.
bengali_stopwords = list(dict.fromkeys(
    unicodedata.normalize("NFC", word) for word in bengali_stopwords))


def remove_stopwords(text):
    """Return the words of `text` that are not Bengali stop words."""
    stopwords = set(bengali_stopwords)
    text = unicodedata.normalize("NFC", text)
    return [word for word in text.split() if word not in stopwords]


if __name__ == "__main__":
    sample = "আমি আজ বন্ধুর সঙ্গে বাজারে গিয়েছিলাম এবং সেখানে কিছু বই কিনলাম"
    print("Number of stop words:", len(bengali_stopwords))
    print("Original sentence    :", sample)
    print("After removing stop words:", " ".join(remove_stopwords(sample)))
