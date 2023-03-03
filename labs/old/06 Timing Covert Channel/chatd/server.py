# Chat Covert Channel (server)
# Author: Dr. Jean Gourd
# Encodes a covert message within an overt one. The overt message is sent to
# clients in a chat-like form. It ends with "EOF". The covert message is
# transmitted as delays in between each overt message character. There are
# two unique delays: one that is interpreted as a binary 0, and the other
# that is interpreted as a binary 1. If the overt message is longer than is
# necessary to encode the covert message, the covert message may be repeated
# until the full overt message has been transmitted. To know when the covert
# message ends, it is also terminated with "EOF".
# Use this to create overt/covert messages so that you can test your code.
# Set the variables below as appropriate.

# VARIABLES
ZERO = 0.025	# 0.025s in between overt transmits for a 0
ONE = 0.1	# 0.1s in between overt transmits for a 1
BITS = 8	# the number of bits to encode ASCII (either 7 or 8)

#############################
# DO NOT EDIT BELOW THIS LINE
#############################

import sys
from binascii import hexlify
import socket
import time
from random import randint
import threading

# the overt message to send every time a client connects
TEXT = [ "I before E except after C...or when going on a heist with a weird, feisty, beige foreign neighbor...or when caffeine-strung atheists reinvent protein at their leisure...or when plebeians deign to forfeit their language--well, either that or perhaps to seize and reinvent it...\n" ]
COVERT_PREFIX = "Your passphrase: "

