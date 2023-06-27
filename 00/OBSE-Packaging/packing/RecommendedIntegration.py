import VisualStudioAutomation as VS
import os

sRecommendedIntegrationFolder = "include/obse"
cRecommendedIntegrationFiles = ["StdAfx.cpp","StdAfx.h",
    "obse/GameActorValues.cpp","obse/GameActorValues.h","obse/GameAPI.cpp","obse/GameAPI.h",
    "obse/GameBSExtraData.cpp","obse/GameBSExtraData.h","obse/GameData.cpp","obse/GameData.h",
    "obse/GameExtraData.cpp","obse/GameExtraData.h","obse/GameForms.cpp","obse/GameForms.h",
    "obse/GameObjects.cpp","obse/GameObjects.h","obse/GameRTTI_1_1.inl","obse/GameRTTI_1_2.inl",
    "obse/GameRTTI_1_2_416.inl","obse/GameTasks.cpp","obse/GameTasks.h","obse/GameTypes.cpp","obse/GameTypes.h",
    "obse/NiAPI.cpp","obse/NiAPI.h","obse/NiNodes.cpp","obse/NiNodes.h","obse/NiRTTI.cpp","obse/NiRTTI.h",
    "obse/ParamInfos.h","obse/PluginAPI.h","obse/Script.cpp","obse/Script.h","obse/Utilities.cpp","obse/Utilities.h"]

def Do(sRoot,sProj,sSln):
    global sRecommendedIntegrationFolder
    global cRecommendedIntegrationFiles
    with VS.DTEWrapper() as vDTEWrapper:
        with vDTEWrapper.OpenSln(sSln):
            with vDTEWrapper.OpenProj(sProj) as vProjWrapper:
                for vItem in cRecommendedIntegrationFiles:
                    vProjWrapper.AddFile(os.path.join(sRoot,sRecommendedIntegrationFolder,vItem),"obse")
                with vDTEWrapper.OpenProj(os.path.join(sRoot,"include/common/common.vcxproj")) as vProjectWrapperToReference:
                    vProjWrapper.AddProjRef(vProjectWrapperToReference.vProj)

def Undo(sRoot,sProj,sSln):
    global sRecommendedIntegrationFolder
    global cRecommendedIntegrationFiles
    with VS.DTEWrapper() as vDTEWrapper:
        with vDTEWrapper.OpenSln(sSln) as vSlnWrapper:
            with vDTEWrapper.OpenProj(sProj) as vProjWrapper:
                for vItem in cRecommendedIntegrationFiles:
                    vProjWrapper.RemoveFile(os.path.join(sRoot,sRecommendedIntegrationFolder,vItem))
                with vDTEWrapper.OpenProj(os.path.join(sRoot,"include/common/common.vcxproj")) as vProjectWrapperToUnreference:
                    vProjWrapper.RemoveProjRef(vProjectWrapperToUnreference.vProj)
            vSlnWrapper.RemoveProj(os.path.join(sRoot,"include/common/common.vcxproj"))
