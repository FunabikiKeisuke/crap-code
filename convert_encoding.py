import os
import glob
import codecs

# 再エンコードするディレクトリのパスを指定
src_dir_path = 'src'

# エンコードしたファイルを保存するディレクトリのパスを指定
dest_dir_path = 'utf8'

# dest_dir_path で指定したディレクトリが存在しなければ作成
os.makedirs(dest_dir_path, exist_ok=True)

# ファイルを読み込む(拡張子指定可)
file = glob.glob(os.path.join(src_dir_path, '*.m'))

# ディレクトリ内を再帰的に処理
for f in file:
  # エンコード前の文字コードを指定してファイルを開く
  shift_jis_f = codecs.open(f, 'r', encoding='shift-jis')
  # エンコード後の文字コードを指定してファイルを開く
  utf_8_f = codecs.open(dest_dir_path + '/' + os.path.basename(f), 'w', encoding='utf-8')

  # 再エンコードして書き込み
  for line in shift_jis_f:
      utf_8_f.write(line)
  shift_jis_f.close()
  utf_8_f.close()