# various hidden messages
# see: http://www.yougowords.com/14-letters
messages = [ "abarticulation", "abdominoplasty", "abdominousness", "abominableness", "absentmindedly", "absquatulation", "abstemiousness", "abstractedness", "abstractionist", "Acanthocephala", "acanthocytosis", "acceptableness", "accommodations", "accomplishable", "accomplishment", "accountability", "achondroplasia", "achondroplasty", "acknowledgment", "Acnidosporidia", "actinomyxidian", "acupunctuation", "adenocarcinoma", "administrating", "administration", "administrative", "admissibleness", "affectionately", "aforementioned", "aftersensation", "aggrandizement", "aggressiveness", "allegorization", "alliteratively", "alphabetically", "altruistically", "ambassadorship", "ammonification", "amorphophallus", "anagrammatical", "anathematizing", "anesthesiology", "Anguilliformes", "Anthoceropsida", "Anthocerotales", "anthropologist", "anthropometric", "anthropopathic", "anthropotheism", "anthropotheist", "antiadrenergic", "antiarrhythmic", "anticonvulsant", "antidepressant", "antineoplastic", "antiperspirant", "antiquarianism", "appendicularia", "appetizingness", "apprehensively", "apprenticeship", "arboricultural", "archaebacteria", "archaeological", "archaeotherium", "archidiaconate", "arrondissement", "arthrocentesis", "articulateness", "Asclepiadaceae", "associationism", "astroalchemist", "astrochemistry", "astrophysicist", "asymptotically", "attractiveness", "Auriculariales", "auspiciousness", "authentication", "autobiographer", "automatization", "automysophobia", "autoplagiarism", "autosuggestion", "backscratching", "bastardisation", "bastardization", "beautification", "benevolentness", "benzodiazepine", "biodegradation", "bioengineering", "bioluminescent", "bioremediation", "blithesomeness", "boisterousness", "braunschweiger", "breathlessness", "Brobdingnagian", "bronchodilator", "bullheadedness", "businesspeople", "businessperson", "candlelighting", "capitalisation", "capitalization", "cardiovascular", "Caryophyllales", "categorisation", "categorization", "censoriousness", "centralisation", "centralization", "centrifugation", "changelessness", "channelisation", "characteristic", "characterizing", "charitableness", "chemosynthesis", "chickenhearted", "choicelessness", "cholelithiasis", "chromatography", "cinematography", "circuitousness", "clavicytherium", "cleistothecium", "collectiveness", "commissionaire", "communications", "comprehensible", "concretization", "condescendence", "conduplication", "conglomeration", "conglutination", "congratulation", "conjunctivitis", "connaturalness", "conscienceless", "Constantinople", "constructivism", "consubstantial", "consuetudinary", "contagiousness", "contestability", "contraindicate", "contraposition", "contrapositive", "coolheadedness", "correspondence", "counterculture", "counterfeiting", "countermeasure", "countervailing", "counterworking", "decolonization", "decolorization", "decompensation", "deconstruction", "defenestration", "defibrillation", "dehumanization", "delightfulness", "delocalization", "demisemiquaver", "demobilisation", "demobilization", "demonetisation", "demoralization", "deossification", "dependableness", "depigmentation", "depolarisation", "depolarization", "dermatomycosis", "desalinization", "detoxification", "Deuteromycetes", "devitalisation", "directionality", "disaffirmation", "disambiguation", "disappointment", "disciplinarian", "discolouration", "discouragement", "discriminating", "discrimination", "disembarkation", "disembowelment", "disenchantment", "disgustingness", "disillusioning", "disinclination", "disinheritance", "disintegrating", "disintegrative", "disinvolvement", "disorderliness", "disorientation", "distinguishing", "diverticulitis", "effortlessness", "egalitarianism", "electioneering", "electrocoating", "electrogilding", "electrokinetic", "electrophysics", "Elisabethville", "emotionalizing", "erythrocytosis", "erythropoiesis", "exceptionality", "existentialism", "exponentiation", "expressionless", "exsanguination", "extemporaneous", "fallaciousness", "farsightedness", "fatherlessness", "featherbedding", "federalisation", "figurativeness", "fingerspelling", "flabbergasting", "fluidification", "foreordination", "foreseeability", "foreshortening", "forthrightness", "fraternisation", "fraternization", "frontierswoman", "fundamentalism", "generalisation", "generalization", "gentrification", "gerrymandering", "glottalization", "grandiloquence", "groundbreaking", "hallucinogenic", "Hemipteronatus", "histoplasmosis", "historicalness", "homogenization", "humidification", "hyperextension", "hyperlipidemia", "hypersecretion", "hyperventilate", "hypnotherapist", "hypothetically", "hypothyroidism", "iatrochemistry", "identification", "immaterialness", "immobilisation", "immunoglobulin", "imperturbation", "implementation", "incapacitating", "incompleteness", "indefiniteness", "indestructible", "indoctrination", "inflexibleness", "influentiality", "infrastructure", "initialisation", "initialization", "insightfulness", "insignificance", "insurmountable", "intellectually", "interaffiliate", "intercommunion", "interconnected", "intermediately", "intermediation", "intermittently", "Internationale", "interplanetary", "interpretation", "intractability", "irreconcilable", "irreproachable", "irresoluteness", "knickerbockers", "languorousness", "lapidification", "lateralisation", "lateralization", "lechatelierite", "lexicalisation", "liberalization", "libertarianism", "libidinousness", "linguistically", "longitudinally", "lyophilisation", "lyophilization", "macroeconomics", "macroevolution", "malfunctioning", "malodorousness", "manageableness", "meaningfulness", "meditativeness", "Megalonychidae", "Mephistopheles", "metamerization", "metamorphosing", "metaphorically", "metempsychosis", "microbiologist", "microeconomics", "micrometeorite", "misapplication", "miscalculation", "misinformation", "mistranslation", "monoplacophora", "monopolisation", "monosaccharide", "motherlessness", "mountaineering", "multiplication", "musclebuilding", "nanotechnology", "naturalisation", "naturalization", "neighborliness", "neocolonialism", "nephroblastoma", "neutralisation", "neutralization", "nondisjunction", "norepinephrine", "noteworthiness", "novemdecillion", "openhandedness", "osteoarthritis", "outlandishness", "outmaneuvering", "outrageousness", "overpopulation", "overproduction", "overprotection", "overprotective", "overshadowment", "overstretching", "paleontologist", "particularness", "pasteurisation", "pasteurization", "performability", "permissiveness", "perniciousness", "persuasiveness", "phantasmagoria", "phantasmagoric", "pharmaceutical", "philanthropist", "philosophaster", "philosophizing", "photosynthesis", "plasmapheresis", "pneumoconiosis", "poikilothermic", "polymerisation", "polymerization", "popularisation", "popularization", "possessiveness", "predestination", "predisposition", "prefabrication", "presupposition", "prettification", "procrastinator", "professionally", "proprioception", "purposefulness", "quantification", "quinquesection", "quintessential", "radicalization", "reasonableness", "rebelliousness", "recapitulation", "reconciliation", "reconnaissance", "reconnoitering", "reconstruction", "redintegration", "regularisation", "rehabilitation", "reinforcements", "reintroduction", "reinvigoration", "remarkableness", "remorsefulness", "representation", "representative", "responsibility", "responsiveness", "retrogradation", "revitalisation", "Rhinocerotidae", "ridiculousness", "roadworthiness", "salubriousness", "sanctification", "saponification", "scatterbrained", "schematisation", "schematization", "schoolmistress", "schweinsteiger", "seasonableness", "septuagenarian", "serviceability", "sesquipedalian", "simplification", "slaughterhouse", "sophistication", "specialisation", "specialization", "staphylococcus", "stratification", "stultification", "submissiveness", "substantiating", "substantiation", "suggestibility", "suggestiveness", "superannuation", "supererogation", "superstructure", "suprainfection", "surprisingness", "suspiciousness", "systematicness", "tatterdemalion", "teleconference", "teleprocessing", "tergiversation", "thermodynamics", "thoughtfulness", "thyrotoxicosis", "tonguelessness", "topicalization", "transamination", "transformation", "transmigration", "transportation", "trichomoniasis", "trivialization", "ultramasculine", "unalterability", "unappreciation", "unapproachable", "unattributable", "unchangingness", "uncontrollable", "uncontroverted", "unconventional", "undemonstrable", "underestimated", "understandable", "understatement", "unenthusiastic", "unfrequentness", "unfriendliness", "unfruitfulness", "unidentifiable", "unindebtedness", "unintermittent", "universalistic", "unpleasantness", "unpoeticalness", "unpreparedness", "unsalutariness", "unsatisfaction", "unskillfulness", "utilitarianism", "weatherologist", "weightlessness", "Westernisation", "Westernization", "widespreadness", "Wollstonecraft", "Worcestershire", "worthwhileness", "Zoroastrianism" ]

