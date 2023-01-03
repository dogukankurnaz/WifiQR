from pickle import FALSE
import wifi_qrcode_generator as qr

qrCode = qr.wifi_qrcode('WIFI NAME',False,'WPA','PASSWORD') #EDIT THIS BLOCK (WIFINAME AND WIFI PASSWORD)
qrCode.show()

qrCode.save('qrcode.png')
