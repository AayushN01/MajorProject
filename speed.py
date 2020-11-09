from speedtest import Speedtest

st = Speedtest()
print("Download speed:", st.download())
print("Upload speed:", st.upload())
