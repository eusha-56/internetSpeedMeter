import speedtest

wifi = speedtest.Speedtest()

print('\nCalculating download speed')
downSpeed = wifi.download()/1000/1000
print('Calculating upload speed\n')
upSpeed = wifi.upload()/1000/1000

print(f'Your download speed is {round(downSpeed*100)/100} Mbps')
print(f'Your upload speed is {round(upSpeed*100)/100} Mbps')