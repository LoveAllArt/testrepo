def clean_list(doc_list):
    docs = [doc.lower() for doc in doc_list]
    docs_repl_1 = [doc.replace('.', ' ') for doc in docs]
    docs_repl_2 = [doc.replace(',', ' ') for doc in docs_repl_1]
    docs_words = [doc.split() for doc in docs_repl_2]
    return docs_words


def word_search(doc_list, keyword):
    docs_words = clean_list(doc_list)
    index_list = []
    for words_list in docs_words:
        for word in words_list:
            if word == keyword:
                pos = docs_words.index(words_list)
                index_list.append(pos)
    return list(set(list(index_list)))


doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
print( word_search(doc_list, 'casino') )
#[0]