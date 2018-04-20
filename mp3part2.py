import numpy as np
from math import e
import math
import random
from matplotlib import mpl,pyplot
label = []
train_set = []
with open('digitdata/optdigits-orig_train.txt') as train_file:
    i = 1
    for line in train_file:
        if i%33 == 0:
            label.append(int(line.strip()))
        i += 1

#print label
with open('digitdata/optdigits-orig_train.txt') as train_file:
    i = 1
    pic_bag = []
    pic = []
    for line in train_file:
        if i%33 == 0:
            pic_bag.append(pic)
            pic = []
            next
        for ch in line.strip():
            if i%33 != 0:
                pic.append(int(ch))
        i += 1

for i in pic_bag:
    array = np.array(i).reshape(32,32)
    train_set.append(array)
print "finish storing the materials, the number of pics are:"
print len(label)
print len(train_set)
# total 2436 pics

# random shuffle an recording list of the train_set
r = list(range(2436))

# create a weights array, with 10 1D vectors, each vector weigths a digit
# initial weights randomly
w = np.random.rand(10,32,32)

for i in range(10):
    for j in range(32):
        for k in range(32):
            w[i][j][k] = w[i][j][k]*2 - 1




for epoch_num in range(9):
    random.shuffle(r)
    for pic_idx in r:
        target_found = False
        number_classified = 0
        cur_label = label[pic_idx]
        #print "starting the",epoch_num,"the epoch, the starting decay_rate is:",decay_rate
        decay_constant = 0
        while(number_classified != 1 or target_found == False):
            decay_constant += 1
            decay_rate = float(1)/(epoch_num + decay_constant)
            # print "decay_rate", decay_rate
            target_found = False
            number_classified = 0


            # has to traverse from number 0-9 to check whether there is only one vector weights 1
            for w_idx in range(10):
                # y is the dot product of w and inputs features
                y = 0
                for i in range(32):
                    for j in range(32):
                        y += w[w_idx][i][j] * train_set[pic_idx][i][j]


                # current weight vector corresponds to the label, want it to be one
                if(w_idx == cur_label):
                    if y > 0:
                        target_found = True
                        number_classified += 1
                    else:
                        target_found = False
                        for i in range(32):
                            for j in range(32):
                                w[w_idx][i][j] += float(train_set[pic_idx][i][j])*decay_rate


                else:
                    if y >= 0:
                        number_classified += 1
                        for i in range(32):
                            for j in range(32):
                                w[w_idx][i][j] -= float(train_set[pic_idx][i][j])*decay_rate


        if(pic_idx % 100 == 0 or pic_idx > 2433):
            print "finish evaluating", pic_idx, "th picture"

    print "this is the", epoch_num, "th epoch"
    epoch_num += 1;

    # print "weight vectors after the first pic"
    # print "w[0][0]"
    # print w[0][0]

    # print "w[1][0]"
    # print w[1][0]
    # print "w[2][0]"
    # print w[2][0]
    # print "w[3][0]"
    # print w[3][0]
    # print "w[4][0]"
    # print w[4][0]
###########################################################################################33
####VISUAL################################################################################
# fig = pyplot.figure(0)
# # cmap = mpl.colors.ListedColormap(['blue','black','red','green', 'yellow'])
# cmap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap', ['blue','black','red'],256)
# # bounds = [-100, -1/e, -1/pow(e,2), 1/pow(e,2), 1/e, 100]
# # norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
#
# img = pyplot.imshow(w[0], interpolation='nearest', cmap = cmap,origin = 'upper')
#
# # make a color bar
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image0.png")
#
#
# fig = pyplot.figure(1)
#
# img = pyplot.imshow(w[1], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image1.png")
#
#
# fig = pyplot.figure(2)
#
# img = pyplot.imshow(w[2], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image2.png")
#
#
# fig = pyplot.figure(3)
#
# img = pyplot.imshow(w[3], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image3.png")
#
#
# fig = pyplot.figure(4)
#
# img = pyplot.imshow(w[4], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image4.png")
#
#
# fig = pyplot.figure(5)
#
# img = pyplot.imshow(w[5], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image5.png")
#
#
# fig = pyplot.figure(6)
#
# img = pyplot.imshow(w[6], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image6.png")
#
#
# fig = pyplot.figure(7)
#
# img = pyplot.imshow(w[7], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image7.png")
#
#
# fig = pyplot.figure(8)
#
# img = pyplot.imshow(w[8], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image8.png")
#
#
# fig = pyplot.figure(9)
#
# img = pyplot.imshow(w[9], interpolation='nearest', cmap = cmap,origin = 'upper')
# pyplot.colorbar(img, cmap=cmap)
# fig.savefig("image9.png")
# #


##############################################################################################
# create test_set
label2 = []
test_set = []
correct_answer = 0
incorrect_answer = 0
with open('digitdata/optdigits-orig_test.txt') as test_file:
    i = 1
    for line in test_file:
        if i%33 == 0:
            label2.append(int(line.strip()))
        i += 1

#print label
with open('digitdata/optdigits-orig_test.txt') as test_file:
    i = 1
    pic_bag2 = []
    pic2 = []
    for line in test_file:
        if i%33 == 0:
            pic_bag2.append(pic2)
            pic2 = []
            next
        for ch in line.strip():
            if i%33 != 0:
                pic2.append(int(ch))
        i += 1

for i in pic_bag2:
    array = np.array(i).reshape(32,32)
    test_set.append(array)
print "finish storing the test set, the number of pics are:", len(label2)

# initialize the confusion matrix
confusion_matrix = np.zeros((10,10))



# the length of test set is 444
for test_idx in range(444):
    cur_weight = [float(0)]*10
    for w_idx2 in range(10):
        for i in range(32):
            for j in range(32):
                cur_weight[w_idx2] += w[w_idx2][i][j] * test_set[test_idx][i][j]

    answer = cur_weight.index(max(cur_weight))

    # record the result in confusion_matrix
    confusion_matrix[answer][label2[test_idx]] += 1
    if(answer == label2[test_idx]):
        correct_answer += 1;
    else:
        incorrect_answer +=1;

c_matrix = np.zeros((10,10))
for i in range(10):
    for j in range(10):
        c_matrix[i][j] = format(confusion_matrix[i][j]/(confusion_matrix[0][j]+confusion_matrix[1][j]+confusion_matrix[2][j]+confusion_matrix[3][j]+confusion_matrix[4][j]+confusion_matrix[5][j]+confusion_matrix[6][j]+confusion_matrix[7][j]+confusion_matrix[8][j]+confusion_matrix[9][j]),'.3f')

print "the number of correct recognition is :", correct_answer, "the number of incorrect recognition is: ", incorrect_answer
print "the overall accuracy is:", float(correct_answer)/float(444)
print "the confusion_matrix is:"
print c_matrix
