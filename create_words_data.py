# -*- coding:utf-8 -*-

# --------------------------------------------------------
# 12306-captcha
# Copyright (c) 2017
# Licensed under The Apache License [see LICENSE for details]
# Written by ruifengshan
# --------------------------------------------------------

import os
import scipy.misc
from src.config import cfg
from src.tools.image_util import read_load_label

synset_file = cfg.ROOT + 'label\\synset'


# 将synset转换为train.txt文件
def load_file(path=synset_file):
    synset = [line.strip() for line in open(path).readlines()]
    print (synset)
    return synset

def create_file(data_path, file_list, file_name):
    """
    创建训练文件train.txt/test.txt

    :param data_path: 图片文件的上级路径
    :param file_list: synset生成的list
    :param train_file_name: 标签表
    :return:
    """

    try:
        #cnt = 0
        # Windows不支持此种写法
        #if not os.path.isfile(file_name):
        #    os.mknod(file_name)
        file_txt = open(file_name, mode='w')
        for key in file_list:
            print (key)
            file_path = os.path.join(data_path, file_list[key])
            print (file_path)
            if not os.path.isdir(file_path):
                print (file_path, '目录不存在')
                continue
            for path in os.listdir(file_path):
                file_txt.write(os.path.join(file_name, path) + " " + str(key) + "\n")
            #cnt += 1
    except Exception as e:
        print ("执行失败", e)


def create_train_file(data_path, file_list, train_file_name='words/train.txt'):
    create_file(data_path, file_list, train_file_name)


def create_test_file(data_path, file_list, test_file_name='words/test.txt'):
    create_file(data_path, file_list, test_file_name)


if __name__ == '__main__':
    create_train_file( "E:\\aaaaa\\download_captcha\\resize_words\\", read_load_label())
    create_test_file(  "E:\\aaaaa\\download_captcha\\resize_words\\", read_load_label() )
    #load_file()
    