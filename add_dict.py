import os
from pathlib import Path

def concat_dict():
    data_path = Path("./data/1")
    labels = list(data_path.rglob("*_rec_gt.txt"))

    # concat all labels
    all_labels = []
    for each_label_path in labels:
        with open(each_label_path, "r", encoding="utf-8") as f:
            all_labels.extend(f.readlines())

    n_total = len(all_labels)
    for i in range(n_total):
        all_labels[i] = all_labels[i].rstrip("\n")

    all_gts = [each.split("\t")[-1] for each in all_labels]
    new_dict = set()
    for each_gt in all_gts:
        for each_word in each_gt:
            new_dict.add(each_word)

    # with open("/home/qiubinglin/projects/paddleOCR/ppocr/utils/dict/chinese_cht_dict.txt",
    #           "r", encoding="utf-8") as f:
    #     old_dict_list = f.readlines()

    # for i, word in enumerate(old_dict_list):
    #     old_dict_list[i] = word.rstrip("\n")
    
    # for each_old_word in old_dict_list:
    #     new_dict.add(each_old_word)

    new_dict_list = list(new_dict) 

    for i, word in enumerate(new_dict_list):
        new_dict_list[i] = word + "\n"
    
    with open("/home/qiubinglin/projects/paddleOCR/ppocr/utils/dict/my_chinese_cht_dict_simple.txt",
             "w", encoding="utf-8") as f:
        f.writelines(new_dict_list)

   

if __name__ == "__main__":
    concat_dict()