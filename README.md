# YOLO-Etiket-Kontrol

YOLO Etiket Kontrol, YOLO formatında etiketlenmiş görüntüleri kontrol etmenizi sağlayan bir araçtır. Özellikle resim boyutlarının değiştirilmesi sonrasında etiketlerin doğru konumda olup olmadığını kontrol etmek için kullanışlıdır.

## Özellikler

- YOLO formatında etiketlenmiş görüntüleri görüntüleme
- Etiket kutularını ve sınıf isimlerini görsel olarak gösterme
- Basit klavye kontrolleri ile görüntüler arası geçiş
- Eksik veya hatalı etiket kutuları görüntüleme.

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/ahmetmerttetik/yolo-etiket-kontrol.git
cd yolo-etiket-kontrol
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

Program aşağıdaki parametrelerle çalıştırılır:

```bash
python yolo_label_control.py --images [images dir] --labels [labels dir] --classes [classes.txt path]
```

veya

```bash
python yolo_label_control.py -i [images dir] -l [labels dir] -c [classes.txt path]
```

### Parametreler:

- `--images` veya `-i`: Görüntü dosyalarının bulunduğu klasör
- `--labels` veya `-l`: YOLO format etiket dosyalarının bulunduğu klasör
- `--classes` veya `-c`: Sınıf isimlerinin bulunduğu metin dosyası

### Klavye Kontrolleri:

- `a`: Sonraki görüntüye geç
- `q`: Programdan çık

## Dosya Yapısı

- Görüntü dosyaları: `.jpg`, `.jpeg` veya `.png` formatında olmalıdır
- Etiket dosyaları: Her görüntü için aynı isimde `.txt` dosyası
- Sınıf dosyası: Her satırda bir sınıf ismi içeren metin dosyası

### Etiket Formatı
YOLO formatında her satır şu şekilde olmalıdır:
```
<class_id> <x_center> <y_center> <width> <height>
```

## Gereksinimler

Projenin çalışması için gereken kütüphaneler requirements.txt dosyasında listelenmiştir.
