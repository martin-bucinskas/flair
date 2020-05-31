import os
import subprocess


def transcode_mime(file_format, config):
    return config['ffmpeg']['mimes'].get(file_format) or config['ffmpeg']['mimes']['*']


def transcode(path, start, file_format, vcodec, acodec, config):
    command = config['ffmpeg']['ffmpeg_command']
    args = config['ffmpeg']['ffmpeg_args']

    cmdline = command + args.format(str(start), path, file_format, vcodec, acodec)
    _fnull = open(os.devnull, 'w')

    process = subprocess.Popen(
        cmdline.split(),
        stdout=subprocess.PIPE,
        stderr=_fnull
    )

    try:
        f = process.stdout
        byte = f.read(65536)

        while byte:
            yield byte
            byte = f.read(65536)

    finally:
        process.kill()
        _fnull.close()
