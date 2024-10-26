import speedtest #Impor modul speedtest --> Agar dapat melakukan tes jaringan
internet = speedtest.Speedtest()
donwload =internet.download()/1_000_000 #Konversi kecepatan donwload dari bit ke Mbps
upload =internet.upload()/1_000_000 #Konversi kecepatan donwload dari bit ke Mbps
ping = internet.results.ping # Mengambil nilai ping dari hasil pengujian

print("Kecepatan internet anda saat ini: ")
print("___________________________________")
print("")
print("")
print(f"Kecepatan donwload anda saat ini :{round(donwload, 2)} Mbps ")
print("")
print(f"Kecepatan upload anda saat ini :{round(upload, 2)} Mbps ")
print("")
print(f"Ping:{round(ping)}ms")
