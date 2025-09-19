# El Kontrol Oynatıcısı
## 📌 Proje Hakkında
Bu proje, **el hareketleriyle bilgisayarı kontrol etmeyi** sağlayan bir uygulamadır. Python ile geliştirilen sistem, `OpenCV` ve `Mediapipe` kütüphaneleriyle el hareketlerini algılar ve `PyAutoGUI` ile bilgisayarda belirli eylemleri otomatik gerçekleştirir. Örneğin:
- Avuç açma hareketi → YouTube veya medya oynatıcıda **oynat/duraklat**  
- Beş parmağı kapatma hareketi → **Ekran görüntüsü alma**  

Bu sayede fare veya klavye kullanmadan medya kontrolü ve hızlı işlemler yapılabilir.  


## ⚙️ Kullanılan Teknolojiler
- Python 3.11  
- OpenCV  
- Mediapipe  
- PyAutoGUI  



## 🚀 Kurulum
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install opencv-python mediapipe pyautogui
Projeyi çalıştırın:

bash

python el_kontrol.py

🎮 Kullanım
Elinizi kameraya gösterin.
Avuç açık → Müzik/video başlat veya duraklat.
Tüm parmakları kapalı (yumruk) → Ekran görüntüsü alır.
İstenirse farklı hareketler eklenerek yeni işlevler tanımlanabilir.



Hand Gesture Controller (English)
📌 About the Project
This project is an application that allows controlling the computer with hand gestures. Built with Python, it uses OpenCV and Mediapipe to detect hand gestures and PyAutoGUI to perform actions automatically. For example:

Open palm → Play/Pause a video or music player

Closed fist → Take a screenshot

This enables media control and quick actions without using a mouse or keyboard.

⚙️ Technologies Used
Python 3.11

OpenCV

Mediapipe

PyAutoGUI

🚀 Installation
Install the required libraries:

bash
Kodu kopyala
pip install opencv-python mediapipe pyautogui
Run the project:

bash

python el_kontrol.py

🎮 Usage
Show your hand to the camera.
Open palm → Starts or pauses a video/music.
Closed fist → Takes a screenshot.
New gestures can be added for different features.

