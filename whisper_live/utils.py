import os
import textwrap
import sounddevice as sd
import scipy
import numpy as np
import av
from pathlib import Path
import logging
import sys

def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_transcript(text):
    """Prints formatted transcript text."""
    wrapper = textwrap.TextWrapper(width=60)
    for line in wrapper.wrap(text="".join(text)):
        print(line)


def format_time(s):
    """Convert seconds (float) to SRT time format."""
    hours = int(s // 3600)
    minutes = int((s % 3600) // 60)
    seconds = int(s % 60)
    milliseconds = int((s - int(s)) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def create_srt_file(segments, resampled_file):
    with open(resampled_file, 'w', encoding='utf-8') as srt_file:
        segment_number = 1
        for segment in segments:
            start_time = format_time(float(segment['start']))
            end_time = format_time(float(segment['end']))
            text = segment['text']

            srt_file.write(f"{segment_number}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{text}\n\n")

            segment_number += 1


def resample(file: str, sr: int = 16000):
    """
    Resample the audio file to 16kHz.

    Args:
        file (str): The audio file to open
        sr (int): The sample rate to resample the audio if necessary

    Returns:
        resampled_file (str): The resampled audio file
    """
    container = av.open(file)
    stream = next(s for s in container.streams if s.type == 'audio')

    resampler = av.AudioResampler(
        format='s16',
        layout='mono',
        rate=sr,
    )

    resampled_file = Path(file).stem + "_resampled.wav"
    output_container = av.open(resampled_file, mode='w')
    output_stream = output_container.add_stream('pcm_s16le', rate=sr)
    output_stream.layout = 'mono'

    for frame in container.decode(audio=0):
        frame.pts = None
        resampled_frames = resampler.resample(frame)
        if resampled_frames is not None:
            for resampled_frame in resampled_frames:
                for packet in output_stream.encode(resampled_frame):
                    output_container.mux(packet)

    for packet in output_stream.encode(None):
        output_container.mux(packet)

    output_container.close()
    return resampled_file




def confirm_device_index_acceptable_as_microphone (proposed_index:int = 1) -> int:
    """
    make sure that the device index is acceptable.
    """
    s = sd.query_devices()
    all_indices = list(map(lambda x: x["index"], s))
    try_to_correct = False
    if proposed_index not in all_indices:
        logging.error("proposed device index is not among the available options")
        try_to_correct = True
    while try_to_correct:
        try:
            with sd.InputStream(device=proposed_index):
                try_to_correct = False
                pass
        except Exception as e:
            logging.error("problem with proposed device index: {e}")
            try_to_correct = True

        if try_to_correct:
            print("your chosen input device was unusable.  Here are the available options.  Choose an index to continue, 'q' to exit the program.")
            for d in s:
                print(d)
            index = input("prompt")
            if index.strip()=='q':
                sys.exit()
            try:
                sdi = int(index)
            except ValueError:
                print("invalid index -- only integers are allowable")
                sys.exit()
            proposed_index = sdi
    return proposed_index



def confirm_host_is_desirable (server_url:str|None) -> str:
    """
    make sure that the device index is acceptable.
    """
    if server_url is not None:
        proposed_host = server_url
    elif 'TRANSCRIPTION_SERVER' in os.environ:
        proposed_host = os.environ['TRANSCRIPTION_SERVER']
    else:
        print("You must choose a server to perform transcriptions.  You can do it on the command line with --server, or you can set the environment variable TRANSCRIPTION_SERVER.")
        sys.exit()
    return proposed_host
