import stanza
from stanza import Pipeline
from stanza.utils.conll import CoNLL
import sys
import argparse
import io
import os
from io import StringIO
from conllu import parse


def runningStanza(nlp,file):
    #nlp = stanza.Pipeline(lang=sys.argv[1], dir=sys.argv[2], download_method=None, processors='tokenize,lemma,pos,depparse')
    text = ""
    file_name = os.path.splitext(os.path.basename(str(file)))[0]

    with io.open(file,'r',encoding='utf8') as f:
        text = f.read()
        f.close()
    

    doc = nlp(text)

    conllu = StringIO()
    old_stdout = sys.stdout
    sys.stdout = conllu

    CoNLL.write_doc2conll(doc,sys.stdout)
    sys.stdout = old_stdout

    conllu = conllu.getvalue()

    sentences = parse(conllu)
    old_metadata = sentences[0].metadata
    new_metadata = {"newdoc id":file_name}
    new_metadata.update(old_metadata)
    sentences[0].metadata = new_metadata
    with open(file_name+'.conllu', 'w') as f:
        f.writelines([sentence.serialize() + "" for sentence in sentences])



def argParser():
    parser = argparse.ArgumentParser(prog='Stanza file processor',add_help=True, description='Tool to process text files with stanza')
    parser.add_argument('-i','--input', nargs='+',type=str,help='specify input file/files',required=True)
    parser.add_argument('-l','--lang',type=str,help='specify language',default="",required=True)
    parser.add_argument('-m','--model',type=str,help='specify model directory',required=True)
        
    args = parser.parse_args()
    return args






if __name__ == "__main__":
    program_arguments = argParser()
    inputFiles  = program_arguments.input
    lang = program_arguments.lang
    model = program_arguments.model
    nlp = stanza.Pipeline(lang=lang, dir=model, download_method=None, processors='tokenize,lemma,pos,depparse')
    for file in inputFiles:
        runningStanza(nlp,file)

