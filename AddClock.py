from pathlib import Path
import os
#import ffmpeg
         
ffmpegCommand1 = '''ffmpeg -y -i '''   
ffmpegCommand2 = ''' -vf "drawtext=fontfile=/tmp/UbuntuMono-B.ttf:fontsize=36:fontcolor=yellow:box=1:boxcolor=black@0.4:text='\: %{pts\:hms}'" '''


pathlist = Path('.').glob('*.mp4')

for path in pathlist:
     path_in_str = str(path)
     name, ext = os.path.splitext(path_in_str)
     output = name + '_Clock' + ext

     os.system(ffmpegCommand1 + path_in_str + ffmpegCommand2 + output)
