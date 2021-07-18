import librosa
import librosa.display
import matplotlib.pyplot as plt
import scipy
import numpy as np
import scipy.io as sio
import scipy.io.wavfile


wav_file1 = '윤종신 좋니 crop.wav'
wav_file2 = '민서 좋아 crop .wav'
wav_file3='나얼바람기억.wav'
wav_file4='벤바람기억.wav'
wav_file5='intotheunknown남자.wav'
wav_file6='intotheunknown여자.wav'



y,sr=librosa.load(wav_file1)
y2,sr2=librosa.load(wav_file2)
y3,sr3=librosa.load(wav_file3)
y4,sr4=librosa.load(wav_file4)
y5,sr5=librosa.load(wav_file5)
y6,sr6=librosa.load(wav_file6)




Dp=librosa.stft(y)
D=np.abs(Dp)
DD=np.copy(Dp)
plt.figure(1)
librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.min), y_axis='log', x_axis='time')
plt.title('man Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%2.0f dB')
plt.tight_layout()
for i in range(len(DD)):
    for j in range(len(DD[0])):
        if DD[i][j] < 25.0:
            DD[i][j] = 0
        else:
            DD[i][j]=185.0


plt.figure(2)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(DD),ref=np.min),y_axis='log',x_axis='time')
plt.title('man Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

Df=librosa.istft(DD)
scipy.io.wavfile.write("testOut.wav",22050,Df)
plt.show()



Dp1=librosa.stft(y2)
D1=np.abs(Dp1)
DD1=np.copy(Dp1)
plt.figure(3)
librosa.display.specshow(librosa.amplitude_to_db(D1,ref=np.min), y_axis='log', x_axis='time')
plt.title(' woman Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%2.0f dB')
plt.tight_layout()
for i in range(len(DD1)):
    for j in range(len(DD1[0])):
        if DD1[i][j] < 25.0:
            DD1[i][j] = 0
        else:
            DD1[i][j]=185.0


plt.figure(4)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(DD1),ref=np.min),y_axis='log',x_axis='time')
plt.title('woman Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

Df2=librosa.istft(DD1)

scipy.io.wavfile.write("testOut2.wav",22050,Df2)#44100,Df)
plt.show()


Dp2=librosa.stft(y3)
D2=np.abs(Dp2)
DD2=np.copy(Dp2)
plt.figure(5)
librosa.display.specshow(librosa.amplitude_to_db(D2,ref=np.min), y_axis='log', x_axis='time')
plt.title('man Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%2.0f dB')
plt.tight_layout()
for i in range(len(DD2)):
    for j in range(len(DD2[0])):
        if DD2[i][j] < 25.0:
            DD2[i][j] = 0
        else:
            DD2[i][j]=185.0


plt.figure(6)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(DD2),ref=np.min),y_axis='log',x_axis='time')
plt.title(' man Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

Df2=librosa.istft(DD2)
scipy.io.wavfile.write("testOut3.wav",22050,Df2)#44100,Df)
plt.show()



Dp3=librosa.stft(y4)
D3=np.abs(Dp3)
DD3=np.copy(Dp3)
plt.figure(7)
librosa.display.specshow(librosa.amplitude_to_db(D3,ref=np.min), y_axis='log', x_axis='time')
plt.title('woman Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%2.0f dB')
plt.tight_layout()
for i in range(len(DD3)):
    for j in range(len(DD3[0])):
        if DD3[i][j] < 25.0:
            DD3[i][j] = 0
        else:
            DD3[i][j]=185.0


plt.figure(8)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(DD3),ref=np.min),y_axis='log',x_axis='time')
plt.title('woman Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

Df3=librosa.istft(DD3)

scipy.io.wavfile.write("testOut4.wav",22050,Df3)#44100,Df)
plt.show()



Dp4=librosa.stft(y5)
D4=np.abs(Dp4)
DD4=np.copy(Dp4)
plt.figure(9)
librosa.display.specshow(librosa.amplitude_to_db(D4,ref=np.min), y_axis='log', x_axis='time')
plt.title('man Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%2.0f dB')
plt.tight_layout()
for i in range(len(DD4)):
    for j in range(len(DD4[0])):
        if DD4[i][j] < 25.0:
            DD4[i][j] = 0
        else:
            DD4[i][j]=185.0


plt.figure(10)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(DD1),ref=np.min),y_axis='log',x_axis='time')
plt.title('man Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

Df4=librosa.istft(DD4)

scipy.io.wavfile.write("testOut5.wav",22050,Df4)#44100,Df)
plt.show()



Dp5=librosa.stft(y6)
D5=np.abs(Dp5)
DD5=np.copy(Dp5)
plt.figure(11)
librosa.display.specshow(librosa.amplitude_to_db(D5,ref=np.min), y_axis='log', x_axis='time')
plt.title('women Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%2.0f dB')
plt.tight_layout()
for i in range(len(DD5)):
    for j in range(len(DD5[0])):
        if DD5[i][j] < 25.0:
            DD5[i][j] = 0
        else:
            DD5[i][j]=185.0


plt.figure(12)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(DD5),ref=np.min),y_axis='log',x_axis='time')
plt.title('women Power spectrogram')
plt.ylim(715,1300)
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

Df5=librosa.istft(DD5)

scipy.io.wavfile.write("testOut6.wav",22050,Df5)#44100,Df)
plt.show()