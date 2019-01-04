from __future__ import print_function
import os
import platform


class Config(object):
    """docstring for Config"""

    def __init__(self):
        super(Config, self).__init__()

        DATAPATH = os.environ.get('DATAPATH')
        '''The default DATAPATH variable is DATAPATH=[path_to_DeepST]/data'''
        if DATAPATH is None:
            if platform.system() == "Windows" or platform.system() == "Linux":
                # DATAPATH = "D:/data/traffic_flow"
            # elif platform.system() == "Linux":
                DATAPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
                '''从当前文件夹转到data目录下'''
            else:
                print("Unsupported/Unknown OS: ", platform.system, "please set DATAPATH")
        self.DATAPATH = DATAPATH
