#scriptStanza
import stanza
from stanza.utils.conll import CoNLL

# usage: python3 room_newmodels_MM.py treebank-to-parse.conllu model

# it can be used with a pipeline on pretokenized text to reprocess parts of the document

#filename = "../Desktop/LT4HALA/Inf_test.conllu"
#filename = "../Desktop/LT4HALA/Purg_test.conllu"
#filename = "./Desktop/TAL/LT4HALA/commenti/infernoall.conllu"
filename = "./TAL/CLIC25/CavalcantiWorkingRepository/poesie/Poesie_Cavalcanti.txt"
with open(filename, "r", encoding="utf-8") as f:
    text = f.read() 


#doc = CoNLL.conll2doc(filename)

#nlp = stanza.Pipeline(lang='it', processors='depparse', #tokenize_pretokenized=True,  
                      #depparse_pretagged=True, package="isdt")
                      #lemma_model_path=f'/lnet/work/people/gamba/sz-training/stanza/morphoharmo/mm-harmo-models-feb24/la_{model}-lemmatizer.pt', pos_model_path=f'/lnet/work/people/gamba/sz-training/stanza/morphoharmo/mm-harmo-models-feb24/la_{model}-tagger.pt', pos_pretrain_path='/lnet/work/people/gamba/sz-training/stanza/fasttext/Latin/cc.la.300-converted.pt', depparse_model_path=f'/lnet/work/people/gamba/sz-training/stanza/morphoharmo/mm-harmo-models-feb24/la_{model}-parser.pt', depparse_pretrain_path='/lnet/work/people/gamba/sz-training/stanza/fasttext/Latin/cc.la.300-converted.pt')


#nlp = stanza.Pipeline(lang='it', processors='depparse', tokenize_pretokenized=True,  
                      #depparse_pretagged=True, package="isdt")

nlp = stanza.Pipeline(lang='it', processors='tokenize,pos,lemma,depparse', package="isdt")  # ✅ Corrected


doc = nlp(text)
#conll_data = CoNLL.doc2conll(doc)


#CoNLL.write_doc2conll(doc, "../Desktop/LT4HALA/stanza_new/Inf1-3Stanza_vit.conllu")
#CoNLL.write_doc2conll(doc, "../Desktop/LT4HALA/stanza_new/Purg1-3Stanzavit.conllu")
CoNLL.write_doc2conll(doc, "./TAL/CLIC25/CavalcantiWorkingRepository/poesie/poesie_conllu/isdtpoesie.conllu")



# per fare solo parse task, usa solo processors="depparse", depparse_pretagged=True, package="isdt") 
#dove package specifica il tipo di treebank da scaricare

# il comando seguente specifica:
#nlp = stanza.Pipeline(lang='it', processors='#tokenize,lemma,pos,depparse', tokenize_pretokenized=True)

# per lanciare il comando ovviamente devi solo lanciare python3 (3!) e mettere il path o trascinare il presente file.

