import requests
import json
import os
import ffmpeg

def get_video_data(url, headers):
    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"An HTTP error occurred: {e}")
        return None

    data = response.text.split("window.__INITIAL_STATE__={")[1].split("};(function()")[0]
    data = json.loads("{" + data + "}")
    return data, session

def download_file(url, headers, output_path):
    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(output_path+"已下载完成")
    except requests.exceptions.HTTPError as e:
        print(f"An HTTP error occurred: {e}")

def merge_audio_video(video_path, audio_path, output_file):
    input_video = ffmpeg.input(video_path)
    input_audio = ffmpeg.input(audio_path)
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(output_file).run()

# 视频链接
url = "https://www.bilibili.com/video/BV1Po4y1W7Qv"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "Referer": "https://www.bilibili.com/"
}

# 获取视频数据和会话
video_data, session = get_video_data(url, headers)

if video_data is not None:
    # 获取视频标题和ID
    video_title = video_data["videoData"]["title"]
    bvid = video_data["bvid"]
    cid = video_data["videoData"]["cid"]

    # 获取音频和视频下载链接
    video_api_url = f"https://api.bilibili.com/x/player/playurl?fnval=80&cid={cid}&bvid={bvid}"
    response = session.get(video_api_url)
    data = json.loads(response.text)["data"]["dash"]
    audio_url = data["audio"][0]["baseUrl"]
    video_url = data["video"][0]["baseUrl"]

    # 创建文件夹（如果不存在）
    username = os.getlogin()
    desktop_path = os.path.join("C:\\Users", username, "Desktop")
    audio_base_path = desktop_path + "\\bilibili\\audio\\"
    video_base_path = desktop_path + "\\bilibili\\video\\"

    if not os.path.exists(audio_base_path):
        os.makedirs(audio_base_path)
    if not os.path.exists(video_base_path):
        os.makedirs(video_base_path)

    # 下载音频和视频文件
    audio_path = os.path.join(audio_base_path, video_title + ".m4a")
    video_path = os.path.join(video_base_path, video_title + ".mp4")

    download_file(audio_url, headers, audio_path)
    download_file(video_url, headers, video_path)

    # 合并音频和视频文件
    concat_path = desktop_path+ "\\bilibili\\concat\\"
    if not os.path.exists(concat_path):
        os.makedirs(concat_path)
    output_file = os.path.join(concat_path, video_title + ".mp4")
    merge_audio_video(video_path, audio_path, output_file)
    print("合并已完成...")