# check to make sure that the garbage text is long enough to covertly transmit all of the hidden messages
print(f"For the current overt message, the full covert message may be up to {sum(len(t) for t in TEXT) // BITS - len('EOF')} characters long.")
print(f"With the prefix \"{COVERT_PREFIX}\", the covert message passphrase may be up to {sum(len(t) for t in TEXT) // BITS - len('EOF') - len(COVERT_PREFIX)} characters long.")
for i in messages:
    # each character in the message (plus EOF) takes either 7 or 8 bits (as specified in BITS)
    if ((len(COVERT_PREFIX) + len(i) + len("EOF")) * BITS > sum(len(t) for t in TEXT)):
        print(f"{i} is too long for the overt message!")
        exit()

# check for proper command line arguments
if (len(sys.argv) != 2):
    print(f"Usage: python3 {sys.argv[0]} <port>")
    exit()

# set the port
port = int(sys.argv[1])

# create the socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server started...")
    print("-----------------")

    # listen for clients
    s.bind(("", port))
    s.listen(0)
except socket.error as e:
    print(f"Error starting the server: {e}.")
    exit(-1)

# the client comm thread
def comm(c, addr):
    try:
        print(f"Client {addr} connected.")

        # set the (random) hidden message for the current client
        msg = COVERT_PREFIX + messages[randint(0, len(messages) - 1)] + "EOF"
        # convert it to binary
        bin_msg =""
        for i in msg:
            # convert each character to a full byte
            # hexlify converts ASCII to hex
            # int converts it to an integer
            # bin provides its binary representation (with a 0b prefix that must be removed)
            # zfill left-pads the bit string with 0s to ensure a full byte
            bin_msg += bin(int(hexlify(i.encode("utf-8")), 16))[2:].zfill(BITS)

        # send the garbage text, along with the hidden message
        print(f"Sending data (with hidden message \"{msg[:-3]}\")...")
        n = 0
        # send one line of the text at a time
        for line in TEXT:
            # send one character per line at a time
            for i in line:
                c.send(i.encode("utf-8"), socket.MSG_DONTWAIT)
                # calculate the appropriate delay for the hidden message
                if (bin_msg[n] == "0"):
                    time.sleep(ZERO)
                else:
                    time.sleep(ONE)
                # go to the next bit in the hidden message
                n = (n + 1) % len(bin_msg)
        # send EOF to signify end of data
        c.send("EOF".encode("utf-8"))
        c.close()
        print(f"Client {addr} disconnected.")
    # handle connection timeouts
    except socket.timeout:
        print(f"Client {addr} timed out.")
        c.close()
    # handle socket errors
    except socket.error:
        print(f"Client {addr} socket error.")
        c.close()

# handle clients connecting
# do this forever (well, until Ctrl+C)
while (True):
    try:
        # accept a client
        c, addr = s.accept()
        # set the timeout to 5s
        c.settimeout(5.0)
        # start the client comm thread
        threading.Thread(target=comm, args=(c, addr)).start()
    # Ctrl+C shuts down the server
    except KeyboardInterrupt:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        print("Server shutdown.")
        break

