from pathlib import Path
import os
import cv2
         
ffmpegCommand1 = '''ffmpeg -y -i '''   
ffmpegCommand2 = ''' -vf "drawtext=timecode='00\:00\:00\:00':rate='''
ffmpegCommand3 = ''':fontsize=48:fontcolor=white:box=1:boxborderw=6:boxcolor=black@0.75:x=0:y=0" -c:a copy '''

pathlist = Path('.').glob('*.mp4')

for path in pathlist:
     path_in_str = str(path)
     name, ext = os.path.splitext(path_in_str)
     output = name + '_Clock' + ext
     cap=cv2.VideoCapture(path_in_str)
     fps = str(cap.get(cv2.CAP_PROP_FPS))
     os.system(ffmpegCommand1 + path_in_str + ffmpegCommand2 + fps + ffmpegCommand3 + output)
