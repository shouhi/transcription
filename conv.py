import pydub
 
def conv(name_mp3,name_wav):
    base_file=pydub.AudioSegment.from_mp3(name_mp3)
    base_file.export(name_wav,format="wav")