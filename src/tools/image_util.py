# coding=utf-8

import os

def read_load_label(label_path="label.txt"):
    """
     读取图片
     :params image_dir: 图片路径
     :params image_shape: 图片宽高dict 
     :params label_path: 12306图片分类label

    """
    label_object={}
    if os.path.exists(label_path):
        with open(label_path,encoding="utf-8") as files:
            for lines in files:
                # split 默认已空格拆分字符串
                lable_name,id = lines.strip().split()
                label_object[int(id)]=lable_name
    
    return label_object
 
    
