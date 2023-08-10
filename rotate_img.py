import os
from pathlib import Path
from PIL import Image

def rotate_imgs(imgs_dir):
    imgs = os.listdir(imgs_dir)
    for each in imgs:
        img = Image.open(imgs_dir.joinpath(each))
        if img.height / img.width >= 1.5:
            img = img.transpose(Image.ROTATE_90)

    
        img.save(imgs_dir.joinpath(each))


if __name__ == "__main__":
    base_dir = Path("./dataset")
    test_dir = base_dir / "test" / "crop_img"
    train_dir = base_dir / "train" / "crop_img"
    val_dir = base_dir / "val" / "crop_img"


    rotate_imgs(test_dir)
    rotate_imgs(train_dir)
    rotate_imgs(val_dir)