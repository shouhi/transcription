import youtube_dl
import os
from pathlib import Path
 
def dw_mp3(url,name_mp3):
    # 初期設定
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s',
                                        'postprocessors': [{
                                            'key': 'FFmpegExtractAudio',
                                            'preferredcodec': 'mp3',
                                            'preferredquality': '192',
                                        }]
                                        })
 
    # 動画情報をダウンロードする
    with ydl:
        result = ydl.extract_info(
            url,
            download=True 
        )
 
    filename_before1 = url[32:] + 'webm' + '.mp3' # ファイル名にwebmが付くのでその対応
    print('filename_before1は：：：：：'+filename_before1)
    filename_after1 = name_mp3
    print('filename_after1は：：：：：'+filename_after1)
    current_dir = Path(os.getcwd())
 
    os.rename(current_dir/filename_before1, current_dir/filename_after1) 
 
    print('音声ファイルのダウンロードが完了しました')