import dw_mp3
import conv
import c_wav
import w_csv
 
name_mp3='test_voice.mp3'
name_wav="test.wav"
name_csv="test.csv"
 
url = input('Enter URL：')
dw_mp3.dw_mp3(url,name_mp3)
conv.conv(name_mp3,name_wav)
c_wav.c_wav(name_wav)
w_csv.w_csv(name_csv)
 
print("全ての処理が完了しました")