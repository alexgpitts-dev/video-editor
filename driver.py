from make_mono import make_mono

path_to_file = r"C:\Users\alexg\Desktop\Processing\20210101_000647B.mp4"

if __name__ == "__main__":
    make_mono(input_file=path_to_file, channel='left')
