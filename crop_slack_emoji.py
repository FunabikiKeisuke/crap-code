import os

from PIL import Image


def crop_slack_emoji(dir_path, img_path, rowcol):
    """画像を分割して保存する。
    
    Args:
        dir_path (String): 分割した画像を保存するディレクトリのパス。
        img_path (String): 分割する画像のパス。
        rowcol (Int): 分割の一辺の数。

    Raises:
        ValueError: rowcol に 1 未満の数値が指定してある場合。
    """
    os.makedirs(dir_path, exist_ok=True)  # ディレクトリの作成
    crop_img = Image.open(img_path)  # 画像の取得
    rows = cols = rowcol  # 行番号と列番号を設定

    # 例外処理
    if rowcol < 1:
        raise ValueError('rowcol={} rowcolに1以上の整数を指定してください。'.format(rowcol))

    # 画像の中心で正方形に切り取る
    if crop_img.width > crop_img.height:
        square_img = crop_img.crop(((crop_img.width - crop_img.height) / 2, 0,
                                    (crop_img.width - crop_img.height) / 2 + crop_img.height, crop_img.height))
    elif crop_img.width < crop_img.height:
        square_img = crop_img.crop((0, (crop_img.height - crop_img.width) / 2,
                                    crop_img.width, (crop_img.height - crop_img.width) / 2 + crop_img.width))
    else:
        square_img = crop_img

    # 画像の一辺の長さを定義 (正方形なので width, height どちらでも)
    len_square_img = square_img.width

    # 行列の数だけループ
    for row in range(rows):
        for col in range(cols):
            # 画像の切り出し crop((left, upper, right, lower))
            left = 0 if col == 0 else len_square_img * col / rowcol
            upper = 0 if row == 0 else len_square_img * row / rowcol
            right = len_square_img * (col + 1) / rowcol
            lower = len_square_img * (row + 1) / rowcol
            tmp = square_img.crop((left, upper, right, lower))
            # 画像の保存
            tmp.save(dir_path + '/crop_{}_{}.jpg'.format(row + 1, col + 1))


if __name__ == "__main__":
    # 切り取った画像を保存するディレクトリパス
    crop_dir_path = 'crop_gude'
    # 切り取る画像のパス
    crop_img_path = "gude.jpg"
    # 関数の実行
    crop_slack_emoji(crop_dir_path, crop_img_path, 1)
