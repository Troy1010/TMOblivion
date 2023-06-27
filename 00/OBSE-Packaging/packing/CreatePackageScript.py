##region Settings
bPause = True
##endregion
from conans import ConanFile, MSBuild
import subprocess, os, errno, ctypes
import TM_CommonPy as TM
import VisualStudioAutomation as VS

##region DoubleclickEvent
if __name__ == "__main__":
    try:
        TM.Run("conan create . Troy1010/channel -pr conanprofile_OBSEPlugin")
    except Exception as e:
        print(e)
        os.system('pause')
        raise
    if bPause:
        print("\n\t\t\tDone\n")
        os.system('pause')
##endregion
