"""
__author__ = "CLiGS"
__authors__ = "Christof Schoech, Daniel Schloer"
__email__ = "christof.schoech@uni-wuerzburg.de"
__license__ = ""
__version__ = "0.3.0"
__date__ = "2016-03-20"
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: model.py


##################################################################
###  Topic Modeling Workflow (tmw)                             ###
##################################################################

##################################################################
###  model.py - actual topic modeling with Mallet              ###
##################################################################


import os
import subprocess

#################################
# call_mallet_import            #
#################################


def call_mallet_import(mallet_path, infolder, outfolder, outfile, stoplist_project):
    """
	__author__ = "CLiGS"
	__authors__ = ""
	__email__ = ""

	Import text data into Mallet.
	"""
    print("\nLaunched call_mallet_import.")    
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)    
    ### Fixed parameters.
    token_regex = "'\p{L}[\p{L}\p{P}]*\p{L}'"
    ### Building the command line command    
    command = mallet_path + " import-dir --input " + infolder + " --output " + outfile + " --keep-sequence --token-regex " + token_regex + " --remove-stopwords TRUE --stoplist-file " + stoplist_project
    ## Make the call 
    subprocess.call(command, shell=True)
    print("Done.\n")



#################################
# call_mallet_modeling          #
#################################

def call_mallet_modeling(mallet_path, inputfile,outfolder,numOfTopics,optimize_interval,num_iterations,num_top_words,doc_topics_max):
    """
	__author__ = "CLiGS"
	__authors__ = ""
	__email__ = ""

	Perform topic modeling with Mallet.
	"""
    print("\nLaunched call_mallet_modeling.")

    ### Getting ready.
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)

    ### Fixed parameters    
    word_topics_counts_file = outfolder + "words-by-topics.txt"
    topic_word_weights_file = outfolder + "word-weights.txt"
    output_topic_keys = outfolder + "topics-with-words.csv"
    output_doc_topics = outfolder + "topics-in-texts.csv"
    output_topic_state = outfolder + "topic_state.gz"
    
    ### Constructing Mallet command from parameters.
    command = mallet_path +" train-topics --input "+ inputfile +" --num-topics "+ numOfTopics +" --optimize-interval "+ optimize_interval +" --num-iterations " + num_iterations +" --num-top-words " + num_top_words +" --word-topic-counts-file "+ word_topics_counts_file + " --topic-word-weights-file "+ topic_word_weights_file +" --output-state topic-state.gz"+" --output-topic-keys "+ output_topic_keys +" --output-doc-topics "+ output_doc_topics +" --doc-topics-max "+ doc_topics_max + " --output-state " + output_topic_state
    #print(command)
    subprocess.call(command, shell=True)
    print("Done.\n")


