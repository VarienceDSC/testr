import os
import glob
from flask import Flask, send_file
from pyngrok import ngrok

app = Flask(__name__)

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        internal_storage_path = '/storage/emulated/0/'
        return send_file(os.path.join(internal_storage_path, filename), as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    file_list = glob.glob('/storage/emulated/0/*')
    file_list2 = glob.glob('/storage/emulated/0/*/*')
    for file in file_list:
        print(file)
    for file2 in file_list2:
        print(file2)
    url = ngrok.connect(5000).public_url
    print(f' * Running on {url}')
    app.run(port=5000)
