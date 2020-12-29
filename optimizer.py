import os

path = os.getcwd() + (r"\engine\config\platform\pc")

filepath = os.path.join(path, 'User.ini')
f = open(filepath, "w")
print('''
      Which settings would you like to set?

        Press 1 for Max Boost (For maximum fps boost)
        Press 2 for Balanced (For Good Quality and FPS)
        Press 3 to delete the set config
      

''')

askInput = input(">")

if askInput == "1":
    f.write('''[Developer/FeatureToggles]
    Antialiasing = True
    Bloom = True
    CharacterLightBlockers = False
    CharacterRimEnhancement = False
    CharacterSubsurfaceScattering = True
    ChromaticAberration = True
    ConstrastAdaptiveSharpening = True
    ContactShadows = True
    DepthOfField = True
    DistantFog = False
    DistantGI = False
    DistantShadows = True
    DistantVolFog = False
    DynamicDecals = True
    FilmGrain = True
    GlobalIllumination = True
    Hair = True
    ImageBasedFlares = True
    LocalShadows = True
    MotionBlur = False
    RainMap = True
    RuntimeTangentUpdate = False
    ScreenSpaceHeatHaze = False
    ScreenSpacePlanarReflection = False
    ScreenSpaceRain = False
    ScreenSpaceReflection = False
    ScreenSpaceUnderwater = False
    SSAO = True
    VolumetricClouds = False
    VolumetricFog = False
    Weather = True
     
    [Rendering/AsyncCompute]
    BuildDepthChain = False
    DynamicTexture = False
    Enable = False
    FlattenNormals = False
    LutGeneration = False
    RaytraceASBuild = False
    SSAO = False
     
    [Rendering/FrostedGlass]
    GlassUseMipChain = True
     
    [Rendering]
    RainMapProxySorting = True
    UseExperimentalVolFog = False
    UseSkinningLOD = True
     
    [Rendering/Shadows]
    CascadeFitToWorstCase = True
    CascadeUseBackfacesAsCullingPlanes = True''')
    f.close()
    print("Done!")
    input(">")

elif askInput == "2":
    f.write('''[Developer/FeatureToggles]
    Antialiasing = True
    Bloom = True
    CharacterLightBlockers = True
    CharacterRimEnhancement = True
    CharacterSubsurfaceScattering = True
    ChromaticAberration = True
    ConstrastAdaptiveSharpening = True
    ContactShadows = True
    DepthOfField = True
    DistantFog = True
    DistantGI = True
    DistantShadows = True
    DistantVolFog = True
    DynamicDecals = True
    FilmGrain = True
    GlobalIllumination = True
    Hair = True
    ImageBasedFlares = True
    LocalShadows = True
    MotionBlur = False
    RainMap = True
    RuntimeTangentUpdate = True
    ScreenSpaceHeatHaze = True
    ScreenSpacePlanarReflection = True
    ScreenSpaceRain = True
    ScreenSpaceReflection = True
    ScreenSpaceUnderwater = True
    SSAO = True
    VolumetricClouds = True
    VolumetricFog = True
    Weather = True
     
    [Rendering/AsyncCompute]
    BuildDepthChain = False
    DynamicTexture = False
    Enable = False
    FlattenNormals = False
    LutGeneration = False
    RaytraceASBuild = False
    SSAO = False
     
    [Rendering/FrostedGlass]
    GlassUseMipChain = True
     
    [Rendering]
    RainMapProxySorting = True
    UseExperimentalVolFog = True
    UseSkinningLOD = True
     
    [Rendering/Shadows]
    CascadeFitToWorstCase = True
    CascadeUseBackfacesAsCullingPlanes = True''')
    f.close()
    print("Done!")
    input(">")

elif askInput == "3":
    os.remove(path + r"\User.ini")
    print("Done!")
    input(">")