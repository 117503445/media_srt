from htutil import file
from pathlib import Path

from app import path
from moviepy.video.io.VideoFileClip import VideoFileClip

from pydub.silence import detect_nonsilent
from pydub import AudioSegment

from aip import AipSpeech


def extract_audio(media_path: Path):
    audio_file = path.dir_temp / 'source.wav'
    audio_file = str(audio_file.absolute())
    video = VideoFileClip(str(media_path.absolute()))
    video.audio.write_audiofile(audio_file, ffmpeg_params=[
                                '-ar', '16000', '-ac', '1'])


def split_audio():
    sound = AudioSegment.from_wav(path.dir_temp / 'source.wav')

    timestamp_list = detect_nonsilent(sound, 500, sound.dBFS*1.3, 1)
    print(timestamp_list)
    # for i in range(len(timestamp_list)):
    #     d = timestamp_list[i][1] - timestamp_list[i][0]
    #     print("Section is :", timestamp_list[i], "duration is:", d)
    #     print('dBFS: {0}, max_dBFS: {1}, duration: {2}, split: {3}'.format(round(
    #         sound.dBFS, 2), round(sound.max_dBFS, 2), sound.duration_seconds, len(timestamp_list)))


def process(media_path: path):
    # extract_audio(media_path)
    split_audio()


def main():
    files = path.dir_input.glob('*.mp4')
    for f in files:
        print(f)
        process(f)


if __name__ == '__main__':
    main()
