import wave
import struct
import math
import os
from scipy import fromstring, int16
 
def c_wav(name_wav):
    #A列～ZZ列までの場合
    def toAlpha2(num):
        i = int((num-1)/26)
        j = int(num-(i*26))
        Alpha = ''
        for z in i,j:
            if z != 0:
                Alpha += chr(z+64)
        return Alpha
 
    #読み込むファイル名
    f_name = name_wav
 
    #切り取り時間[sec]
    cut_time = 10
 
    # 保存するフォルダの作成
    file = os.path.exists("output")
    print(file)
 
    if file == False:
        os.mkdir("output")
 
    def wav_cut(name_wav,time): 
 
        # ファイルを読み出し
        wavf = name_wav
        wr = wave.open(wavf, 'r')
 
        # waveファイルが持つ性質を取得
        ch = wr.getnchannels()
        width = wr.getsampwidth()
        fr = wr.getframerate()
        fn = wr.getnframes()
        total_time = 1.0 * fn / fr
        integer = math.floor(total_time) # 小数点以下切り捨て
        t = int(time)  # 秒数[sec]
        frames = int(ch * fr * t)
        num_cut = int(integer//t)
 
        #　確認用
        print("Channel: ", ch)
        print("Sample width: ", width)
        print("Frame Rate: ", fr)
        print("Frame num: ", fn)
        print("Params: ", wr.getparams())
        print("Total time: ", total_time)
        print("Total time(integer)",integer)
        print("Time: ", t) 
        print("Frames: ", frames) 
        print("Number of cut: ",num_cut)
 
        # waveの実データを取得し、数値化
        data = wr.readframes(wr.getnframes())
        wr.close()
        X = fromstring(data, dtype=int16)
        print(X)
 
        for i in range(num_cut):
            print(i)
            # 出力データを生成
            outf = 'output/' + str(toAlpha2(i+1)) + '.wav' 
            start_cut = i*frames
            end_cut = i*frames + frames
            print(start_cut)
            print(end_cut)
            Y = X[start_cut:end_cut]
            outd = struct.pack("h" * len(Y), *Y)
 
            # 書き出し
            ww = wave.open(outf, 'w')
            ww.setnchannels(ch)
            ww.setsampwidth(width)
            ww.setframerate(fr)
            ww.writeframes(outd)
            ww.close()
 
    wav_cut(f_name,cut_time)