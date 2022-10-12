import csv
import os
import speech_recognition as sr
import csv
 
def w_csv(name_csv):
    count=0
 
    with open(name_csv,'w') as f:
        writer = csv.writer(f)
 
    for fd_path, sb_folder, sb_file in os.walk('./output/'):
        for fil in sb_file:      
            count= count+1
            file_name=fd_path +fil
            r = sr.Recognizer()
            with sr.AudioFile(file_name) as source:
                audio = r.record(source)
                text = r.recognize_google(audio, language='ja-JP')  # 英語の場合はen-US
            print(count,fil," 文字起こし完了")
            print(text)
            with open(name_csv, 'a', newline='',encoding="shift_jis") as csvfile:
                write = csv.writer(csvfile, delimiter=' ')
                write.writerow([text])
