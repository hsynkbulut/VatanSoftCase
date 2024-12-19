# Random Dog API Response Size Check

Bu Python scripti, bir genel API'ye 100 istek gönderir ve yanıtları boyutlarına göre bayt cinsinden kategorize eder. Amaç, 1.050.000 bayttan büyük olan yanıtların sayısını ve bu eşikten küçük veya eşit olan yanıtların sayısını belirlemektir.

## Özellikler
- Belirtilen bir API uç noktasına 100 HTTP GET isteği gönderir.
- Her yanıtın boyutunu bayt cinsinden ölçer.
- Yanıtları "büyük" (1.050.000 bayttan büyük) ve "küçük/eşit" (1.050.000 bayt veya daha küçük) olarak kategorize eder.
- Kategorileştirme sonuçlarını terminalde gösterir.


## Kullanım

1. Scripti Python ile çalıştırın:
   ```bash
   python main.py
   ```
2. Script, sonuçları terminalde yazdıracaktır. Bu sonuçlar, kaç tane yanıtın büyük ve kaç tanesinin küçük/eşit olduğunu gösterecektir.

## Örnek Çıktı

Script çalıştırıldıktan sonra, aşağıdaki gibi bir çıktı alabilirsiniz:

```
100 adet API isteği gönderiliyor... Lütfen bekleyin.

1.050.000 bayttan büyük olan cevaplar: 25
1.050.000 bayttan küçük veya eşit olan cevaplar: 75
```

## Kod Açıklaması

- Script,  API Endpoint'ine GET istekleri göndermek için `requests` kütüphanesini kullanır.
- Yanıt boyutu, `len()` fonksiyonu kullanılarak yanıt içeriği üzerinde ölçülür.
- İki sayaç (`large_responses` ve `small_responses`), her kategoriye ait yanıt sayısını takip etmek için kullanılır.
- İstek sırasında oluşabilecek istisnalar yakalanır ve konsola yazdırılır.

##  API Endpoint

Script şu genel API ile iletişim kurar:

```
https://publicapis.io/random-dog-animals-api
```
