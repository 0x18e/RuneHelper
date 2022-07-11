#levenshtein distance
import numpy



def levenshteinFunc(token1, token2):
    distances = numpy.zeros((len(token1) + 1 , len(token2) + 1))
    #rows getting initialized
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    #columns getting initialized
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1-1][t2-1]
            else:
                a = distances[t1][t2-1]
                b = distances[t1-1][t2]
                c = distances[t1-1][t2-1]
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    #printDistances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]



def printDistances(distances, token1_length, token2_length):
    for t1 in range(token1_length + 1):
        for t2 in range(token2_length + 1):
            print(int(distances[t1][t2]), end=" ")
        print("")



def calcDictDistance(word, numWords):
    file = open('new_champions.txt', 'r')
    lines = file.readlines()
    file.close()
    dictWordDist = []
    wordIdx = 0
    for line in lines:
        wordDistance = levenshteinFunc(word, line.strip())
        if wordDistance >= 10:
            wordDistance = 9
        dictWordDist.append(str(int(wordDistance)) + "-" + line.strip())
        wordIdx = wordIdx + 1

    closestWords = []
    wordDetails = []
    currWordDist = 0
    dictWordDist.sort()
    for i in range(numWords):
        currWordDist = dictWordDist[i]
        wordDetails = currWordDist.split("-")
        closestWords.append(wordDetails[1])
    return closestWords
















































# conv = []
#
# with open('champions.txt', 'r') as file:
#     word = file.readlines()
#     print(word)
#
# new_list = [s.replace("\n", "") for s in word]
# print(new_list)
# while "" in new_list:
#     new_list.remove("")
#
# final_list = []
# for x in new_list:
#     final_list.append(x.lower())
#
# with open('new_champions.txt', 'w') as file:
#     for champ in final_list:
#        file.write(champ + "\n")
#
# #print(conv)
