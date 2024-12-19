import requests

# API endpoint
url = "https://publicapis.io/random-dog-animals-api"

# Sayaçlar
large_responses = 0
small_responses = 0

print("100 adet API isteği gönderiliyor... Lütfen bekleyin.\n")

# 100 istek gönderme
for i in range(100):
    try:
        response = requests.get(url)
        size = len(response.content)  # Yanıt boyutunu bayt cinsinden al
        if size > 1050000:
            large_responses += 1
        else:
            small_responses += 1
    except Exception as e:
        print(f"{i + 1}. istekte bir hata oluştu: {e}")

# Sonuçlar
print(f"1.050.000 bayttan büyük olan cevaplar: {large_responses}")
print(f"1.050.000 bayttan küçük veya eşit olan cevaplar: {small_responses}")
