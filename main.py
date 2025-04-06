import os
import yt_dlp
from flask import Flask, send_file, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/download')

def download():
    url = request.args.get('url')
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audios/%(id)s.%(ext)s',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }
    output_dir = 'audios'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            name= info['id']
            file_path = f"audios/{name}.mp3"
            return send_file(
    file_path,
    as_attachment=True,
    download_name=f"{name}.mp3",
    mimetype='audio/mpeg'
), os.remove(f"audios/{name}.mp3")
@app.route('/search')
def search():
    url = request.args.get('url')
    ydl_opts= {
        'quiet': True,
        'skip_download': True
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download= False)
        data =  {'titulo': info.get('title'),
                 'duration': info.get('duratton'),
                 'channel': info.get('uploader'),
                 'thumbnail': info.get('thumbnail'),}
        return jsonify(data)
app.run()
