import matplotlib.pyplot as plt
import numpy as np
import time


import copy

"""

def loa(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    C4_1_img, C4_1_label, C2_0_img, C2_0_label, C6_2_img, C6_2_label = np.load(a), np.load(b), np.load(c), np.load(
        d), np.load(e), np.load(f)
    C8_3_img, C8_3_label, C10_4_img, C10_4_label = np.load(g), np.load(h), np.load(i), np.load(j)
    C12_5_img, C12_5_label, C14_6_img, C14_6_label, C16_7_img, C16_7_label = np.load(k), np.load(l), np.load(
        m), np.load(n), np.load(o), np.load(p)
    C18_8_img, C18_8_label, C20_9_img, C20_9_label = np.load(q), np.load(r), np.load(s), np.load(t)
    """
"""
    imgC=[]
    img = [C2_0_img,C4_1_img, C6_2_img]
    label = [C2_0_label,C4_1_label, C6_2_label]
    for i in range(3):
      if len(imgC) == 0:
        imgC = copy.deepcopy(img[i])
        labC = np.array(label[i])
      else:
        imgC = np.concatenate((imgC, img[i]), axis=0)
        labC = np.concatenate((labC, label[i]), axis=0)
    """
"""
    np.random.seed(116)
    np.random.shuffle(C4_1_img)
    np.random.seed(116)
    np.random.shuffle(C4_1_label)
    np.random.seed(64)
    np.random.shuffle(C2_0_img)
    np.random.seed(64)
    np.random.shuffle(C2_0_label)
    np.random.seed(62)
    np.random.shuffle(C6_2_img)
    np.random.seed(62)
    np.random.shuffle(C6_2_label)
    np.random.seed(604)
    np.random.shuffle(C8_3_img)
    np.random.seed(604)
    np.random.shuffle(C8_3_label)
    np.random.seed(602)
    np.random.shuffle(C10_4_img)
    np.random.seed(602)
    np.random.shuffle(C10_4_label)
    np.random.seed(624)
    np.random.shuffle(C12_5_img)
    np.random.seed(624)
    np.random.shuffle(C12_5_label)
    np.random.seed(642)
    np.random.shuffle(C14_6_img)
    np.random.seed(642)
    np.random.shuffle(C14_6_label)
    np.random.seed(42)
    np.random.shuffle(C16_7_img)
    np.random.seed(42)
    np.random.shuffle(C16_7_label)
    np.random.seed(642)
    np.random.shuffle(C18_8_img)
    np.random.seed(642)
    np.random.shuffle(C18_8_label)
    np.random.seed(42)
    np.random.shuffle(C20_9_img)
    np.random.seed(42)
    np.random.shuffle(C20_9_label)
    print(C4_1_img[0:int(C4_1_img.shape[0] * 0.6)].shape)
    X_train = np.concatenate((C4_1_img[0:int(C4_1_img.shape[0] * 0.6)], C2_0_img[0:int(C2_0_img.shape[0] * 0.6)]),
                             axis=0)
    for j in [C6_2_img, C8_3_img, C10_4_img, C12_5_img, C14_6_img, C16_7_img, C18_8_img, C20_9_img]:
        X_train = np.concatenate((X_train, j[0:int(j.shape[0] * 0.6)]), axis=0)

    y_train_label = np.concatenate(
        (C4_1_label[0:int(C4_1_img.shape[0] * 0.6)], C2_0_label[0:int(C2_0_img.shape[0] * 0.6)]), axis=0)
    for j in [C6_2_label, C8_3_label, C10_4_label, C12_5_label, C14_6_label, C16_7_label, C18_8_label, C20_9_label]:
        y_train_label = np.concatenate((y_train_label, j[0:int(j.shape[0] * 0.6)]), axis=0)

    X_valid = np.concatenate((C4_1_img[int(C4_1_img.shape[0] * 0.6):int(C4_1_img.shape[0] * 0.8)],
                              C2_0_img[int(C2_0_img.shape[0] * 0.6):int(C2_0_img.shape[0] * 0.8)]), axis=0)
    for j in [C6_2_img, C8_3_img, C10_4_img, C12_5_img, C14_6_img, C16_7_img, C18_8_img, C20_9_img]:
        X_valid = np.concatenate((X_valid, j[int(j.shape[0] * 0.6):int(j.shape[0] * 0.8)]), axis=0)

    y_valid_label = np.concatenate((C4_1_label[int(C4_1_img.shape[0] * 0.6):int(C4_1_img.shape[0] * 0.8)],
                                    C2_0_label[int(C2_0_img.shape[0] * 0.6):int(C2_0_img.shape[0] * 0.8)]), axis=0)
    for j in [C6_2_label, C8_3_label, C10_4_label, C12_5_label, C14_6_label, C16_7_label, C18_8_label, C20_9_label]:
        y_valid_label = np.concatenate((y_valid_label, j[int(j.shape[0] * 0.6):int(j.shape[0] * 0.8)]), axis=0)

    X_test = np.concatenate((C4_1_img[int(C4_1_img.shape[0] * 0.8):C4_1_img.shape[0]],
                             C2_0_img[int(C2_0_img.shape[0] * 0.8):C2_0_img.shape[0]]), axis=0)
    for j in [C6_2_img, C8_3_img, C10_4_img, C12_5_img, C14_6_img, C16_7_img, C18_8_img, C20_9_img]:
        X_test = np.concatenate((X_test, j[int(j.shape[0] * 0.8):j.shape[0]]), axis=0)

    y_test_label = np.concatenate((C4_1_label[int(C4_1_img.shape[0] * 0.8):C4_1_img.shape[0]],
                                   C2_0_label[int(C2_0_img.shape[0] * 0.8):C2_0_img.shape[0]]), axis=0)
    for j in [C6_2_label, C8_3_label, C10_4_label, C12_5_label, C14_6_label, C16_7_label, C18_8_label, C20_9_label]:
        y_test_label = np.concatenate((y_test_label, j[int(j.shape[0] * 0.8):j.shape[0]]), axis=0)

    # show_memory_info('6-1')
    np.random.seed(6264)
    np.random.shuffle(X_train)
    np.random.seed(6264)
    np.random.shuffle(y_train_label)
    np.random.seed(6462)
    np.random.shuffle(X_valid)
    np.random.seed(6462)
    np.random.shuffle(y_valid_label)
    np.random.seed(604)
    np.random.shuffle(X_test)
    np.random.seed(604)
    np.random.shuffle(y_test_label)
    # train,X_valid,train_label,y_valid_label = train_test_split(imgC, labC, test_size=0.2, random_state=62, shuffle=True)
    # X_train,X_test,y_train_label,y_test_label = train_test_split(train, train_label, test_size=0.25, random_state=64, shuffle=True)
    # del imgC, labC
    # del a,b,c,d,e,f
    # print(sys.getrefcount(C4_1_img), sys.getrefcount(C4_1_label), sys.getrefcount(C2_0_img), sys.getrefcount(C2_0_label), sys.getrefcount(C6_2_img), sys.getrefcount(C6_2_label), sys.getrefcount(img), sys.getrefcount(label))
    # b=[C4_1_img, C4_1_label, C2_0_img, C2_0_label, C6_2_img, C6_2_label, img, label,imgC, labC]
    # print(gc.collect())
    # time.sleep(10)
    # show_memory_info('6-2')
    return X_train, X_valid, X_test, y_train_label, y_valid_label, y_test_label

import numpy as np



datafile1 = u'D:/New/molecule_avo_fig/4/4/400/300X300/4C_1_img.npy'
datafile2 = u'D:/New/molecule_avo_fig/4/4/400/300X300/4C_1_label.npy'
datafile3 = u'D:/New/molecule_avo_fig/4/2/400/300X300/2C_0_img.npy'
datafile4 = u'D:/New/molecule_avo_fig/4/2/400/300X300/2C_0_label.npy'
datafile5 = u'D:/New/molecule_avo_fig/4/6/400/300X300/6C_2_img.npy'
datafile6 = u'D:/New/molecule_avo_fig/4/6/400/300X300/6C_2_label.npy'
datafile7 = u'D:/New/molecule_avo_fig/4/8/400/300X300/8C_3_img.npy'
datafile8 = u'D:/New/molecule_avo_fig/4/8/400/300X300/8C_3_label.npy'
datafile9 = u'D:/New/molecule_avo_fig/4/10/400X777775/300X300/10C_4_img.npy'
datafile10 = u'D:/New/molecule_avo_fig/4/10/400X777775/300X300/10C_4_label.npy'
datafile11 = u'D:/New/molecule_avo_fig/4/12/400X777775/300X300/12C_5_img.npy'
datafile12 = u'D:/New/molecule_avo_fig/4/12/400X777775/300X300/12C_5_label.npy'
datafile13 = u'D:/New/molecule_avo_fig/4/14/400X777775/300X300/14C_6_img.npy'
datafile14 = u'D:/New/molecule_avo_fig/4/14/400X777775/300X300/14C_6_label.npy'
datafile15 = u'D:/New/molecule_avo_fig/4/16/400X55555555/300X300/16C_7_img.npy'
datafile16 = u'D:/New/molecule_avo_fig/4/16/400X55555555/300X300/16C_7_label.npy'
datafile17 = u'D:/New/molecule_avo_fig/4/18/400X55555555/300X300/18C_8_img.npy'
datafile18 = u'D:/New/molecule_avo_fig/4/18/400X55555555/300X300/18C_8_label.npy'
datafile19 = u'D:/New/molecule_avo_fig/4/20/400X55555555/300X300/20C_9_img.npy'
datafile20 = u'D:/New/molecule_avo_fig/4/20/400X55555555/300X300/20C_9_label.npy'
X_train,X_valid,X_test,y_train_label,y_valid_label,y_test_label = loa(datafile1,datafile2,datafile3,datafile4,datafile5,datafile6,datafile7,datafile8,datafile9,datafile10,datafile11,datafile12,datafile13,datafile14,datafile15,datafile16,datafile17,datafile18,datafile19,datafile20)
#print(X_train[0:2])

np.save('X_train', X_train)
np.save('y_train_label', y_train_label)
np.save('X_test', X_test)
np.save('y_test_label', y_test_label)
np.save('X_valid', X_valid)
np.save('y_valid_label', y_valid_label)
"""


