##region Settings
bPause = True
##endregion
from conans import ConanFile
import subprocess, os
import VisualStudioAutomation as VS

class OBSEPackaging_Conan(ConanFile):
    name = "OBSEPluginDevPackage"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/Troy1010/OBSE-Packaging"
    description = "Development sources for OBSE plugins."
    settings = "os", "compiler", "build_type", "arch"
    exports = "RecommendedIntegration.py"

    def source(self):
        try:
            os.makedirs('Oblivion-Script-Extender')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        os.chdir('Oblivion-Script-Extender')
        subprocess.call(['git', 'clone', 'https://github.com/llde/Oblivion-Script-Extender.git', '.', '--no-checkout'])
        subprocess.call(['git', 'checkout', '338206760744df35711bde343d7efe5367644d75'])
        os.chdir('..')

    def package(self):
        #---RecommendedIntegration
        self.copy("RecommendedIntegration.py")
        #---common
        VS.SetIncludeDir('Oblivion-Script-Extender/common/common.vcxproj',"$(ProjectDir);$(ProjectDir)\..;%(AdditionalIncludeDirectories)")
        self.copy('common.vcxproj',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.h',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.cpp',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.inl',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.inc',src='Oblivion-Script-Extender/common/',dst='include/common/')
        #---obse
        self.copy('*.h',src='Oblivion-Script-Extender/obse/',dst='include/obse/')
        self.copy('*.cpp',src='Oblivion-Script-Extender/obse/',dst='include/obse/')
        self.copy('*.inl',src='Oblivion-Script-Extender/obse/',dst='include/obse/')

    def package_info(self):
        self.cpp_info.includedirs = ['include','include/obse','include/common'] #'include/common' may not be necessary
