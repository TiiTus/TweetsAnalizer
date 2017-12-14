************************************************
* Projet de Traitement Automatique des Langues *
* Analyse du caractère positif ou négatif de   *
* tweets.                                      *
* Jérémy Germain                               *
* Julien Hans                                  *
* Paul Renoult                                 *
* Charles Ris                                  *
************************************************

Prérequis pour l'utilisation de l'application :

  - /!\ l'application fonctionne uniquement sous python 3.x
  - la librairie tweepy
    - Installation :
        pip3 install tweepy
            OU
        git clone git://github.com/tweepy/tweepy.git
        cd tweepy
        python setup.py install

  - Stanford CoreNLP (https://stanfordnlp.github.io/CoreNLP/download.html)

Utilisation :

  - Pour récupérer des tweets, lancez le script getTweets.py
    l'application vous demandera d'entrer le ou les mots que vous souhaitez
    chercher ainsi que le nombre de tweets voulu. (Un exemple de résultats est contenu
    dans tweets.txt avec 300 tweets contenants "Trump").

  - Pour nettoyer les résultats obtenus précédemment, lancez le script cleanTweets.py
    qui retire les URLs, emojis, etc... (Un exemple de résultats est contenu
    dans cleanedTweets.txt)

  - Pour "tokenizer" ensuite les tweets nettoyés, il vous faudra copier-coller le
    fichier de résultats cleanedTweets.txt dans le dossier Stanford CoreNLP préciser
    dans les prérequis ci-dessus. Ensuite, lancez la commande suivante dans un terminal, dans le
    dossier stanford-corenlp-full-2017-06-09 :

      java -mx1g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma -file cleanedTweets.txt

  - Enfin, cette commande va créer un fichier XML qu'il suffit de copier-coller dans le dossier
    de cette application (à la racine), puis lancez le script readXML.py qui va afficher les
    scores positifs et négatifs de chaque tweet.