def lo(a, b, c, d):
    straight0_img, straight0_label, ring1_img, ring1_label= np.load(a), np.load(b), np.load(c), np.load(d)
    np.random.seed(62)
    np.random.shuffle(straight0_img)
    np.random.seed(62)
    np.random.shuffle( straight0_label)
    np.random.seed(64)
    np.random.shuffle(ring1_img)
    np.random.seed(64)
    np.random.shuffle(ring1_label)
    X_train = np.concatenate((straight0_img[0:int(straight0_img.shape[0] * 0.6)], ring1_img[0:int(ring1_img.shape[0] * 0.6)]),
                             axis=0)

    y_train_label = np.concatenate((straight0_label[0:int(straight0_label.shape[0] * 0.6)], ring1_label[0:int(ring1_label.shape[0] * 0.6)]), axis=0)

    X_valid = np.concatenate((straight0_img[int(straight0_img.shape[0] * 0.6):int(straight0_img.shape[0] * 0.8)],
                              ring1_img[int(ring1_img.shape[0] * 0.6):int(ring1_img.shape[0] * 0.8)]), axis=0)

    y_valid_label = np.concatenate((straight0_label[int(straight0_label.shape[0] * 0.6):int(straight0_label.shape[0] * 0.8)],
                                    ring1_label[int(ring1_label.shape[0] * 0.6):int(ring1_label.shape[0] * 0.8)]), axis=0)

    X_test = np.concatenate((straight0_img[int(straight0_img.shape[0] * 0.8):straight0_img.shape[0]],
                             ring1_img[int(ring1_img.shape[0] * 0.8):ring1_img.shape[0]]), axis=0)

    y_test_label = np.concatenate((straight0_label[int(straight0_label.shape[0] * 0.8):straight0_label.shape[0]],
                                   ring1_label[int(ring1_label.shape[0] * 0.8):ring1_label.shape[0]]), axis=0)
    np.random.seed(6264)
    np.random.shuffle(X_train)
    np.random.seed(6264)
    np.random.shuffle(y_train_label)
    np.random.seed(6462)
    np.random.shuffle(X_valid)
    np.random.seed(6462)
    np.random.shuffle(y_valid_label)
    np.random.seed(604)
    np.random.shuffle(X_test)
    np.random.seed(604)
    np.random.shuffle(y_test_label)

    return X_train, X_valid, X_test, y_train_label, y_valid_label, y_test_label

datafile1 = u'D:/New/molecule_avo_fig/ring/1/1200X300X300/no_resize/5C/5C0_img.npy'
datafile2 = u'D:/New/molecule_avo_fig/ring/1/1200X300X300/no_resize/5C/5C0_label.npy'
datafile3 = u'D:/New/molecule_avo_fig/ring/1/1200X300X300/no_resize/6C/6C1_img.npy'
datafile4 = u'D:/New/molecule_avo_fig/ring/1/1200X300X300/no_resize/6C/6C1_label.npy'

X_train,X_valid,X_test,y_train_label,y_valid_label,y_test_label = lo(datafile1,datafile2,datafile3,datafile4)
#print(X_train[0:2])

np.save('X_train', X_train)
np.save('y_train_label', y_train_label)
np.save('X_test', X_test)
np.save('y_test_label', y_test_label)
np.save('X_valid', X_valid)
np.save('y_valid_label', y_valid_label)
