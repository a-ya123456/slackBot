import codecs
import datetime

class FileReadWrite:

    # ファイルを読み込むメソッド
    def file_read(self, path):
        try:
            # ファイルを開く
            target_file = codecs.open(path, "r", "utf_8")
            # ファイルを読み込む
            text = target_file.read()
            target_file.close()
        except:
            # エラーが出た時の例外処理
            text = "ng"

        return text

    # ファイルを書き込むメソッド
    def file_write(self, path, text):
        try:
            dt_now = datetime.datetime.now()
            dt_now += datetime.timedelta(hours=9)
            clock = dt_now.strftime('%Y年%m月%d日 %H:%M:%S\n')
            clock += text + '\n'

            target_file = codecs.open(path, "a", "utf_8")
            target_file.write(clock)
            result = "ok"
            target_file.close()
        except:
            # エラーが出た時の例外処理
            result = "ng"
        return result
