import os
from os.path import exists
from shutil import copy
from pathlib import Path
import random
import argparse
from tqdm import tqdm


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src",
        default="./raw_datasets/only_cao_img_data",
        type=str,
    )
    parser.add_argument(
        "--dst",
        default="./training_dataset",
        type=str,
    )
    args = parser.parse_args()
    return args.src, args.dst


def find_all_imgs_labels(src: Path, dst: Path):
    imgs = os.listdir(src / "crop_img")
    label_path = src / "rec_gt.txt"

    # concat all labels
    with open(label_path, "r", encoding="utf-8") as f:
        labels = f.readlines()

    n_total = len(labels)
    assert len(imgs) == n_total, "imgs and labels are not equal!"
    for i in range(n_total):
        labels[i] = labels[i].rstrip("\n")

    # split dataset
    random.shuffle(labels)

    n_train = int(n_total * 0.7)
    n_val = int(n_total * 0.2)
    n_test = int(n_total * 0.1)

    train_list = labels[:n_train]
    val_list = labels[n_train : n_train + n_val]
    test_list = labels[n_train + n_val :]

    move_and_save_gt(src, dst, train_list, "train")
    move_and_save_gt(src, dst, val_list, "val")
    move_and_save_gt(src, dst, test_list, "test")


def move_and_save_gt(src, dst, dataset_list, dataset_type):
    imgs_dir = dst / dataset_type / "crop_img"
    if not exists(imgs_dir):
        os.makedirs(imgs_dir)
    for i, each_img in enumerate(tqdm(dataset_list)):
        img_path = each_img.split("\t")[0]
        img_path = src / img_path
        copy(img_path, imgs_dir)
        dataset_list[i] = dataset_list[i] + "\n"

    with open(dst / dataset_type / "rec_gt.txt", "w", encoding="utf-8") as f:
        f.writelines(dataset_list)


if __name__ == "__main__":
    src, dst = args_parse()
    src, dst = Path(src), Path(dst)
    find_all_imgs_labels(src, dst)
