import subprocess
import sys
import os
import imageio_ffmpeg as ffmpeg

ffmpeg_path = ffmpeg.get_ffmpeg_exe()

def make_mono(input_file, output_file=None, channel="left"):
    """
    Duplicate one audio channel (left or right) to both outputs,
    while copying the video stream untouched.
    Uses imageio-ffmpeg to locate ffmpeg automatically.
    """
    if output_file is None:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_mono{ext}"

    if channel.lower() == "left":
        pan_filter = "pan=stereo|c0=FL|c1=FL"
    elif channel.lower() == "right":
        pan_filter = "pan=stereo|c0=FR|c1=FR"
    else:
        raise ValueError("channel must be 'left' or 'right'")

    cmd = [
        ffmpeg_path,
        "-y",                # overwrite output if exists
        "-i", input_file,
        "-c:v", "copy",      # don’t re-encode video
        "-c:a", "aac",       # re-encode audio only
        "-filter_complex", pan_filter,
        output_file
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    print(f"Done. Output saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python make_mono.py inputfile [left|right]")
        sys.exit(1)

    infile = sys.argv[1]
    channel = sys.argv[2] if len(sys.argv) > 2 else "left"
    make_mono(infile, channel=channel)
