#/////////////////////   IMPORTS   /////////////////////

import json 
import pandas as pd 
import matplotlib.pyplot as plt
import sklearn as skl

#/////////////////////   MAIN   /////////////////////

createPdfs(); 


#/////////////////////   Q1   /////////////////////


with open ("goemotions.json\goemotions.json") as f: 
    data =  json.load(f) 

df = pd.DataFrame(data, columns = ['Post', 'Emotions', 'Sentiment'])
print(df)

def createPdfs():

    # Make a count of all unique Emotions and Sentiments 
    countEmotions = df['Emotions'].value_counts()
    countSentiment = df['Sentiment'].value_counts()

    print(f"this is it dude{type(countSentiment)}")

    print(f"The list of Emotions counted \n {countEmotions} \nThe list of Emotions counted {countSentiment}")

    #Transforms the DF to a Dictionary with key value pairs 
    emotionDict = countEmotions.to_dict()
    sentimentDict = countSentiment.to_dict()

    # Function using matplot, takes two params. First assigns X coord to the emotion or sentiment, y value takes the assigned value pair
    plt.bar(emotionDict.keys(), emotionDict.values())
    #Rotate X param 90 degrees for readability, tight_layout adjusts padding of subplot
    plt.xticks(rotation=90)
    plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
    #Saves into PDF as it's root directory
    plt.savefig('Emotions-Plot.pdf', dpi = 1000) 
    #Shows the Plot
    plt.show()

    #Repeats steps for Sentiment
    plt.bar(sentimentDict.keys(), sentimentDict.values())
    plt.savefig('Sentiment-Plot.pdf')
    plt.show()



#/////////////////////   Q2  /////////////////////
skl.feature_extraction.text.CountVectorizer(data)