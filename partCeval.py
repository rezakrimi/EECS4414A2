import pickle
import random

with open('adamic_adar_idex.pkl', 'rb') as f:
    adar = pickle.load(f)

with open('jaccard_coefficient.pkl', 'rb') as f:
    jaccard = pickle.load(f)

with open('preferential_attachment.pkl', 'rb') as f:
    pref = pickle.load(f)

with open('T.pkl', 'rb') as f:
    T = pickle.load(f)

with open('fof.pkl', 'rb') as f:
    fof = pickle.load(f)

T = set(T)
K = [10, 20, 50, 100, len(T)]

for k in K:
    adarK = adar[:k]
    jaccardK = jaccard[:k]
    prefK = pref[:k]
    randomK = random.sample(fof, k)
    # include neighbours
    adar_score = 0
    jaccard_score = 0
    pref_score = 0
    random_score = 0
    for i in range(k):
        if (adarK[i][0], adarK[i][1]) in T or (adarK[i][1], adarK[i][0]) in T:
            adar_score += 1
        if (jaccardK[i][0], jaccardK[i][1]) in T or (jaccardK[i][1], jaccardK[i][0]) in T:
            jaccard_score += 1
        if (prefK[i][0], prefK[i][1]) in T or (prefK[i][1], prefK[i][0]) in T:
            pref_score += 1
        if (randomK[i][0], randomK[i][1]) in T or (randomK[i][1], randomK[i][0]) in T:
            random_score += 1

    print('scores for k=' + str(k))
    print('adar score: ' + str(adar_score/k))
    print('jaccard score: ' + str(jaccard_score/k))
    print('preferential score: ' + str(pref_score/k))
    print('random predictor score: ' + str(random_score/k))