# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:24:51 2024

@author: Brilyananda
"""
import ahocorasick
import string


class CheckWord:
    def __init__(self, kal:str):
        self.kalimat:str = kal
        self.read_text_word_id()
        self.read_text_word_en()
        self.remove_sentence_punctuation()
    
    # kumpulan kata-kata indonesia
    def read_text_word_id(self):
        with open("source/list_1.0.0.txt", "r") as file:
            self.words_id = file.read().splitlines()
    
    # kumpulan kata-kata english
    def read_text_word_en(self):
        with open("source/words_en.txt", "r") as file:
            self.words_en = file.read().splitlines()
    
    
    def remove_sentence_punctuation(self):
        self.clean_kal = self.kalimat.translate(str.maketrans("", "", string.punctuation))
        pass
    
    # english check
    @property
    def check_word_en(self):
        word_kal = self.check_word_wrong_id
        print(word_kal)
        ahor = ahocorasick.Automaton()
        
        for ind, word in enumerate(self.words_en):
            ahor.add_word(word, (ind, word))
            
        ahor.make_automaton()
        
        found_word_en = set()
        for end_idx, (insert_order, original_value) in ahor.iter(word_kal):
            found_word_en.add(original_value)
        
        word_in_kal_en = set(word_kal.split())
        not_found_kal = word_in_kal_en.difference(found_word_en)
        return not_found_kal
        
    # indonesia check
    @property
    def check_word_wrong_id(self):
        ahor = ahocorasick.Automaton()
        
        for idx, word in enumerate(self.words_id):
            ahor.add_word(word,(idx,word))
            
        ahor.make_automaton()
        
        found_word = set()
        for end_idx, (insert_order, original_value) in ahor.iter(self.clean_kal.lower()):
            found_word.add(original_value)
            
        word_in_kalimat = set(self.clean_kal.lower().split())
        not_found_words = word_in_kalimat.difference(found_word)
        
        return " ".join(not_found_words).lower()
    
    
if __name__ == "__main__":
    kal = CheckWord("Saya amazing akan pegi ke toko sebentar lagi untuk membeli beberapa kebutuhab. Kamu harus menonton filam ini, sangat seru! Mereka sedang belanjar untuk ujian besok, jadi tidak bisa ikut bermain blola. Kami menginap di hotle yang sangat nyaman selama liburan kemarin.")
    a = kal.check_word_en           
    print(a)        
            