# -*- coding: mbcs -*-
# Created by makepy.py version 0.4.95
# By python version 2.5.1 (r251:54863, May  1 2007, 17:47:05) [MSC v.1310 32 bit (Intel)]
# From type library 'TypeLibrary.tlb'
# On Sat Oct 15 13:19:15 2011
"""Adobe Photoshop CS5 Type Library"""
makepy_version = '0.4.95'
python_version = 0x20501f0

import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{4B0AB3E1-80F1-11CF-86B4-444553540000}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x409

class constants:
	phClassAction                 =0x4163746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassActionSet              =0x41536574 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassAdjustment             =0x41646a73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassAdjustmentLayer        =0x41646a4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassAirbrushTool           =0x4162546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassAlphaChannelOptions    =0x4143686c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassAntiAliasedPICTAcquire =0x416e7441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassApplication            =0x63617070 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassArrowhead              =0x63417277 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassArtHistoryBrushTool    =0x4142546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassAssert                 =0x41737274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassAssumedProfile         =0x41737350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBMPFormat              =0x424d5046 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBackLight              =0x42616b4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBackgroundEraserTool   =0x5345546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBackgroundLayer        =0x42636b4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBevelEmboss            =0x6562626c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBitmapMode             =0x42746d4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBlendRange             =0x426c6e64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBlurTool               =0x426c546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBookColor              =0x426b436c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBrightnessContrast     =0x42726743 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBrush                  =0x42727368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassBurnInTool             =0x4272546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCMYKColor              =0x434d5943 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCMYKColorMode          =0x434d594d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCMYKSetup              =0x434d5953 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCachePrefs             =0x43636850 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCalculation            =0x436c636c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassChannel                =0x43686e6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassChannelMatrix          =0x43684d78 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassChannelMixer           =0x43686e4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassChromeFX               =0x43684658 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassClippingInfo           =0x436c706f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassClippingPath           =0x436c7050 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCloneStampTool         =0x436c546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassColor                  =0x436c7220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassColorBalance           =0x436c7242 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassColorCast              =0x436f6c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassColorCorrection        =0x436c7243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassColorPickerPrefs       =0x436c726b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassColorSampler           =0x436c536d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassColorStop              =0x436c7274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCommand                =0x436d6e64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassContour                =0x46785363 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCurvePoint             =0x43725074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCurves                 =0x43727673 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCurvesAdjustment       =0x43727641 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCustomPalette          =0x4373746c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCustomPhosphors        =0x43737450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassCustomWhitePoint       =0x43737457 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassDisplayPrefs           =0x44737050 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassDocument               =0x44636d6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassDodgeTool              =0x4464546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassDropShadow             =0x44725368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassDuotoneInk             =0x44746e49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassDuotoneMode            =0x44746e4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassEPSGenericFormat       =0x45505347 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassEPSPICTPreview         =0x45505343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassEPSTIFFPreview         =0x45505354 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassElement                =0x456c6d6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassEllipse                =0x456c7073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassEraserTool             =0x4572546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassExport                 =0x45787072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassFileInfo               =0x466c496e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassFileSavePrefs          =0x466c5376 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassFillFlash              =0x46696c46 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassFlashPixFormat         =0x466c7350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassFontDesignAxes         =0x466e7444 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassFormat                 =0x466d7420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassFrameFX                =0x46724658 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGIF89aExport           =0x47463839 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGIFFormat              =0x47464672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGeneralPrefs           =0x476e7250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGlobalAngle            =0x67626c41 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGradient               =0x4772646e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGradientFill           =0x47726466 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGradientMap            =0x47644d70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGradientTool           =0x4772546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGraySetup              =0x47725374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGrayscale              =0x47727363 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGrayscaleMode          =0x47727973 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGuide                  =0x47642020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassGuidesPrefs            =0x47645072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHSBColor               =0x48534243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHSBColorMode           =0x4853424d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHalftoneScreen         =0x486c6653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHalftoneSpec           =0x486c6670 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHistoryBrushTool       =0x4842546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHistoryPrefs           =0x43487350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHistoryState           =0x48737453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHueSatAdjustment       =0x48537441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHueSatAdjustmentV2     =0x48737432 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassHueSaturation          =0x48537472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassIFFFormat              =0x49464646 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassIllustratorPathsExport =0x496c7350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassImagePoint             =0x496d6750 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassImport                 =0x496d7072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassIndexedColorMode       =0x496e6443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassInkTransfer            =0x496e6b54 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassInnerGlow              =0x4972476c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassInnerShadow            =0x49725368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassInterfaceColor         =0x49436c72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassInvert                 =0x496e7672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassJPEGFormat             =0x4a504547 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLabColor               =0x4c62436c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLabColorMode           =0x4c62434d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLayer                  =0x4c797220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLayerEffects           =0x4c656678 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLayerFXVisible         =0x6c667876 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLevels                 =0x4c766c73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLevelsAdjustment       =0x4c766c41 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLightSource            =0x4c676853 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassLine                   =0x4c6e2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassMacPaintFormat         =0x4d63506e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassMagicEraserTool        =0x4d674572 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassMagicPoint             =0x4d676370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassMask                   =0x4d736b20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassMenuItem               =0x4d6e2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassMode                   =0x4d642020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassMultichannelMode       =0x4d6c7443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassNull                   =0x6e756c6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassObsoleteTextLayer      =0x54784c79 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassOffset                 =0x4f667374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassOpacity                =0x4f706163 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassOuterGlow              =0x4f72476c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPDFGenericFormat       =0x50444647 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPICTFileFormat         =0x50494346 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPICTResourceFormat     =0x50494352 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPNGFormat              =0x504e4746 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPageSetup              =0x50675374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPaintbrushTool         =0x5062546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPath                   =0x50617468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPathComponent          =0x5061436d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPathPoint              =0x50746870 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPattern                =0x50747452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPatternStampTool       =0x5061546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPencilTool             =0x5063546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPhotoshop20Format      =0x50687432 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPhotoshop35Format      =0x50687433 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPhotoshopDCS2Format    =0x50684432 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPhotoshopDCSFormat     =0x50684431 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPhotoshopEPSFormat     =0x50687445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPhotoshopPDFFormat     =0x50687450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPixel                  =0x5078656c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPixelPaintFormat       =0x50786c50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPluginPrefs            =0x506c6750 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPoint                  =0x506e7420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPoint16                =0x506e7431 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPolygon                =0x506c676e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPosterize              =0x50737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassPreferences            =0x476e7250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassProfileSetup           =0x50726653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassProperty               =0x50727072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassRGBColor               =0x52474243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassRGBColorMode           =0x5247424d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassRGBSetup               =0x52474274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassRange                  =0x52616e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassRawFormat              =0x52772020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassRect16                 =0x52637431 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassRectangle              =0x5263746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSaturationTool         =0x5372546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassScitexCTFormat         =0x53637478 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSelection              =0x6373656c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSelectiveColor         =0x536c6343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassShapingCurve           =0x53687043 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSharpenTool            =0x5368546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSingleColumn           =0x536e6763 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSingleRow              =0x536e6772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSmudgeTool             =0x536d546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSnapshot               =0x536e7053 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSolidFill              =0x536f4669 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSpotColorChannel       =0x53436368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassStyle                  =0x53747943 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassSubPath                =0x5362706c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTIFFFormat             =0x54494646 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTargaFormat            =0x54726746 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTextLayer              =0x54784c72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTextStyle              =0x54787453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTextStyleRange         =0x54787474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassThreshold              =0x54687273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTool                   =0x546f6f6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTransferPoint          =0x44746e50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTransferSpec           =0x54726670 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTransparencyPrefs      =0x54726e50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassTransparencyStop       =0x54726e53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassUnitsPrefs             =0x556e7450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassUnspecifiedColor       =0x556e7343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassVersion                =0x5672736e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassWebdavPrefs            =0x57646276 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phClassXYYColor               =0x58595943 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phDialogDisplay               =0x1        # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phDialogDontDisplay           =0x0        # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phDialogSilent                =0x2        # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum16BitsPerPixel          =0x31364274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum1BitPerPixel            =0x4f6e4274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum2BitsPerPixel           =0x32427473 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum32BitsPerPixel          =0x33324274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum4BitsPerPixel           =0x34427473 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum5000                    =0x35303030 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum5500                    =0x35353030 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum6500                    =0x36353030 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum72Color                 =0x3732436c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum72Gray                  =0x37324772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum7500                    =0x37353030 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum8BitsPerPixel           =0x45676842 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnum9300                    =0x39333030 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumA                       =0x41202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumADSBottoms              =0x41644274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumADSCentersH             =0x41644348 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumADSCentersV             =0x41644356 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumADSHorizontal           =0x41644872 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumADSLefts                =0x41644c66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumADSRights               =0x41645267 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumADSTops                 =0x41645470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumADSVertical             =0x41645672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumASCII                   =0x41534349 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAboutApp                =0x41624170 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAbsColorimetric         =0x41436c72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAbsolute                =0x4162736c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumActualPixels            =0x41637450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAdaptive                =0x41647074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAdd                     =0x41646420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAdjustmentOptions       =0x41646a4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAdobeRGB1998            =0x534d5054 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAirbrushEraser          =0x41726273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAll                     =0x416c2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAmiga                   =0x416d6761 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAmountHigh              =0x616d4869 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAmountLow               =0x616d4c6f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAmountMedium            =0x616d4d64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAngle                   =0x416e676c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAntiAliasCrisp          =0x416e4372 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAntiAliasHigh           =0x416e4869 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAntiAliasLow            =0x416e4c6f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAntiAliasMedium         =0x416e4d64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAntiAliasNone           =0x416e6e6f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAntiAliasSmooth         =0x416e536d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAntiAliasStrong         =0x416e5374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAny                     =0x416e7920 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAppleRGB                =0x41707052 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumApplyImage              =0x41706c49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAroundCenter            =0x41726e43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumArrange                 =0x41726e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAsk                     =0x41736b20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumAskWhenOpening          =0x41736b57 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumB                       =0x42202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBack                    =0x4261636b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBackground              =0x42636b67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBackgroundColor         =0x42636b43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBackward                =0x42636b77 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBehind                  =0x42686e64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBest                    =0x42737420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBetter                  =0x44746862 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBicubic                 =0x42636263 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBilinear                =0x426c6e72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBinary                  =0x426e7279 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepth1               =0x42443120 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepth16              =0x42443136 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepth24              =0x42443234 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepth32              =0x42443332 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepth4               =0x42443420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepth8               =0x42443820 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepthA1R5G5B5        =0x31353635 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepthA4R4G4B4        =0x34343434 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepthR5G6B5          =0x78353635 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepthX4R4G4B4        =0x78343434 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitDepthX8R8G8B8        =0x78383838 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBitmap                  =0x42746d70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlack                   =0x426c636b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlackAndWhite           =0x42616e57 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlackBody               =0x426c6342 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlacks                  =0x426c6b73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlast                   =0x426c7374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlockEraser             =0x426c6b20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlocks                  =0x426c6b73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlue                    =0x426c2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBlues                   =0x426c7320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBottom                  =0x4274746d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushDarkRough          =0x42724452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushLightRough         =0x4272734c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushSimple             =0x4272536d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushSize               =0x42727353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushSparkle            =0x42725370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushWideBlurry         =0x42726257 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushWideSharp          =0x42727357 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushesAppend           =0x42727341 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushesDefine           =0x42727344 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushesDelete           =0x42727366 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushesLoad             =0x42727364 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushesNew              =0x4272734e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushesOptions          =0x4272734f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushesReset            =0x42727352 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBrushesSave             =0x42727376 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBuiltin                 =0x426c746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBurnInH                 =0x42726e48 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBurnInM                 =0x42726e4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumBurnInS                 =0x42726e53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumButtonMode              =0x42746e4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCIERGB                  =0x43524742 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCMYK                    =0x434d594b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCMYK64                  =0x434d5346 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCMYKColor               =0x45434d59 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCalculations            =0x436c636c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCascade                 =0x43736364 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCenter                  =0x436e7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCenterGlow              =0x53726343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCenteredFrame           =0x43747246 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumChannelOptions          =0x43686e4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumChannelsPaletteOptions  =0x43686e50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCheckerboardLarge       =0x4368634c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCheckerboardMedium      =0x4368634d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCheckerboardNone        =0x4368634e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCheckerboardSmall       =0x43686353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumClear                   =0x436c6172 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumClearGuides             =0x436c7247 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumClipboard               =0x436c7062 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumClippingPath            =0x436c7050 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCloseAll                =0x436c7341 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCoarseDots              =0x43727344 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumColor                   =0x436c7220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumColorBurn               =0x4342726e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumColorDodge              =0x43446467 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumColorMatch              =0x436c4d74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumColorNoise              =0x436c4e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumColorimetric            =0x436c726d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumComposite               =0x436d7073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumContourCustom           =0x73703036 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumContourDouble           =0x73703034 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumContourGaussian         =0x73703032 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumContourLinear           =0x73703031 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumContourSingle           =0x73703033 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumContourTriple           =0x73703035 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumConvertToCMYK           =0x436e7643 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumConvertToGray           =0x436e7647 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumConvertToLab            =0x436e764c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumConvertToRGB            =0x436e7652 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCreateDuplicate         =0x43727444 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCreateInterpolation     =0x43727449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCross                   =0x43727320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCurrentLayer            =0x4372724c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCustom                  =0x43737420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCustomPattern           =0x4373746d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCustomStops             =0x43737453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCyan                    =0x43796e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumCyans                   =0x43796e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDark                    =0x44726b20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDarken                  =0x44726b6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDarkenOnly              =0x44726b4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDashedLines             =0x4473684c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDesaturate              =0x44737474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDiamond                 =0x446d6e64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDifference              =0x4466726e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDiffusion               =0x4466736e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDiffusionDither         =0x44666e44 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDisplayCursorsPreferences=0x44737043 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDissolve                =0x44736c76 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDistort                 =0x44737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDodgeH                  =0x44646748 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDodgeM                  =0x4464674d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDodgeS                  =0x44646753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDots                    =0x44747320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDraft                   =0x44726674 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumDuotone                 =0x44746e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumEBUITU                  =0x45425420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumEdgeGlow                =0x53726345 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumEliminateEvenFields     =0x456c6d45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumEliminateOddFields      =0x456c6d4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumEllipse                 =0x456c7073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumEmboss                  =0x456d6273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumExact                   =0x45786374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumExclusion               =0x58636c75 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFPXCompressLossyJPEG    =0x46784a50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFPXCompressNone         =0x46784e6f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFaster                  =0x44746866 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFile                    =0x466c6520 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFileInfo                =0x466c496e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFillBack                =0x466c4263 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFillFore                =0x466c4672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFillInverse             =0x466c496e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFillSame                =0x466c536d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFineDots                =0x466e4474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFirst                   =0x46727374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFirstIdle               =0x46724964 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFitOnScreen             =0x46744f6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumForegroundColor         =0x46726743 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumForward                 =0x46727772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFreeTransform           =0x46725472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFront                   =0x46726e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFullDocument            =0x466c6c44 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumFullSize                =0x466c537a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFColorFileColorTable  =0x47464354 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFColorFileColors      =0x47464346 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFColorFileMicrosoftPalette=0x47464d53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFPaletteAdaptive      =0x47465041 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFPaletteExact         =0x47465045 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFPaletteOther         =0x4746504f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFPaletteSystem        =0x47465053 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFRequiredColorSpaceIndexed=0x47464349 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFRequiredColorSpaceRGB=0x47465247 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFRowOrderInterlaced   =0x4746494e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGIFRowOrderNormal       =0x47464e49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGaussianDistribution    =0x47736e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGeneralPreferences      =0x476e7250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGood                    =0x47642020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGradientFill            =0x4772466c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainClumped            =0x47726e43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainContrasty          =0x4772436e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainEnlarged           =0x47726e45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainHorizontal         =0x47726e48 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainRegular            =0x47726e52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainSoft               =0x47725366 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainSpeckle            =0x47725370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainSprinkles          =0x47725372 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainStippled           =0x47725374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainVertical           =0x47726e56 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrainyDots              =0x47726e44 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGraphics                =0x47727020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGray                    =0x47727920 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGray16                  =0x47727958 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGray18                  =0x47723138 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGray22                  =0x47723232 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGray50                  =0x47723530 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrayScale               =0x47727963 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGrayscales              =0x47727973 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGreen                   =0x47726e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGreens                  =0x47726e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumGuidesGridPreferences   =0x47756447 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHDTV                    =0x48445456 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHSBColor                =0x4853426c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHSLColor                =0x48534c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHalftoneFile            =0x486c6646 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHalftoneScreen          =0x486c6653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHardLight               =0x4872644c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHeavy                   =0x48767920 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHideAll                 =0x4864416c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHideSelection           =0x4864536c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHigh                    =0x48696768 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHighQuality             =0x48676820 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHighlights              =0x4867686c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHistogram               =0x48737467 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHistory                 =0x48737479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHistoryPaletteOptions   =0x4873744f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHistoryPreferences      =0x48737450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHorizontal              =0x48727a6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHorizontalOnly          =0x48727a4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumHue                     =0x48202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumIBMPC                   =0x49424d50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumICC                     =0x49434320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumIcon                    =0x49636e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumIdleVM                  =0x4964564d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumIgnore                  =0x49676e72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumImage                   =0x496d6720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumImageCachePreferences   =0x496d6750 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumIndexedColor            =0x496e646c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumInfoPaletteOptions      =0x496e6650 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumInfoPaletteToggleSamplers=0x496e6654 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumInnerBevel              =0x496e7242 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumInsetFrame              =0x496e7346 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumInside                  =0x496e7364 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumJPEG                    =0x4a504547 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumJustifyAll              =0x4a737441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumJustifyFull             =0x4a737446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumKeepProfile             =0x4b50726f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumKeyboardPreferences     =0x4b796250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLab                     =0x4c616220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLab48                   =0x4c624346 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLabColor                =0x4c62436c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLarge                   =0x4c726720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLast                    =0x4c737420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLastFilter              =0x4c737446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLayerOptions            =0x4c79724f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLayersPaletteOptions    =0x4c797250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLeft                    =0x4c656674 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLeft_PLUGIN             =0x4c667420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLevelBased              =0x4c766c42 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLight                   =0x4c677420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightBlue               =0x4c677442 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirBottom          =0x4c444274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirBottomLeft      =0x4c44424c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirBottomRight     =0x4c444252 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirLeft            =0x4c444c66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirRight           =0x4c445267 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirTop             =0x4c445470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirTopLeft         =0x4c44544c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirTopRight        =0x4c445452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightDirectional        =0x4c676844 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightGray               =0x4c677447 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightOmni               =0x4c67684f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightPosBottom          =0x4c504274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightPosBottomLeft      =0x4c50424c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightPosBottomRight     =0x4c504272 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightPosLeft            =0x4c504c66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightPosRight           =0x4c505267 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightPosTop             =0x4c505470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightPosTopLeft         =0x4c50544c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightPosTopRight        =0x4c505452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightRed                =0x4c677452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightSpot               =0x4c676853 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLighten                 =0x4c67686e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightenOnly             =0x4c67684f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLightness               =0x4c676874 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLine                    =0x4c6e2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLinear                  =0x4c6e7220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLines                   =0x4c6e7320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLinked                  =0x4c6e6b64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLongLines               =0x4c6e674c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLongStrokes             =0x4c6e6753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLow                     =0x4c6f7720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLowQuality              =0x4c772020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLower                   =0x4c777220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumLuminosity              =0x4c6d6e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMacThumbnail            =0x4d635468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMacintosh               =0x4d636e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMacintoshSystem         =0x4d636e53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMagenta                 =0x4d676e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMagentas                =0x4d676e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMask                    =0x4d736b20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMaskedAreas             =0x4d736b41 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMasterAdaptive          =0x4d416470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMasterPerceptual        =0x4d506572 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMasterSelective         =0x4d53656c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMaximum                 =0x4d786d6d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMaximumQuality          =0x4d786d20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMaya                    =0x4d617961 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMedium                  =0x4d64696d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMediumBlue              =0x4d646d42 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMediumDots              =0x4d646d44 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMediumLines             =0x4d646d4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMediumQuality           =0x4d646d20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMediumStrokes           =0x4d646d53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMemoryPreferences       =0x4d6d7250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMergeChannels           =0x4d726743 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMerged                  =0x4d726764 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMergedLayers            =0x4d72674c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMiddle                  =0x4d64646c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMidtones                =0x4d64746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumModeGray                =0x4d644772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumModeRGB                 =0x4d645247 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMonitor                 =0x4d6f6e69 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMonitorSetup            =0x4d6e7453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMonotone                =0x4d6e746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMulti72Color            =0x3732434d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMulti72Gray             =0x3732474d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMultiNoCompositePS      =0x4e436d4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMultichannel            =0x4d6c7468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumMultiply                =0x4d6c7470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNTSC                    =0x4e545343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNavigatorPaletteOptions =0x4e766750 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNearestNeighbor         =0x4e727374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNetscapeGray            =0x4e734772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNeutrals                =0x4e74726c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNewView                 =0x4e775677 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNext                    =0x4e787420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNikon                   =0x4e6b6e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNikon105                =0x4e6b6e31 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNo                      =0x4e202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNoCompositePS           =0x4e436d70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNone                    =0x4e6f6e65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNormal                  =0x4e726d6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNormalPath              =0x4e726d50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumNull                    =0x6e756c6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOS2                     =0x4f533220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOff                     =0x4f666620 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOn                      =0x4f6e2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOpenAs                  =0x4f704173 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOrange                  =0x4f726e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOutFromCenter           =0x4f744672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOutOfGamut              =0x4f744f66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOuterBevel              =0x4f747242 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOutsetFrame             =0x4f757446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOutside                 =0x4f747364 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumOverlay                 =0x4f76726c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumP22EBU                  =0x50323242 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPNGFilterAdaptive       =0x50474164 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPNGFilterAverage        =0x50474176 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPNGFilterNone           =0x50474e6f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPNGFilterPaeth          =0x50475074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPNGFilterSub            =0x50475362 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPNGFilterUp             =0x50475570 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPNGInterlaceAdam7       =0x50474941 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPNGInterlaceNone        =0x5047494e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPagePosCentered         =0x50675043 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPagePosTopLeft          =0x5067544c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPageSetup               =0x50675374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPaintbrushEraser        =0x506e7462 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPalSecam                =0x506c5363 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPanaVision              =0x506e5673 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPathsPaletteOptions     =0x50746850 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPattern                 =0x5074726e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPatternDither           =0x50746e44 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPencilEraser            =0x506e636c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPerceptual              =0x50657263 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPerspective             =0x50727370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPhotoshopPicker         =0x5068746b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPickCMYK                =0x50636b43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPickGray                =0x50636b47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPickHSB                 =0x50636b48 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPickLab                 =0x50636b4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPickOptions             =0x50636b4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPickRGB                 =0x50636b52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPillowEmboss            =0x506c4562 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPixelPaintSize1         =0x50785331 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPixelPaintSize2         =0x50785332 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPixelPaintSize3         =0x50785333 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPixelPaintSize4         =0x50785334 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPlace                   =0x506c6365 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPlaybackOptions         =0x50626b4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPluginPicker            =0x506c6750 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPluginsScratchDiskPreferences=0x506c6753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPolarToRect             =0x506c7252 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPondRipples             =0x506e6452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPrecise                 =0x50726320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPreciseMatte            =0x5072424c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPreviewBlack            =0x50727642 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPreviewCMY              =0x5072764e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPreviewCMYK             =0x50727643 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPreviewCyan             =0x50727679 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPreviewMagenta          =0x5072764d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPreviewOff              =0x5072764f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPreviewYellow           =0x50727659 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPrevious                =0x50727673 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPrimaries               =0x5072696d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPrintSize               =0x50726e53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPrintingInksSetup       =0x50726e49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPurple                  =0x50727020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumPyramids                =0x5079726d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSAverage              =0x51637361 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSCorner0              =0x51637330 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSCorner1              =0x51637331 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSCorner2              =0x51637332 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSCorner3              =0x51637333 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSIndependent          =0x51637369 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSSide0                =0x51637334 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSSide1                =0x51637335 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSSide2                =0x51637336 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQCSSide3                =0x51637337 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQuadtone                =0x5164746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQueryAlways             =0x51757241 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQueryAsk                =0x5175726c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumQueryNever              =0x5175724e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRGB                     =0x52474220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRGB48                   =0x52474246 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRGBColor                =0x52474243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRadial                  =0x52646c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRandom                  =0x526e646d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRectToPolar             =0x52637450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRed                     =0x52642020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRedrawComplete          =0x5264436d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumReds                    =0x52647320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumReflected               =0x52666c63 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRelative                =0x526c7476 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRepeat                  =0x52707420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRepeatEdgePixels        =0x52707445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRevealAll               =0x52766c41 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRevealSelection         =0x52766c53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRevert                  =0x52767274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRight                   =0x52676874 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRotate                  =0x52747465 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRotoscopingPreferences  =0x52747350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRound                   =0x526e6420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRulerCm                 =0x5272436d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRulerInches             =0x5272496e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRulerPercent            =0x52725072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRulerPicas              =0x52725069 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRulerPixels             =0x52725078 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumRulerPoints             =0x52725074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSMPTEC                  =0x534d5043 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSRGB                    =0x53524742 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSample3x3               =0x536d7033 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSample5x5               =0x536d7035 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSamplePoint             =0x536d7050 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSaturate                =0x53747220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSaturation              =0x53747274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSaveForWeb              =0x53766677 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSaved                   =0x53766564 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSavingFilesPreferences  =0x53766e46 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumScale                   =0x53636c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumScreen                  =0x5363726e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumScreenCircle            =0x53637243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumScreenDot               =0x53637244 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumScreenLine              =0x5363724c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSelectedAreas           =0x536c6341 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSelection               =0x536c6374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSelective               =0x53656c65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSeparationSetup         =0x53707253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSeparationTables        =0x53707254 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumShadows                 =0x53686477 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumShortLines              =0x5368724c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumShortStrokes            =0x53685374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSingle72Color           =0x37324353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSingle72Gray            =0x37324753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSingleNoCompositePS     =0x4e436d53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSkew                    =0x536b6577 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSlopeLimitMatte         =0x536c6d74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSmall                   =0x536d6c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSmartBlurModeEdgeOnly   =0x53424d45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSmartBlurModeNormal     =0x53424d4e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSmartBlurModeOverlayEdge=0x53424d4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSmartBlurQualityHigh    =0x53425148 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSmartBlurQualityLow     =0x5342514c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSmartBlurQualityMedium  =0x5342514d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSnapshot                =0x536e7073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSoftLight               =0x5366744c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSoftMatte               =0x5366424c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSolidColor              =0x53436c72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSpectrum                =0x53706374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSpin                    =0x53706e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSpotColor               =0x53706f74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSquare                  =0x53717220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStagger                 =0x53746772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStampIn                 =0x496e2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStampOut                =0x4f757420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStandard                =0x53746420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStdA                    =0x53746441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStdB                    =0x53746442 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStdC                    =0x53746443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStdE                    =0x53746445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStretchToFit            =0x53747246 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStrokeDirHorizontal     =0x5344487a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStrokeDirLeftDiag       =0x53444c44 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStrokeDirRightDiag      =0x53445244 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStrokeDirVertical       =0x53445674 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStylesAppend            =0x536c7341 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStylesDelete            =0x536c7366 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStylesLoad              =0x536c7364 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStylesNew               =0x536c734e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStylesReset             =0x536c7352 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumStylesSave              =0x536c7376 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSubtract                =0x53627472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSwatchesAppend          =0x53777441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSwatchesReplace         =0x53777470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSwatchesReset           =0x53777452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSwatchesSave            =0x53777453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumSystemPicker            =0x53797350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTIFF                    =0x54494646 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTables                  =0x54626c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTarget                  =0x54726774 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTargetPath              =0x54726770 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTexTypeBlocks           =0x5478426c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTexTypeBrick            =0x54784272 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTexTypeBurlap           =0x54784275 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTexTypeCanvas           =0x54784361 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTexTypeFrosted          =0x54784672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTexTypeSandstone        =0x54785374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTexTypeTinyLens         =0x5478544c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumThreshold               =0x54687268 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumThumbnail               =0x54686d62 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTile                    =0x54696c65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTile_PLUGIN             =0x546c2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleActionsPalette    =0x54676c41 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleBlackPreview      =0x54674250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleBrushesPalette    =0x54676c42 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleCMYKPreview       =0x54676c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleCMYPreview        =0x5467434d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleChannelsPalette   =0x54676c68 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleColorPalette      =0x54676c63 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleCyanPreview       =0x54674350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleEdges             =0x54676c45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleGamutWarning      =0x54676c47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleGrid              =0x54674772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleGuides            =0x54676c64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleHistoryPalette    =0x54676c48 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleInfoPalette       =0x54676c49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleLayerMask         =0x54676c4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleLayersPalette     =0x54676c79 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleLockGuides        =0x54676c4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleMagentaPreview    =0x54674d50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleNavigatorPalette  =0x54676c4e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleOptionsPalette    =0x54676c4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTogglePaths             =0x54676c50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTogglePathsPalette      =0x54676c74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleRGBMacPreview     =0x54724d70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleRGBUncompensatedPreview=0x54725570 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleRGBWindowsPreview =0x54725770 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleRulers            =0x54676c52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleSnapToGrid        =0x5467536e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleSnapToGuides      =0x54676c53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleStatusBar         =0x54676c73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleStylesPalette     =0x5467536c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleSwatchesPalette   =0x54676c77 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleToolsPalette      =0x54676c54 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumToggleYellowPreview     =0x54675950 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTop                     =0x546f7020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTransparency            =0x54727370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTransparencyGamutPreferences=0x54726e47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTransparent             =0x54726e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTrinitron               =0x54726e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumTritone                 =0x5472746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUIBitmap                =0x5542746d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUICMYK                  =0x55434d59 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUIDuotone               =0x5544746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUIGrayscale             =0x55477279 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUIIndexed               =0x55496e64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUILab                   =0x554c6162 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUIMultichannel          =0x554d6c74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUIRGB                   =0x55524742 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUndo                    =0x556e6420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUniform                 =0x556e666d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUniformDistribution     =0x556e6672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUnitsRulersPreferences  =0x556e7452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUpper                   =0x55707220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumUserStop                =0x55737253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumVMPreferences           =0x564d5072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumVertical                =0x56727463 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumVerticalOnly            =0x5672744f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumViolet                  =0x566c7420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWaveSine                =0x5776536e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWaveSquare              =0x57765371 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWaveTriangle            =0x57765472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWeb                     =0x57656220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWhite                   =0x57687420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWhites                  =0x57687473 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWideGamutRGB            =0x57524742 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWidePhosphors           =0x57696465 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWinThumbnail            =0x576e5468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWind                    =0x576e6420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWindows                 =0x57696e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWindowsSystem           =0x576e6453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWorkPath                =0x57726b50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWrap                    =0x57727020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumWrapAround              =0x57727041 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumYellow                  =0x596c6c77 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumYellowColor             =0x596c7720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumYellows                 =0x596c7773 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumYes                     =0x59732020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumZip                     =0x5a70456e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumZoom                    =0x5a6d2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumZoomIn                  =0x5a6d496e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEnumZoomOut                 =0x5a6d4f74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEvent3DTransform            =0x54645420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventAccentedEdges          =0x41636345 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventAdd                    =0x41646420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventAddNoise               =0x41644e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventAddTo                  =0x41646454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventAlign                  =0x416c676e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventAll                    =0x416c6c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventAngledStrokes          =0x416e6753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventApplyImage             =0x41707049 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventApplyStyle             =0x41537479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventAssert                 =0x41737274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventBackLight              =0x4261634c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventBasRelief              =0x4273526c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventBatch                  =0x42746368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventBatchFromDroplet       =0x42746346 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventBlur                   =0x426c7220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventBlurMore               =0x426c724d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventBorder                 =0x42726472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventBrightness             =0x42726743 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCanvasSize             =0x436e7653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventChalkCharcoal          =0x43686c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventChannelMixer           =0x43686e4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCharcoal               =0x43687263 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventChrome                 =0x4368726d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventClear                  =0x436c6572 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventClose                  =0x436c7320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventClouds                 =0x436c6473 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventColorBalance           =0x436c7242 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventColorCast              =0x436f6c45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventColorHalftone          =0x436c7248 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventColorRange             =0x436c7252 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventColoredPencil          =0x436c7250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventConteCrayon            =0x436e7443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventContract               =0x436e7463 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventConvertMode            =0x436e764d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCopy                   =0x636f7079 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCopyEffects            =0x43704658 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCopyMerged             =0x4370794d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCopyToLayer            =0x4370544c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCraquelure             =0x4372716c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCreateDroplet          =0x43727444 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCrop                   =0x43726f70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCrosshatch             =0x43727368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCrystallize            =0x43727374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCurves                 =0x43727673 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCustom                 =0x4373746d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCut                    =0x63757420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCutToLayer             =0x4374544c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventCutout                 =0x43742020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDarkStrokes            =0x44726b53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDeInterlace            =0x446e7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDefinePattern          =0x44666e50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDefringe               =0x44667267 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDelete                 =0x446c7420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDesaturate             =0x44737474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDeselect               =0x44736c63 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDespeckle              =0x44737063 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDifferenceClouds       =0x44667243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDiffuse                =0x44667320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDiffuseGlow            =0x44667347 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDisableLayerFX         =0x646c6678 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDisplace               =0x4473706c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDistribute             =0x44737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDraw                   =0x44726177 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDryBrush               =0x44727942 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDuplicate              =0x44706c63 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventDustAndScratches       =0x44737453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventEmboss                 =0x456d6273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventEqualize               =0x45716c7a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventExchange               =0x45786368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventExpand                 =0x4578706e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventExport                 =0x45787072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventExtrude                =0x45787472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFacet                  =0x46637420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFade                   =0x46616465 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFeather                =0x46746872 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFill                   =0x466c2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFillFlash              =0x46696c45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFilmGrain              =0x466c6d47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFilter                 =0x466c7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFindEdges              =0x466e6445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFlattenImage           =0x466c7449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFlip                   =0x466c6970 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFragment               =0x4672676d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventFresco                 =0x46727363 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGaussianBlur           =0x47736e42 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGet                    =0x67657464 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGlass                  =0x476c7320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGlowingEdges           =0x476c7745 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGradient               =0x4772646e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGradientMap            =0x47724d70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGrain                  =0x47726e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGraphicPen             =0x47726150 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGroup                  =0x4772704c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventGrow                   =0x47726f77 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventHSBHSL                 =0x48736250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventHalftoneScreen         =0x486c6653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventHide                   =0x48642020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventHighPass               =0x48676850 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventHueSaturation          =0x48537472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventImageSize              =0x496d6753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventImport                 =0x496d7072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventInkOutlines            =0x496e6b4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventIntersect              =0x496e7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventIntersectWith          =0x496e7457 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventInverse                =0x496e7673 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventInvert                 =0x496e7672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventJumpto                 =0x4a70746f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventLensFlare              =0x4c6e7346 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventLevels                 =0x4c766c73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventLightingEffects        =0x4c676845 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventLink                   =0x4c6e6b20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMake                   =0x4d6b2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMaximum                =0x4d786d20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMedian                 =0x4d646e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMergeLayers            =0x4d72674c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMergeSpotChannel       =0x4d537074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMergeVisible           =0x4d726756 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMezzotint              =0x4d7a746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMinimum                =0x4d6e6d20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMosaic                 =0x4d736320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMosaic_PLUGIN          =0x4d736354 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMotionBlur             =0x4d746e42 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventMove                   =0x6d6f7665 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventNTSCColors             =0x4e545343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventNeonGlow               =0x4e476c77 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventNext                   =0x4e787420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventNotePaper              =0x4e745072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventNotify                 =0x4e746679 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventNull                   =0x6e756c6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventOceanRipple            =0x4f636e52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventOffset                 =0x4f667374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventOpen                   =0x4f706e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPaintDaubs             =0x506e7444 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPaletteKnife           =0x506c744b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPaste                  =0x70617374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPasteEffects           =0x50614658 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPasteInto              =0x50737449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPasteOutside           =0x5073744f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPatchwork              =0x50746368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPhotocopy              =0x50687463 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPinch                  =0x506e6368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPlace                  =0x506c6320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPlaster                =0x506c7374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPlasticWrap            =0x506c7357 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPlay                   =0x506c7920 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPointillize            =0x506e746c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPolar                  =0x506c7220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPosterEdges            =0x50737445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPosterize              =0x50737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPrevious               =0x50727673 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPrint                  =0x50726e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventProfileToProfile       =0x50726654 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventPurge                  =0x50726765 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventQuit                   =0x71756974 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRadialBlur             =0x52646c42 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRasterize              =0x52737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRasterizeTypeSheet     =0x52737454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRemoveBlackMatte       =0x526d7642 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRemoveLayerMask        =0x526d764c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRemoveWhiteMatte       =0x526d7657 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRename                 =0x526e6d20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventReplaceColor           =0x52706c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventReset                  =0x52736574 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventReticulation           =0x5274636c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRevert                 =0x52767274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRipple                 =0x52706c65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRotate                 =0x52747465 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventRoughPastels           =0x52676850 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSave                   =0x73617665 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSelect                 =0x736c6374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSelectiveColor         =0x536c6343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSet                    =0x73657464 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSharpen                =0x53687270 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSharpenEdges           =0x53687245 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSharpenMore            =0x5368724d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventShear                  =0x53687220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventShow                   =0x53687720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSimilar                =0x536d6c72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSmartBlur              =0x536d7242 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSmooth                 =0x536d7468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSmudgeStick            =0x536d6453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSolarize               =0x536c727a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSpatter                =0x53707420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSpherize               =0x53706872 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSplitChannels          =0x53706c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSponge                 =0x53706e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSprayedStrokes         =0x53707253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventStainedGlass           =0x53746e47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventStamp                  =0x53746d70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventStop                   =0x53746f70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventStroke                 =0x5374726b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSubtract               =0x53627472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSubtractFrom           =0x53627446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventSumie                  =0x536d6965 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTakeMergedSnapshot     =0x546b4d72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTakeSnapshot           =0x546b536e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTextureFill            =0x54787446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTexturizer             =0x5478747a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventThreshold              =0x54687273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTiles                  =0x546c7320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTornEdges              =0x54726e45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTraceContour           =0x54726343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTransform              =0x54726e66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTrap                   =0x54726170 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventTwirl                  =0x5477726c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventUnderpainting          =0x556e6472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventUndo                   =0x756e646f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventUngroup                =0x556e6772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventUnlink                 =0x556e6c6b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventUnsharpMask            =0x556e734d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventVariations             =0x5672746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventWait                   =0x57616974 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventWaterPaper             =0x57747250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventWatercolor             =0x57747263 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventWave                   =0x57617665 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventWind                   =0x576e6420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phEventZigZag                 =0x5a675a67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormAbsolutePosition        =0x696e6478 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormClass                   =0x436c7373 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormEnumerated              =0x456e6d72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormIdentifier              =0x49646e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormIndex                   =0x696e6478 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormOffset                  =0x72656c65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormProperty                =0x70726f70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormPropertyID              =0x70726f70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phFormRelativePosition        =0x72656c65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKey3DAntiAlias              =0x416c6973 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyA                        =0x41202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAdjustment               =0x41646a73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAligned                  =0x416c6764 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAlignment                =0x416c676e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAllExcept                =0x416c6c45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAllPS                    =0x416c6c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAllToolOptions           =0x416c546c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAlphaChannelOptions      =0x4143686e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAlphaChannels            =0x416c7043 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAmbientBrightness        =0x416d6242 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAmbientColor             =0x416d6243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAmount                   =0x416d6e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAmplitudeMax             =0x416d4d78 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAmplitudeMin             =0x416d4d6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAnchor                   =0x416e6368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAngle                    =0x416e676c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAngle1                   =0x416e6731 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAngle2                   =0x416e6732 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAngle3                   =0x416e6733 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAngle4                   =0x416e6734 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAntiAlias                =0x416e7441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAppend                   =0x41707065 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyApply                    =0x41706c79 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyArea                     =0x41722020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyArrowhead                =0x41727277 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAs                       =0x41732020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAssumedCMYK              =0x41737343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAssumedGray              =0x41737347 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAssumedRGB               =0x41737352 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAt                       =0x41742020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAuto                     =0x4175746f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAutoContrast             =0x4175436f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAutoErase                =0x41747273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAutoKern                 =0x41744b72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAutoUpdate               =0x41745570 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyAxis                     =0x41786973 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyB                        =0x42202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBackground               =0x42636b67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBackgroundColor          =0x42636b43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBackgroundLevel          =0x42636b4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBackward                 =0x42776420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBalance                  =0x426c6e63 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBaselineShift            =0x42736c6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBeepWhenDone             =0x42705768 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBeginRamp                =0x42676e52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBeginSustain             =0x42676e53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBevelDirection           =0x62766c44 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBevelEmboss              =0x6562626c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBevelStyle               =0x62766c53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBevelTechnique           =0x62766c54 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBigNudgeH                =0x42674e48 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBigNudgeV                =0x42674e56 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBitDepth                 =0x42744470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlack                    =0x426c636b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlackClip                =0x426c6343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlackGeneration          =0x426c636e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlackGenerationCurve     =0x426c6347 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlackIntensity           =0x426c6349 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlackLevel               =0x426c634c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlackLimit               =0x426c634c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBleed                    =0x426c6420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlendRange               =0x426c6e64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlue                     =0x426c2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlueBlackPoint           =0x426c426c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlueGamma                =0x426c476d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlueWhitePoint           =0x426c5768 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlueX                    =0x426c5820 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlueY                    =0x426c5920 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlur                     =0x626c7572 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlurMethod               =0x426c724d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBlurQuality              =0x426c7251 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBook                     =0x426b2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBorderThickness          =0x42726454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBottom                   =0x42746f6d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBrightness               =0x42726768 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBrushDetail              =0x42727344 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBrushSize                =0x42727353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBrushType                =0x42727354 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBrushes                  =0x42727368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBumpAmplitude            =0x426d7041 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBumpChannel              =0x426d7043 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBy                       =0x42792020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyByline                   =0x42796c6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyBylineTitle              =0x42796c54 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyByteOrder                =0x4279744f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCMYKSetup                =0x434d5953 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCachePrefs               =0x43636850 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCalculation              =0x436c636c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCalibrationBars          =0x436c6272 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCaption                  =0x4370746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCaptionWriter            =0x43707457 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCategory                 =0x43746772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCellSize                 =0x436c537a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCenter                   =0x436e7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCenterCropMarks          =0x436e7443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyChalkArea                =0x43686c41 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyChannel                  =0x43686e6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyChannelMatrix            =0x43684d78 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyChannelName              =0x43686e4e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyChannels                 =0x43686e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyChannelsInterleaved      =0x43686e49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCharcoalAmount           =0x4368416d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCharcoalArea             =0x43687241 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyChokeMatte               =0x436b6d74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyChromeFX                 =0x43684658 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCity                     =0x43697479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyClearAmount              =0x436c7241 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyClippingPath             =0x436c5074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyClippingPathEPS          =0x436c7050 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyClippingPathFlatness     =0x436c7046 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyClippingPathIndex        =0x436c7049 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyClippingPathInfo         =0x436c7067 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCloneSource              =0x436c6e53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyClosedSubpath            =0x436c7370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColor                    =0x436c7220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorChannels            =0x436c7268 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorCorrection          =0x436c7243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorIndicates           =0x436c7249 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorManagement          =0x436c4d67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorPickerPrefs         =0x436c7272 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorSpace               =0x436c7253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorTable               =0x436c7254 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorize                 =0x436c727a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColors                   =0x436c7273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColorsList               =0x436c724c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyColumnWidth              =0x436c6d57 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCommandKey               =0x436d644b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCompensation             =0x436d706e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCompression              =0x436d7072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyConcavity                =0x436e6376 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCondition                =0x436e6474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyConstant                 =0x436e7374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyConstrain                =0x436e7374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyConstrainProportions     =0x436e7350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyConstructionFOV          =0x43666f76 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyContiguous               =0x436e7467 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyContinue                 =0x436e746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyContinuity               =0x436e7479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyContourType              =0x53687043 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyContrast                 =0x436e7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyConvert                  =0x436e7672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCopy                     =0x43707920 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCopyright                =0x43707972 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCopyrightNotice          =0x4370724e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCornerCropMarks          =0x43726e43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCount                    =0x436e7420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCountryName              =0x436e744e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCrackBrightness          =0x43726342 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCrackDepth               =0x43726344 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCrackSpacing             =0x43726353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCreateLayersFromLayerFX  =0x626c666c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCredit                   =0x43726474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCrossover                =0x43727373 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCurrent                  =0x43726e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCurrentHistoryState      =0x43726e48 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCurrentLight             =0x43726e4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCurrentToolOptions       =0x43726e54 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCurve                    =0x43727620 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCurveFile                =0x43727646 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCustom                   =0x4373746d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCustomForced             =0x43737446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCustomMatte              =0x4373744d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCustomPalette            =0x43737450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyCyan                     =0x43796e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDCS                      =0x44435320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDarkIntensity            =0x44726b49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDarker                   =0x4461726b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDarkness                 =0x44726b6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDateCreated              =0x44744372 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDatum                    =0x44742020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDefinition               =0x44666e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDensity                  =0x446e7374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDepth                    =0x44707468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDestBlackMax             =0x4473746c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDestBlackMin             =0x44737442 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDestWhiteMax             =0x44737474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDestWhiteMin             =0x44737457 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDestinationMode          =0x4473744d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDetail                   =0x44746c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDiameter                 =0x446d7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDiffusionDither          =0x44666644 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDirection                =0x44726374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDirectionBalance         =0x44726342 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDisplaceFile             =0x44737046 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDisplacementMap          =0x4473704d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDisplayPrefs             =0x44737050 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDistance                 =0x4473746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDistortion               =0x44737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDistribution             =0x44737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDither                   =0x44746872 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDitherAmount             =0x44746841 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDitherPreserve           =0x44746870 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDitherQuality            =0x44746871 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDocumentID               =0x446f6349 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDotGain                  =0x4474476e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDotGainCurves            =0x44744743 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDropShadow               =0x44725368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDuplicate                =0x44706c63 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyDynamicColorSliders      =0x446e6d43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEdge                     =0x45646720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEdgeBrightness           =0x45646742 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEdgeFidelity             =0x45646746 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEdgeIntensity            =0x45646749 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEdgeSimplicity           =0x45646753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEdgeThickness            =0x45646754 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEdgeWidth                =0x45646757 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEffect                   =0x45666663 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEmbedCMYK                =0x456d6243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEmbedGray                =0x456d6247 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEmbedLab                 =0x456d624c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEmbedProfiles            =0x456d6250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEmbedRGB                 =0x456d6252 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEmulsionDown             =0x456d6c44 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEnabled                  =0x656e6162 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEncoding                 =0x456e6364 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEnd                      =0x456e6420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEndArrowhead             =0x456e6441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEndRamp                  =0x456e6452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEndSustain               =0x456e6453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEngine                   =0x456e676e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEraseToHistory           =0x45727354 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEraserKind               =0x4572734b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExactPoints              =0x45786350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExport                   =0x45787072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExportClipboard          =0x45787043 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExposure                 =0x45787073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtend                   =0x45787464 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtendedQuality          =0x45516c74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtension                =0x4578746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtensionsQuery          =0x45787451 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtrudeDepth             =0x45787444 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtrudeMaskIncomplete    =0x4578744d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtrudeRandom            =0x45787452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtrudeSize              =0x45787453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtrudeSolidFace         =0x45787446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyExtrudeType              =0x45787454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyEyeDropperSample         =0x45794472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFPXCompress              =0x4678436d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFPXQuality               =0x4678516c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFPXSize                  =0x4678537a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFPXView                  =0x46785677 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFadeTo                   =0x46645420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFadeoutSteps             =0x46647453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFalloff                  =0x466c4f66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFeather                  =0x46746872 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFiberLength              =0x4662724c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFile                     =0x46696c65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFileCreator              =0x466c4372 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFileInfo                 =0x466c496e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFileReference            =0x46696c52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFileSavePrefs            =0x466c5350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFileType                 =0x466c5479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFill                     =0x466c2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFillColor                =0x466c436c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFillNeutral              =0x466c4e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFingerpainting           =0x466e6772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFlareCenter              =0x466c7243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFlatness                 =0x466c746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFlatten                  =0x466c7474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFlipVertical             =0x466c7056 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFocus                    =0x46637320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFolders                  =0x466c6472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFontDesignAxes           =0x466e7444 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFontDesignAxesVectors    =0x466e7456 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFontName                 =0x466e744e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFontScript               =0x53637270 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFontStyleName            =0x466e7453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFontTechnology           =0x466e7454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyForcedColors             =0x46726343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyForegroundColor          =0x46726743 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyForegroundLevel          =0x4672674c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFormat                   =0x466d7420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyForward                  =0x46776420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFrameFX                  =0x46724658 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFrameWidth               =0x46726d57 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFreeTransformCenterState =0x46546373 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFrequency                =0x4672716e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFrom                     =0x46726f6d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFromBuiltin              =0x46726d42 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFromMode                 =0x46726d4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFunctionKey              =0x466e634b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyFuzziness                =0x467a6e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGCR                      =0x47435220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFColorFileType         =0x47465054 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFColorLimit            =0x4746434c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFExportCaption         =0x47464543 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFMaskChannelIndex      =0x47464d49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFMaskChannelInverted   =0x47464d56 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFPaletteFile           =0x47465046 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFPaletteType           =0x4746504c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFRequiredColorSpaceType=0x47464353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFRowOrderType          =0x47464954 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFTransparentColor      =0x47465443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFTransparentIndexBlue  =0x47465442 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFTransparentIndexGreen =0x47465447 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFTransparentIndexRed   =0x47465452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGIFUseBestMatch          =0x4746424d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGamma                    =0x476d6d20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGamutWarning             =0x476d7457 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGeneralPrefs             =0x476e7250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGlobalAngle              =0x67626c41 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGlobalLightingAngle      =0x6761676c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGloss                    =0x476c6f73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGlowAmount               =0x476c7741 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGlowTechnique            =0x476c7754 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGradient                 =0x47726164 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGradientFill             =0x47726466 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGrain                    =0x47726e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGrainType                =0x47726e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGraininess               =0x47726e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGray                     =0x47727920 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGrayBehavior             =0x47724268 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGraySetup                =0x47725374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGreen                    =0x47726e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGreenBlackPoint          =0x47726e42 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGreenGamma               =0x47726e47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGreenWhitePoint          =0x47726e57 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGreenX                   =0x47726e58 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGreenY                   =0x47726e59 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGridColor                =0x47726443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGridCustomColor          =0x47726473 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGridMajor                =0x4772644d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGridMinor                =0x4772646e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGridStyle                =0x47726453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGridUnits                =0x47726474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGroup                    =0x47727570 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGroutWidth               =0x47727457 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGuides                   =0x47646573 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGuidesColor              =0x47647343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGuidesCustomColor        =0x47647373 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGuidesPrefs              =0x47645072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGuidesStyle              =0x47647353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyGutterWidth              =0x47747457 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHalftoneFile             =0x486c6646 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHalftoneScreen           =0x486c6653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHalftoneSize             =0x486c537a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHalftoneSpec             =0x486c6670 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHardness                 =0x4872646e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHeader                   =0x48647220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHeadline                 =0x48646c6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHeight                   =0x48676874 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHighlightArea            =0x48676841 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHighlightColor           =0x68676c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHighlightLevels          =0x4867684c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHighlightMode            =0x68676c4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHighlightOpacity         =0x68676c4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHighlightStrength        =0x48676853 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHistoryBrushSource       =0x48737442 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHistoryPrefs             =0x48737450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHistoryStateSource       =0x48735353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHistoryStates            =0x48735374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHorizontal               =0x48727a6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHorizontalScale          =0x48727a53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHostName                 =0x4873744e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHostVersion              =0x48737456 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyHue                      =0x48202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyICCEngine                =0x49434345 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyICCSetupName             =0x49434374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyID                       =0x49646e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyIdle                     =0x49646c65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyImageBalance             =0x496d6742 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyImport                   =0x496d7072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyImpressionist            =0x496d7073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyIn                       =0x496e2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInherits                 =0x6340235e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInkColors                =0x496e6b43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInks                     =0x496e6b73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInnerGlow                =0x4972476c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInnerGlowSource          =0x676c7753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInnerShadow              =0x49725368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInput                    =0x496e7074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInputMapRange            =0x496e6d72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInputRange               =0x496e7072 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyIntensity                =0x496e746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyIntent                   =0x496e7465 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceBevelHighlight  =0x496e7448 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceBevelShadow     =0x496e7476 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceBlack           =0x496e7442 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceBorder          =0x496e7464 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceButtonDarkShadow=0x496e746b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceButtonDownFill  =0x496e7474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceButtonUpFill    =0x496e4246 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceColorBlue2      =0x4943424c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceColorBlue32     =0x49434248 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceColorGreen2     =0x4943474c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceColorGreen32    =0x49434748 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceColorRed2       =0x4943524c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceColorRed32      =0x49435248 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceIconFillActive  =0x496e7449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceIconFillDimmed  =0x496e7446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceIconFillSelected=0x496e7463 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceIconFrameActive =0x496e746d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceIconFrameDimmed =0x496e7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceIconFrameSelected=0x496e7453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfacePaletteFill     =0x496e7450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceRed             =0x496e7452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceToolTipBackground=0x496e7454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceToolTipText     =0x49545454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceTransparencyBackground=0x49544267 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceTransparencyForeground=0x49544667 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterfaceWhite           =0x496e7457 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterlace                =0x496e7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterlaceCreateType      =0x496e7443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterlaceEliminateType   =0x496e7445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterpolation            =0x496e7472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInterpolationMethod      =0x496e744d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInvert                   =0x496e7672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInvertMask               =0x496e764d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInvertSource2            =0x496e7653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyInvertTexture            =0x496e7654 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyIsDirty                  =0x49734472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyItemIndex                =0x49746d49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyJPEGQuality              =0x4a504551 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyKerning                  =0x4b726e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyKeywords                 =0x4b797764 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyKind                     =0x4b6e6420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLUTAnimation             =0x4c546e6d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLZWCompression           =0x4c5a5743 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLabels                   =0x4c626c73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLandscape                =0x4c6e6473 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLastTransform            =0x4c737454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLayer                    =0x4c797220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLayerEffects             =0x4c656678 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLayerFXVisible           =0x6c667876 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLayerID                  =0x4c797249 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLayerName                =0x4c79724e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLayers                   =0x4c797273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLeading                  =0x4c646e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLeft                     =0x4c656674 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLegacySerialString       =0x6c534e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLength                   =0x4c6e6774 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLens                     =0x4c6e7320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLevel                    =0x4c766c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLevels                   =0x4c766c73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLightDark                =0x4c674472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLightDirection           =0x4c676844 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLightIntensity           =0x4c676849 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLightPosition            =0x4c676850 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLightSource              =0x4c676853 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLightType                =0x4c676854 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLightenGrout             =0x4c676847 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLighter                  =0x4c696768 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLightness                =0x4c676874 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLine                     =0x4c696e65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLinkedLayerIDs           =0x4c6e6b4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLocalLightingAltitude    =0x4c616c64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLocalLightingAngle       =0x6c61676c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLocalRange               =0x4c636c52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLocation                 =0x4c63746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLog                      =0x4c6f6720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLowerCase                =0x4c774373 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyLuminance                =0x4c6d6e63 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMagenta                  =0x4d676e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMakeVisible              =0x4d6b5673 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyManipulationFOV          =0x4d666f76 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMapBlack                 =0x4d70426c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMapping                  =0x4d706e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMappingShape             =0x4d706753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMaterial                 =0x4d74726c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMatrix                   =0x4d747278 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMatteColor               =0x4d747443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMaximum                  =0x4d786d20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMaximumStates            =0x4d786d53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMemoryUsagePercent       =0x4d6d7255 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMerge                    =0x4d726765 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMerged                   =0x4d726764 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMessage                  =0x4d736765 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMethod                   =0x4d746864 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMezzotintType            =0x4d7a7454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMidpoint                 =0x4d64706e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMidtoneLevels            =0x4d64744c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMinimum                  =0x4d6e6d20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMismatchCMYK             =0x4d736d43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMismatchGray             =0x4d736d47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMismatchRGB              =0x4d736d52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMode                     =0x4d642020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMonochromatic            =0x4d6e6368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyMoveTo                   =0x4d765420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyName                     =0x4e6d2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNegative                 =0x4e677476 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNew                      =0x4e772020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNoise                    =0x4e6f7365 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNonImageData             =0x4e6e496d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNonLinear                =0x4e6e4c6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNull                     =0x6e756c6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumLights                =0x4e6d2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumber                   =0x4e6d6272 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfCacheLevels      =0x4e436368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfChannels         =0x4e6d624f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfChildren         =0x4e6d6243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfDocuments        =0x4e6d6244 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfGenerators       =0x4e6d6247 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfLayers           =0x4e6d624c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfLevels           =0x4e6d624c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfPaths            =0x4e6d6250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfRipples          =0x4e6d6252 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyNumberOfSiblings         =0x4e6d6253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyObjectName               =0x4f626a4e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOffset                   =0x4f667374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOn                       =0x4f6e2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOpacity                  =0x4f706374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOptimized                =0x4f70746d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOrientation              =0x4f726e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOriginalHeader           =0x4f726748 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOriginalTransmissionReference=0x4f726754 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOtherCursors             =0x4f746843 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOuterGlow                =0x4f72476c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOutput                   =0x4f747074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOverprintColors          =0x4f767243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOverrideOpen             =0x4f76724f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOverridePrinter          =0x4f627250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyOverrideSave             =0x4f767264 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPNGFilter                =0x504e4766 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPNGInterlaceType         =0x50474954 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPageFormat               =0x504d7066 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPageNumber               =0x50674e6d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPagePosition             =0x50675073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPageSetup                =0x50675374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPaintCursorKind          =0x506e434b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPaintType                =0x506e7454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPaintingCursors          =0x506e7443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPalette                  =0x506c7420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPaletteFile              =0x506c7446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPaperBrightness          =0x50707242 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyParentIndex              =0x5072496e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyParentName               =0x50724e6d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPath                     =0x50617468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPathContents             =0x50746843 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPathName                 =0x5074684e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPattern                  =0x5074746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPencilWidth              =0x506e636c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPerspectiveIndex         =0x50727370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPhosphors                =0x50687370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPickerID                 =0x50636b49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPickerKind               =0x50636b72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPixelPaintSize           =0x5050537a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPlatform                 =0x506c7466 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPluginFolder             =0x506c6746 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPluginPrefs              =0x506c6750 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPoints                   =0x50747320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPosition                 =0x5073746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPostScriptColor          =0x50737453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPosterization            =0x50737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPredefinedColors         =0x50726443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreferBuiltin            =0x50726642 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreferences              =0x50726672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreserveAdditional       =0x50727341 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreserveLuminosity       =0x5072734c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreserveTransparency     =0x50727354 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPressure                 =0x50727320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreview                  =0x50727677 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreviewCMYK              =0x5072764b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreviewFullSize          =0x50727646 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreviewIcon              =0x50727649 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreviewMacThumbnail      =0x5072764d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreviewWinThumbnail      =0x50727657 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPreviewsQuery            =0x50727651 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyPrintSettings            =0x504d7073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyProfileSetup             =0x50726653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyProvinceState            =0x50727653 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyQuality                  =0x516c7479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyQuickMask                =0x5175634d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRGBSetup                 =0x52474253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRadius                   =0x52647320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRandomSeed               =0x526e6453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRatio                    =0x52742020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRecentFiles              =0x52636e66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRed                      =0x52642020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRedBlackPoint            =0x5264426c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRedGamma                 =0x5264476d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRedWhitePoint            =0x52645768 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRedX                     =0x52645820 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRedY                     =0x52645920 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRegistrationMarks        =0x5267734d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRelative                 =0x526c7476 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRelief                   =0x526c6620 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRenderFidelity           =0x52666964 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyResample                 =0x52736d70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyResizeWindowsOnZoom      =0x52574f5a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyResolution               =0x52736c74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyResourceID               =0x52737249 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyResponse                 =0x5273706e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRetainHeader             =0x52746e48 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyReverse                  =0x52767273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRight                    =0x52676874 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRippleMagnitude          =0x52706c4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRippleSize               =0x52706c53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRotate                   =0x52747420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRoundness                =0x526e646e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRulerOriginH             =0x526c7248 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRulerOriginV             =0x526c7256 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyRulerUnits               =0x526c7255 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySaturation               =0x53747274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySaveAndClose             =0x5376416e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySaveComposite            =0x5376436d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySavePaletteLocations     =0x506c744c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySavePaths                =0x53765074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySavePyramids             =0x53765079 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySaving                   =0x53766e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyScale                    =0x53636c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyScaleHorizontal          =0x53636c48 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyScaleVertical            =0x53636c56 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyScaling                  =0x53636c6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyScans                    =0x53636e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyScratchDisks             =0x53637244 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyScreenFile               =0x53637246 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyScreenType               =0x53637254 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySelection                =0x6673656c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySeparations              =0x53707274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySerialString             =0x53726c53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShadingIntensity         =0x53686449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShadingNoise             =0x5368644e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShadingShape             =0x53686453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShadowColor              =0x73647743 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShadowIntensity          =0x53686449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShadowLevels             =0x5368644c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShadowMode               =0x7364774d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShadowOpacity            =0x7364774f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShape                    =0x53687020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySharpness                =0x53687270 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShearEd                  =0x53687245 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShearPoints              =0x53687250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShearSt                  =0x53687253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShiftKey                 =0x5368664b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShiftKeyToolSwitch       =0x53684b54 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShortNames               =0x5368724e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShowEnglishFontNames     =0x53687745 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShowToolTips             =0x53687754 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyShowTransparency         =0x53685472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySizeKey                  =0x537a2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySkew                     =0x536b6577 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySmartBlurMode            =0x536d424d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySmartBlurQuality         =0x536d4251 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySmooth                   =0x536d6f6f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySmoothness               =0x536d7468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySnapshotInitial          =0x536e7049 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySoftness                 =0x5366746e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySolidFill                =0x536f4669 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySource                   =0x53726365 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySource2                  =0x53726332 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySourceMode               =0x5372634d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySpacing                  =0x5370636e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySpecialInstructions      =0x53706349 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySpherizeMode             =0x5370684d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySpot                     =0x53706f74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySprayRadius              =0x53707252 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySquareSize               =0x53717253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySrcBlackMax              =0x5372636c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySrcBlackMin              =0x53726342 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySrcWhiteMax              =0x5372636d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySrcWhiteMin              =0x53726357 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStart                    =0x53747274 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStartArrowhead           =0x53747241 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyState                    =0x53747465 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrength                 =0x73726768 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrengthRatio            =0x73726752 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrength_PLUGIN          =0x53747267 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrokeDetail             =0x53744474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrokeDirection          =0x53446972 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrokeLength             =0x5374724c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrokePressure           =0x53747250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrokeSize               =0x53747253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStrokeWidth              =0x53747257 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStyle                    =0x5374796c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStyles                   =0x53747973 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStylusIsColor            =0x53746c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStylusIsOpacity          =0x53746c4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStylusIsPressure         =0x53746c50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyStylusIsSize             =0x53746c53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySubPathList              =0x5362704c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySupplementalCategories   =0x53706c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySystemInfo               =0x53737449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeySystemPalette            =0x53737450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTarget                   =0x6e756c6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTargetPath               =0x54726770 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTargetPathIndex          =0x54726750 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyText                     =0x54787420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTextClickPoint           =0x54787443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTextData                 =0x54787444 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTextStyle                =0x54787453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTextStyleRange           =0x54787474 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTexture                  =0x54787472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTextureCoverage          =0x54787443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTextureFile              =0x54787446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTextureType              =0x54787454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyThreshold                =0x54687368 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTileNumber               =0x546c4e6d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTileOffset               =0x546c4f66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTileSize                 =0x546c537a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTitle                    =0x54746c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTo                       =0x54202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyToBuiltin                =0x54426c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyToLinked                 =0x546f4c6b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyToMode                   =0x544d6420 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyToggleOthers             =0x54676c4f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTolerance                =0x546c726e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTop                      =0x546f7020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTotalLimit               =0x54746c4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTracking                 =0x5472636b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransferFunction         =0x54726e46 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransferSpec             =0x54726e53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransparency             =0x54726e73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransparencyGrid         =0x54726e47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransparencyGridColors   =0x54726e43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransparencyGridSize     =0x54726e47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransparencyPrefs        =0x54726e50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransparencyShape        =0x54726e53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransparentIndex         =0x54726e49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTransparentWhites        =0x54726e57 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyTwist                    =0x54777374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyType                     =0x54797065 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUCA                      =0x55432020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyURL                      =0x55524c20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUndefinedArea            =0x556e6441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUnderline                =0x556e646c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUnitsPrefs               =0x556e7450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUntitled                 =0x556e746c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUpperY                   =0x55707059 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUrgency                  =0x5572676e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUseAccurateScreens       =0x41637253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUseAdditionalPlugins     =0x4164506c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUseCacheForHistograms    =0x55734363 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUseCurves                =0x55734372 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUseDefault               =0x55734466 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUseGlobalAngle           =0x75676c67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUseICCProfile            =0x55734943 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUseMask                  =0x55734d73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUserMaskEnabled          =0x5573724d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUserMaskLinked           =0x55737273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyUsing                    =0x55736e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyValue                    =0x566c2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVector0                  =0x56637430 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVector1                  =0x56637431 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVectorColor              =0x56637443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVersionFix               =0x56727346 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVersionMajor             =0x5672734d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVersionMinor             =0x5672734e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVertical                 =0x56727463 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVerticalScale            =0x56727453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVideoAlpha               =0x56646c70 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyVisible                  =0x5673626c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWatchSuspension          =0x57746353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWatermark                =0x77617472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWaveType                 =0x57767470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWavelengthMax            =0x574c4d78 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWavelengthMin            =0x574c4d6e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWebdavPrefs              =0x57626450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWetEdges                 =0x57746467 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWhat                     =0x57686174 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWhiteClip                =0x57687443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWhiteIntensity           =0x57687449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWhiteIsHigh              =0x57684869 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWhiteLevel               =0x5768744c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWhitePoint               =0x57687450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWholePath                =0x57685074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWidth                    =0x57647468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWindMethod               =0x576e644d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWith                     =0x57697468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWorkPath                 =0x57725074 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyWorkPathIndex            =0x57726b50 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyX                        =0x58202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyY                        =0x59202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyYellow                   =0x596c7720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKeyZigZagType               =0x5a5a5479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phKey_Source                  =0x54202020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phPInherits                   =0x6340235e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeActionData              =0x41637444 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeActionReference         =0x23416374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeAlias                   =0x616c6973 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeAlignDistributeSelector =0x41445374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeAlignment               =0x416c6720 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeAmount                  =0x416d6e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeAntiAlias               =0x416e6e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeAreaSelector            =0x4172536c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeAssumeOptions           =0x4173734f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBevelEmbossStampStyle   =0x42455373 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBevelEmbossStyle        =0x4245536c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBitDepth                =0x42744470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBlackGeneration         =0x426c6347 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBlendMode               =0x426c6e4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBlurMethod              =0x426c724d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBlurQuality             =0x426c7251 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBoolean                 =0x626f6f6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBrushType               =0x42727354 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBuiltInContour          =0x426c7443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeBuiltinProfile          =0x426c7450 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeCMYKSetupEngine         =0x434d5945 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeCalculation             =0x436c636e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeChannel                 =0x43686e6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeChannelReference        =0x23436852 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeChar                    =0x54455854 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeCheckerboardSize        =0x4368636b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClass                   =0x74797065 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassColor              =0x23436c72 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassElement            =0x23436c45 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassExport             =0x23436c65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassFormat             =0x23436c46 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassHueSatHueSatV2     =0x23487356 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassImport             =0x23436c49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassMode               =0x23436c4d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassStringFormat       =0x23436c53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassTextExport         =0x23435445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeClassTextImport         =0x23436c54 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeColor                   =0x436c7220 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeColorChannel            =0x23436c43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeColorPalette            =0x436c7250 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeColorSpace              =0x436c7253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeColorStopType           =0x436c7279 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeColors                  =0x436c7273 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeCompensation            =0x436d706e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeContourEdge             =0x436e7445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeConvert                 =0x436e7672 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeCorrectionMethod        =0x4372634d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeCursorKind              =0x4372734b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDCS                     =0x44435320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDeepDepth               =0x44704470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDepth                   =0x44707468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDiffuseMode             =0x4466734d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDirection               =0x44726374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDisplacementMap         =0x4473704d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDistribution            =0x44737472 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDither                  =0x44746872 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDitherQuality           =0x44746871 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDocumentReference       =0x23446352 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeDouble                  =0x646f7562 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeEPSPreview              =0x45505350 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeElementReference        =0x23456c52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeEncoding                =0x456e6364 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeEnumerated              =0x656e756d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeEraserKind              =0x4572734b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeExtrudeRandom           =0x45787452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeExtrudeType             =0x45787454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeEyeDropperSample        =0x45794470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeFPXCompress             =0x4678436d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeFill                    =0x466c2020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeFillColor               =0x466c436c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeFillContents            =0x466c436e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeFillMode                =0x466c4d64 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeFloat                   =0x646f7562 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeForcedColors            =0x46726343 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeFrameFill               =0x4672466c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeFrameStyle              =0x4653746c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGIFColorFileType        =0x47465054 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGIFPaletteType          =0x4746504c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGIFRequiredColorSpaceType=0x47464353 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGIFRowOrderType         =0x47464954 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGlobalClass             =0x476c6243 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGlobalObject            =0x476c624f # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGradientForm            =0x47726446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGradientType            =0x47726454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGrainType               =0x47726e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGrayBehavior            =0x47724268 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGuideGridColor          =0x47644772 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeGuideGridStyle          =0x47644753 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeHistoryStateSource      =0x48737453 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeHorizontalLocation      =0x48727a4c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeImageReference          =0x23496d52 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeInnerGlowSource         =0x49475372 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeInteger                 =0x6c6f6e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeIntegerChannel          =0x23696e43 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeIntent                  =0x496e7465 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeInterlaceCreateType     =0x496e7443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeInterlaceEliminateType  =0x496e7445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeInterpolation           =0x496e7470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeKelvin                  =0x4b6c766e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeKelvinCustomWhitePoint  =0x234b6c76 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeLens                    =0x4c6e7320 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeLightDirection          =0x4c676844 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeLightPosition           =0x4c676850 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeLightType               =0x4c676854 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeLocationReference       =0x234c6374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeMaskIndicator           =0x4d736b49 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeMatteColor              =0x4d747443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeMatteTechnique          =0x42455445 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeMenuItem                =0x4d6e4974 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeMethod                  =0x4d746864 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeMezzotintType           =0x4d7a7454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeMode                    =0x4d642020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeNotify                  =0x4e746679 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeNull                    =0x6e756c6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeObject                  =0x4f626a63 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeObjectReference         =0x6f626a20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeObjectSpecifier         =0x6f626a20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeOnOff                   =0x4f6e4f66 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeOrdinal                 =0x4f72646e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeOrientation             =0x4f726e74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePNGFilter               =0x504e4766 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePNGInterlaceType        =0x50474954 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePagePosition            =0x50675073 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePath                    =0x50746820 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePathKind                =0x5074684b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePathReference           =0x23507452 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePhosphors               =0x50687370 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePhosphorsCustomPhosphors=0x23506873 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePickerKind              =0x50636b4b # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePixelPaintSize          =0x5050537a # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePlatform                =0x506c7466 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePreview                 =0x50727677 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePreviewCMYK             =0x50727674 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeProfileMismatch         =0x5072664d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypePurgeItem               =0x50726749 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeQuadCenterState         =0x51435374 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeQuality                 =0x516c7479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeQueryState              =0x51757253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeRGBSetupSource          =0x52474253 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeRawData                 =0x74647461 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeRippleSize              =0x52706c53 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeRulerUnits              =0x526c7255 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeScreenType              =0x53637254 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeShape                   =0x53687020 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeSmartBlurMode           =0x536d424d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeSmartBlurQuality        =0x536d4251 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeSourceMode              =0x436e646e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeSpherizeMode            =0x5370684d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeState                   =0x53747465 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeStringChannel           =0x23737468 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeStringClassFormat       =0x23537443 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeStringCompensation      =0x2353746d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeStringFSS               =0x23537466 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeStringInteger           =0x23537449 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeStrokeDirection         =0x53747244 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeStrokeLocation          =0x5374724c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeText                    =0x54455854 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeTextureType             =0x54787454 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeTransparencyGridColors  =0x54726e6c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeTransparencyGridSize    =0x54726e47 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeType                    =0x74797065 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeTypeClassModeOrClassMode=0x2354794d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeUndefinedArea           =0x556e6441 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeUnitDouble              =0x556e7446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeUnitFloat               =0x556e7446 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeUrgency                 =0x5572676e # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeUserMaskOptions         =0x5573724d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeValueList               =0x566c4c73 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeVerticalLocation        =0x5672744c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeWaveType                =0x57767470 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeWindMethod              =0x576e644d # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeYesNo                   =0x59734e20 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phTypeZigZagType              =0x5a5a5479 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phUnitAngle                   =0x23416e67 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phUnitDensity                 =0x2352736c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phUnitDistance                =0x23526c74 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phUnitNone                    =0x234e6e65 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phUnitPercent                 =0x23507263 # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001
	phUnitPixels                  =0x2350786c # from enum __MIDL___MIDL_itf_OLEActions_0000_0000_0001

from win32com.client import DispatchBaseClass
class IAction(DispatchBaseClass):
	"""Action."""
	CLSID = IID('{90CED626-8D78-11CF-86B4-444553540000}')
	coclass_clsid = None

	def Play(self):
		"""Plays action on active document"""
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"name": (1610743808, 2, (8, 0), (), "name", None),
	}
	_prop_map_put_ = {
	}

class IActionControl(DispatchBaseClass):
	"""Control interface for Photoshop actions system."""
	CLSID = IID('{38FB4290-9DF6-11D1-B032-00C04FD7EC47}')
	coclass_clsid = None

	def GetActionProperty(self, reference=defaultNamedNotOptArg, propertyDesc=pythoncom.Missing):
		return self._ApplyTypes_(1610743809, 1, (24, 0), ((9, 1), (16393, 2)), 'GetActionProperty', None,reference
			, propertyDesc)

	# Result is of type IActionDescriptor
	def Play(self, eventID=defaultNamedNotOptArg, parameters=defaultNamedNotOptArg, dialogOptions=defaultNamedNotOptArg):
		"""Plays an event."""
		ret = self._oleobj_.InvokeTypes(1610743808, LCID, 1, (9, 0), ((3, 1), (9, 1), (3, 1)),eventID
			, parameters, dialogOptions)
		if ret is not None:
			ret = Dispatch(ret, 'Play', '{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}', UnicodeToString=0)
		return ret

	def StringIDToTypeID(self, stringID=defaultNamedNotOptArg, typeID=pythoncom.Missing):
		return self._ApplyTypes_(1610743810, 1, (24, 0), ((8, 1), (16387, 2)), 'StringIDToTypeID', None,stringID
			, typeID)

	def TypeIDToStringID(self, typeID=defaultNamedNotOptArg, stringID=pythoncom.Missing):
		return self._ApplyTypes_(1610743811, 1, (24, 0), ((3, 1), (16392, 2)), 'TypeIDToStringID', None,typeID
			, stringID)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class IActionDescriptor(DispatchBaseClass):
	"""Container class for actions system parameters."""
	CLSID = IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')
	coclass_clsid = None

	def Clear(self):
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (24, 0), (),)

	def Erase(self, key=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((3, 1),),key
			)

	def GetBoolean(self, key=defaultNamedNotOptArg, retval=pythoncom.Missing):
		return self._ApplyTypes_(1610743823, 1, (24, 0), ((3, 1), (16387, 2)), 'GetBoolean', None,key
			, retval)

	def GetClass(self, key=defaultNamedNotOptArg, classID=pythoncom.Missing):
		return self._ApplyTypes_(1610743835, 1, (24, 0), ((3, 1), (16387, 2)), 'GetClass', None,key
			, classID)

	def GetCount(self, count=pythoncom.Missing):
		return self._ApplyTypes_(1610743811, 1, (24, 0), ((16387, 2),), 'GetCount', None,count
			)

	def GetData(self, key=defaultNamedNotOptArg, retval=pythoncom.Missing):
		return self._ApplyTypes_(1610743842, 1, (24, 0), ((3, 1), (16392, 2)), 'GetData', None,key
			, retval)

	def GetDataLength(self, key=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743841, 1, (24, 0), ((3, 1), (16387, 2)), 'GetDataLength', None,key
			, value)

	def GetDouble(self, key=defaultNamedNotOptArg, retval=pythoncom.Missing):
		return self._ApplyTypes_(1610743817, 1, (24, 0), ((3, 1), (16389, 2)), 'GetDouble', None,key
			, retval)

	def GetEnumerated(self, key=defaultNamedNotOptArg, enumType=pythoncom.Missing, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743831, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2)), 'GetEnumerated', None,key
			, enumType, value)

	def GetGlobalClass(self, key=defaultNamedNotOptArg, classID=pythoncom.Missing):
		return self._ApplyTypes_(1610743837, 1, (24, 0), ((3, 1), (16387, 2)), 'GetGlobalClass', None,key
			, classID)

	def GetGlobalObject(self, key=defaultNamedNotOptArg, classID=pythoncom.Missing, retval=pythoncom.Missing):
		return self._ApplyTypes_(1610743829, 1, (24, 0), ((3, 1), (16387, 2), (16393, 2)), 'GetGlobalObject', None,key
			, classID, retval)

	def GetInteger(self, key=defaultNamedNotOptArg, retval=pythoncom.Missing):
		return self._ApplyTypes_(1610743815, 1, (24, 0), ((3, 1), (16387, 2)), 'GetInteger', None,key
			, retval)

	def GetKey(self, index=defaultNamedNotOptArg, key=pythoncom.Missing):
		return self._ApplyTypes_(1610743809, 1, (24, 0), ((3, 1), (16387, 2)), 'GetKey', None,index
			, key)

	def GetList(self, key=defaultNamedNotOptArg, list=pythoncom.Missing):
		return self._ApplyTypes_(1610743825, 1, (24, 0), ((3, 1), (16393, 2)), 'GetList', None,key
			, list)

	def GetObject(self, key=defaultNamedNotOptArg, classID=pythoncom.Missing, retval=pythoncom.Missing):
		return self._ApplyTypes_(1610743827, 1, (24, 0), ((3, 1), (16387, 2), (16393, 2)), 'GetObject', None,key
			, classID, retval)

	def GetPath(self, key=defaultNamedNotOptArg, pathString=pythoncom.Missing):
		return self._ApplyTypes_(1610743839, 1, (24, 0), ((3, 1), (16392, 2)), 'GetPath', None,key
			, pathString)

	def GetReference(self, key=defaultNamedNotOptArg, reference=pythoncom.Missing):
		return self._ApplyTypes_(1610743833, 1, (24, 0), ((3, 1), (16393, 2)), 'GetReference', None,key
			, reference)

	def GetString(self, key=defaultNamedNotOptArg, retval=pythoncom.Missing):
		return self._ApplyTypes_(1610743821, 1, (24, 0), ((3, 1), (16392, 2)), 'GetString', None,key
			, retval)

	def GetType(self, key=defaultNamedNotOptArg, type=pythoncom.Missing):
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((3, 1), (16387, 2)), 'GetType', None,key
			, type)

	def GetUnitDouble(self, key=defaultNamedNotOptArg, unitID=pythoncom.Missing, retval=pythoncom.Missing):
		return self._ApplyTypes_(1610743819, 1, (24, 0), ((3, 1), (16387, 2), (16389, 2)), 'GetUnitDouble', None,key
			, unitID, retval)

	def HasKey(self, key=defaultNamedNotOptArg, HasKey=pythoncom.Missing):
		return self._ApplyTypes_(1610743810, 1, (24, 0), ((3, 1), (16387, 2)), 'HasKey', None,key
			, HasKey)

	def IsEqual(self, otherDesc=defaultNamedNotOptArg, IsEqual=pythoncom.Missing):
		return self._ApplyTypes_(1610743812, 1, (24, 0), ((9, 1), (16387, 2)), 'IsEqual', None,otherDesc
			, IsEqual)

	def PutBoolean(self, key=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743824, LCID, 1, (24, 0), ((3, 1), (3, 1)),key
			, value)

	def PutClass(self, key=defaultNamedNotOptArg, classID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743836, LCID, 1, (24, 0), ((3, 1), (3, 1)),key
			, classID)

	def PutData(self, key=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743843, LCID, 1, (24, 0), ((3, 1), (8, 1)),key
			, value)

	def PutDouble(self, key=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743818, LCID, 1, (24, 0), ((3, 1), (5, 1)),key
			, value)

	def PutEnumerated(self, key=defaultNamedNotOptArg, enumType=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743832, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),key
			, enumType, value)

	def PutGlobalClass(self, key=defaultNamedNotOptArg, classID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743838, LCID, 1, (24, 0), ((3, 1), (3, 1)),key
			, classID)

	def PutGlobalObject(self, key=defaultNamedNotOptArg, classID=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743830, LCID, 1, (24, 0), ((3, 1), (3, 1), (9, 1)),key
			, classID, value)

	def PutInteger(self, key=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743816, LCID, 1, (24, 0), ((3, 1), (3, 1)),key
			, value)

	def PutList(self, key=defaultNamedNotOptArg, list=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743826, LCID, 1, (24, 0), ((3, 1), (9, 1)),key
			, list)

	def PutObject(self, key=defaultNamedNotOptArg, classID=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743828, LCID, 1, (24, 0), ((3, 1), (3, 1), (9, 1)),key
			, classID, value)

	def PutPath(self, key=defaultNamedNotOptArg, pathString=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743840, LCID, 1, (24, 0), ((3, 1), (8, 1)),key
			, pathString)

	def PutReference(self, key=defaultNamedNotOptArg, reference=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743834, LCID, 1, (24, 0), ((3, 1), (9, 1)),key
			, reference)

	def PutString(self, key=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743822, LCID, 1, (24, 0), ((3, 1), (8, 1)),key
			, value)

	def PutUnitDouble(self, key=defaultNamedNotOptArg, unitID=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743820, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1)),key
			, unitID, value)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class IActionList(DispatchBaseClass):
	"""Container class for actions system lists."""
	CLSID = IID('{B249C0B0-A004-11D1-B036-00C04FD7EC47}')
	coclass_clsid = None

	def GetBoolean(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743818, 1, (24, 0), ((3, 1), (16387, 2)), 'GetBoolean', None,index
			, value)

	def GetClass(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743830, 1, (24, 0), ((3, 1), (16387, 2)), 'GetClass', None,index
			, value)

	def GetCount(self, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743809, 1, (24, 0), ((16387, 2),), 'GetCount', None,value
			)

	def GetData(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743837, 1, (24, 0), ((3, 1), (16392, 2)), 'GetData', None,index
			, value)

	def GetDataLength(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743836, 1, (24, 0), ((3, 1), (16387, 2)), 'GetDataLength', None,index
			, value)

	def GetDouble(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743812, 1, (24, 0), ((3, 1), (16389, 2)), 'GetDouble', None,index
			, value)

	def GetEnumerated(self, index=defaultNamedNotOptArg, type=pythoncom.Missing, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743826, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2)), 'GetEnumerated', None,index
			, type, value)

	def GetGlobalClass(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743832, 1, (24, 0), ((3, 1), (16387, 2)), 'GetGlobalClass', None,index
			, value)

	def GetGlobalObject(self, index=defaultNamedNotOptArg, type=pythoncom.Missing, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743824, 1, (24, 0), ((3, 1), (16387, 2), (16393, 2)), 'GetGlobalObject', None,index
			, type, value)

	def GetInteger(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743810, 1, (24, 0), ((3, 1), (16387, 2)), 'GetInteger', None,index
			, value)

	def GetList(self, index=defaultNamedNotOptArg, actionList=pythoncom.Missing):
		return self._ApplyTypes_(1610743820, 1, (24, 0), ((3, 1), (16393, 2)), 'GetList', None,index
			, actionList)

	def GetObject(self, index=defaultNamedNotOptArg, type=pythoncom.Missing, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743822, 1, (24, 0), ((3, 1), (16387, 2), (16393, 2)), 'GetObject', None,index
			, type, value)

	def GetPath(self, index=defaultNamedNotOptArg, pathString=pythoncom.Missing):
		return self._ApplyTypes_(1610743834, 1, (24, 0), ((3, 1), (16392, 2)), 'GetPath', None,index
			, pathString)

	def GetReference(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743828, 1, (24, 0), ((3, 1), (16393, 2)), 'GetReference', None,index
			, value)

	def GetString(self, index=defaultNamedNotOptArg, str=pythoncom.Missing):
		return self._ApplyTypes_(1610743816, 1, (24, 0), ((3, 1), (16392, 2)), 'GetString', None,index
			, str)

	def GetType(self, index=defaultNamedNotOptArg, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((3, 1), (16387, 2)), 'GetType', None,index
			, value)

	def GetUnitDouble(self, index=defaultNamedNotOptArg, unit=pythoncom.Missing, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743814, 1, (24, 0), ((3, 1), (16387, 2), (16389, 2)), 'GetUnitDouble', None,index
			, unit, value)

	def PutBoolean(self, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743819, LCID, 1, (24, 0), ((3, 1),),value
			)

	def PutClass(self, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743831, LCID, 1, (24, 0), ((3, 1),),value
			)

	def PutData(self, length=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743838, LCID, 1, (24, 0), ((3, 1), (8, 1)),length
			, value)

	def PutDouble(self, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((5, 1),),value
			)

	def PutEnumerated(self, type=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743827, LCID, 1, (24, 0), ((3, 1), (3, 1)),type
			, value)

	def PutGlobalClass(self, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743833, LCID, 1, (24, 0), ((3, 1),),value
			)

	def PutGlobalObject(self, type=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743825, LCID, 1, (24, 0), ((3, 1), (9, 1)),type
			, value)

	def PutInteger(self, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (24, 0), ((3, 1),),value
			)

	def PutList(self, actionList=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743821, LCID, 1, (24, 0), ((9, 1),),actionList
			)

	def PutObject(self, type=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743823, LCID, 1, (24, 0), ((3, 1), (9, 1)),type
			, value)

	def PutPath(self, pathString=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743835, LCID, 1, (24, 0), ((8, 1),),pathString
			)

	def PutReference(self, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743829, LCID, 1, (24, 0), ((9, 1),),value
			)

	def PutString(self, str=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743817, LCID, 1, (24, 0), ((8, 1),),str
			)

	def PutUnitDouble(self, unit=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (24, 0), ((3, 1), (5, 1)),unit
			, value)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class IActionReference(DispatchBaseClass):
	"""Container class for actions system references."""
	CLSID = IID('{B249C0B1-A004-11D1-B036-00C04FD7EC47}')
	coclass_clsid = None

	def GetContainer(self, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743823, 1, (24, 0), ((16393, 2),), 'GetContainer', None,value
			)

	def GetDesiredClass(self, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743809, 1, (24, 0), ((16387, 2),), 'GetDesiredClass', None,value
			)

	def GetEnumerated(self, type=pythoncom.Missing, enumValue=pythoncom.Missing):
		return self._ApplyTypes_(1610743819, 1, (24, 0), ((16387, 2), (16387, 2)), 'GetEnumerated', None,type
			, enumValue)

	def GetForm(self, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2),), 'GetForm', None,value
			)

	def GetIdentifier(self, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743815, 1, (24, 0), ((16387, 2),), 'GetIdentifier', None,value
			)

	def GetIndex(self, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743813, 1, (24, 0), ((16387, 2),), 'GetIndex', None,value
			)

	def GetName(self, name=pythoncom.Missing):
		return self._ApplyTypes_(1610743811, 1, (24, 0), ((16392, 2),), 'GetName', None,name
			)

	def GetOffset(self, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743817, 1, (24, 0), ((16387, 2),), 'GetOffset', None,value
			)

	def GetProperty(self, value=pythoncom.Missing):
		return self._ApplyTypes_(1610743821, 1, (24, 0), ((16387, 2),), 'GetProperty', None,value
			)

	def PutClass(self, desiredClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), ((3, 1),),desiredClass
			)

	def PutEnumerated(self, desiredClass=defaultNamedNotOptArg, type=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743820, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),desiredClass
			, type, value)

	def PutIdentifier(self, desiredClass=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743816, LCID, 1, (24, 0), ((3, 1), (3, 1)),desiredClass
			, value)

	def PutIndex(self, desiredClass=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (24, 0), ((3, 1), (3, 1)),desiredClass
			, value)

	def PutName(self, desiredClass=defaultNamedNotOptArg, name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743812, LCID, 1, (24, 0), ((3, 1), (8, 1)),desiredClass
			, name)

	def PutOffset(self, desiredClass=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743818, LCID, 1, (24, 0), ((3, 1), (3, 1)),desiredClass
			, value)

	def PutProperty(self, desiredClass=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743822, LCID, 1, (24, 0), ((3, 1), (3, 1)),desiredClass
			, value)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class IActions(DispatchBaseClass):
	"""Actions collection."""
	CLSID = IID('{90CED625-8D78-11CF-86B4-444553540000}')
	coclass_clsid = None

	# Result is of type IAction
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		"""Given an integer index, returns one of the Actions in the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{90CED626-8D78-11CF-86B4-444553540000}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"count": (1610743808, 2, (3, 0), (), "count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		"""Given an integer index, returns one of the Actions in the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{90CED626-8D78-11CF-86B4-444553540000}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{90CED626-8D78-11CF-86B4-444553540000}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IAutoPSDoc(DispatchBaseClass):
	"""Automation interface to Photoshop Image documeent"""
	CLSID = IID('{9077D1E1-8959-11CF-86B4-444553540000}')
	coclass_clsid = None

	def Activate(self):
		"""Make this document the current target"""
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (24, 0), (),)

	def Close(self):
		"""Closes and saves this document"""
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (24, 0), (),)

	def SaveTo(self, fileName=defaultNamedNotOptArg):
		"""Save to a different name, but file remains open"""
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), ((8, 1),),fileName
			)

	_prop_map_get_ = {
		"Title": (1610743808, 2, (8, 0), (), "Title", None),
	}
	_prop_map_put_ = {
	}

class IPhotoshopApplication(DispatchBaseClass):
	"""Adobe Photoshop 12.0 Application"""
	CLSID = IID('{9414F179-C905-11D1-92CC-00600808FC44}')
	coclass_clsid = IID('{6DECC242-87EF-11CF-86B4-444553540000}')

	# Result is of type IActionControl
	def MakeControlObject(self):
		"""Creates an IActionControl object."""
		ret = self._oleobj_.InvokeTypes(1610743813, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeControlObject', '{38FB4290-9DF6-11D1-B032-00C04FD7EC47}', UnicodeToString=0)
		return ret

	# Result is of type IActionDescriptor
	def MakeDescriptor(self):
		"""Creates an IActionDescriptor object."""
		ret = self._oleobj_.InvokeTypes(1610743814, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeDescriptor', '{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}', UnicodeToString=0)
		return ret

	# Result is of type IActionList
	def MakeList(self):
		"""Creates an IActionList object."""
		ret = self._oleobj_.InvokeTypes(1610743815, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeList', '{B249C0B0-A004-11D1-B036-00C04FD7EC47}', UnicodeToString=0)
		return ret

	# Result is of type IActionReference
	def MakeReference(self):
		"""Creates an IActionReference object."""
		ret = self._oleobj_.InvokeTypes(1610743816, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeReference', '{B249C0B1-A004-11D1-B036-00C04FD7EC47}', UnicodeToString=0)
		return ret

	# Result is of type IAutoPSDoc
	def Open(self, fileName=defaultNamedNotOptArg):
		"""Opens a Photoshop document."""
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 1, (9, 0), ((8, 1),),fileName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{9077D1E1-8959-11CF-86B4-444553540000}', UnicodeToString=0)
		return ret

	def PlayAction(self, fileName=defaultNamedNotOptArg):
		"""Plays Action by name on active document"""
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (3, 0), ((8, 1),),fileName
			)

	def Quit(self):
		"""Exits the application."""
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Actions' returns object of type 'IActions'
		"Actions": (1610743812, 2, (9, 0), (), "Actions", '{90CED625-8D78-11CF-86B4-444553540000}'),
		"FullName": (1610743808, 2, (8, 0), (), "FullName", None),
		"Visible": (1610743817, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Visible": ((1610743817, LCID, 4, 0),()),
	}

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'Photoshop.Application.12.1'
class PhotoshopApplication(CoClassBaseClass): # A CoClass
	# Photoshop Object Type Information
	CLSID = IID('{6DECC242-87EF-11CF-86B4-444553540000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPhotoshopApplication,
	]
	default_interface = IPhotoshopApplication

IAction_vtables_dispatch_ = 1
IAction_vtables_ = [
	(( 'name' , 'retval' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Play' , ), 1610743809, (1610743809, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

IActionControl_vtables_dispatch_ = 1
IActionControl_vtables_ = [
	(( 'Play' , 'eventID' , 'parameters' , 'dialogOptions' , 'result' , 
			), 1610743808, (1610743808, (), [ (3, 1, None, None) , (9, 1, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , (3, 1, None, None) , (16393, 10, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'GetActionProperty' , 'reference' , 'propertyDesc' , ), 1610743809, (1610743809, (), [ (9, 1, None, "IID('{B249C0B1-A004-11D1-B036-00C04FD7EC47}')") , 
			(16393, 2, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'StringIDToTypeID' , 'stringID' , 'typeID' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'TypeIDToStringID' , 'typeID' , 'stringID' , ), 1610743811, (1610743811, (), [ (3, 1, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

IActionDescriptor_vtables_dispatch_ = 1
IActionDescriptor_vtables_ = [
	(( 'GetType' , 'key' , 'type' , ), 1610743808, (1610743808, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'GetKey' , 'index' , 'key' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'HasKey' , 'key' , 'HasKey' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'GetCount' , 'count' , ), 1610743811, (1610743811, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'IsEqual' , 'otherDesc' , 'IsEqual' , ), 1610743812, (1610743812, (), [ (9, 1, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Erase' , 'key' , ), 1610743813, (1610743813, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 1610743814, (1610743814, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'GetInteger' , 'key' , 'retval' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PutInteger' , 'key' , 'value' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'GetDouble' , 'key' , 'retval' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , 
			(16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PutDouble' , 'key' , 'value' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'GetUnitDouble' , 'key' , 'unitID' , 'retval' , ), 1610743819, (1610743819, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PutUnitDouble' , 'key' , 'unitID' , 'value' , ), 1610743820, (1610743820, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'GetString' , 'key' , 'retval' , ), 1610743821, (1610743821, (), [ (3, 1, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PutString' , 'key' , 'value' , ), 1610743822, (1610743822, (), [ (3, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'GetBoolean' , 'key' , 'retval' , ), 1610743823, (1610743823, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PutBoolean' , 'key' , 'value' , ), 1610743824, (1610743824, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'GetList' , 'key' , 'list' , ), 1610743825, (1610743825, (), [ (3, 1, None, None) , 
			(16393, 2, None, "IID('{B249C0B0-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PutList' , 'key' , 'list' , ), 1610743826, (1610743826, (), [ (3, 1, None, None) , 
			(9, 1, None, "IID('{B249C0B0-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'GetObject' , 'key' , 'classID' , 'retval' , ), 1610743827, (1610743827, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 2, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PutObject' , 'key' , 'classID' , 'value' , ), 1610743828, (1610743828, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (9, 1, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'GetGlobalObject' , 'key' , 'classID' , 'retval' , ), 1610743829, (1610743829, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 2, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PutGlobalObject' , 'key' , 'classID' , 'value' , ), 1610743830, (1610743830, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (9, 1, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'GetEnumerated' , 'key' , 'enumType' , 'value' , ), 1610743831, (1610743831, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PutEnumerated' , 'key' , 'enumType' , 'value' , ), 1610743832, (1610743832, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'GetReference' , 'key' , 'reference' , ), 1610743833, (1610743833, (), [ (3, 1, None, None) , 
			(16393, 2, None, "IID('{B249C0B1-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PutReference' , 'key' , 'reference' , ), 1610743834, (1610743834, (), [ (3, 1, None, None) , 
			(9, 1, None, "IID('{B249C0B1-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'GetClass' , 'key' , 'classID' , ), 1610743835, (1610743835, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PutClass' , 'key' , 'classID' , ), 1610743836, (1610743836, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'GetGlobalClass' , 'key' , 'classID' , ), 1610743837, (1610743837, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PutGlobalClass' , 'key' , 'classID' , ), 1610743838, (1610743838, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'GetPath' , 'key' , 'pathString' , ), 1610743839, (1610743839, (), [ (3, 1, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PutPath' , 'key' , 'pathString' , ), 1610743840, (1610743840, (), [ (3, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'GetDataLength' , 'key' , 'value' , ), 1610743841, (1610743841, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetData' , 'key' , 'retval' , ), 1610743842, (1610743842, (), [ (3, 1, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'PutData' , 'key' , 'value' , ), 1610743843, (1610743843, (), [ (3, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IActionList_vtables_dispatch_ = 1
IActionList_vtables_ = [
	(( 'GetType' , 'index' , 'value' , ), 1610743808, (1610743808, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'GetCount' , 'value' , ), 1610743809, (1610743809, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'GetInteger' , 'index' , 'value' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'PutInteger' , 'value' , ), 1610743811, (1610743811, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'GetDouble' , 'index' , 'value' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , 
			(16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'PutDouble' , 'value' , ), 1610743813, (1610743813, (), [ (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'GetUnitDouble' , 'index' , 'unit' , 'value' , ), 1610743814, (1610743814, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'PutUnitDouble' , 'unit' , 'value' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetString' , 'index' , 'str' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'PutString' , 'str' , ), 1610743817, (1610743817, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetBoolean' , 'index' , 'value' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'PutBoolean' , 'value' , ), 1610743819, (1610743819, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetList' , 'index' , 'actionList' , ), 1610743820, (1610743820, (), [ (3, 1, None, None) , 
			(16393, 2, None, "IID('{B249C0B0-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'PutList' , 'actionList' , ), 1610743821, (1610743821, (), [ (9, 1, None, "IID('{B249C0B0-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetObject' , 'index' , 'type' , 'value' , ), 1610743822, (1610743822, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 2, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'PutObject' , 'type' , 'value' , ), 1610743823, (1610743823, (), [ (3, 1, None, None) , 
			(9, 1, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetGlobalObject' , 'index' , 'type' , 'value' , ), 1610743824, (1610743824, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16393, 2, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'PutGlobalObject' , 'type' , 'value' , ), 1610743825, (1610743825, (), [ (3, 1, None, None) , 
			(9, 1, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetEnumerated' , 'index' , 'type' , 'value' , ), 1610743826, (1610743826, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'PutEnumerated' , 'type' , 'value' , ), 1610743827, (1610743827, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetReference' , 'index' , 'value' , ), 1610743828, (1610743828, (), [ (3, 1, None, None) , 
			(16393, 2, None, "IID('{B249C0B1-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'PutReference' , 'value' , ), 1610743829, (1610743829, (), [ (9, 1, None, "IID('{B249C0B1-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetClass' , 'index' , 'value' , ), 1610743830, (1610743830, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'PutClass' , 'value' , ), 1610743831, (1610743831, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetGlobalClass' , 'index' , 'value' , ), 1610743832, (1610743832, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'PutGlobalClass' , 'value' , ), 1610743833, (1610743833, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetPath' , 'index' , 'pathString' , ), 1610743834, (1610743834, (), [ (3, 1, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'PutPath' , 'pathString' , ), 1610743835, (1610743835, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GetDataLength' , 'index' , 'value' , ), 1610743836, (1610743836, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'GetData' , 'index' , 'value' , ), 1610743837, (1610743837, (), [ (3, 1, None, None) , 
			(16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PutData' , 'length' , 'value' , ), 1610743838, (1610743838, (), [ (3, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
]

IActionReference_vtables_dispatch_ = 1
IActionReference_vtables_ = [
	(( 'GetForm' , 'value' , ), 1610743808, (1610743808, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'GetDesiredClass' , 'value' , ), 1610743809, (1610743809, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'PutClass' , 'desiredClass' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'GetName' , 'name' , ), 1610743811, (1610743811, (), [ (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'PutName' , 'desiredClass' , 'name' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'GetIndex' , 'value' , ), 1610743813, (1610743813, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'PutIndex' , 'desiredClass' , 'value' , ), 1610743814, (1610743814, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'GetIdentifier' , 'value' , ), 1610743815, (1610743815, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PutIdentifier' , 'desiredClass' , 'value' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'GetOffset' , 'value' , ), 1610743817, (1610743817, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PutOffset' , 'desiredClass' , 'value' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'GetEnumerated' , 'type' , 'enumValue' , ), 1610743819, (1610743819, (), [ (16387, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PutEnumerated' , 'desiredClass' , 'type' , 'value' , ), 1610743820, (1610743820, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'GetProperty' , 'value' , ), 1610743821, (1610743821, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PutProperty' , 'desiredClass' , 'value' , ), 1610743822, (1610743822, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'GetContainer' , 'value' , ), 1610743823, (1610743823, (), [ (16393, 2, None, "IID('{B249C0B1-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IActions_vtables_dispatch_ = 1
IActions_vtables_ = [
	(( 'count' , 'retval' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{90CED626-8D78-11CF-86B4-444553540000}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 1 , )),
]

IAutoPSDoc_vtables_dispatch_ = 1
IAutoPSDoc_vtables_ = [
	(( 'Title' , 'retval' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Close' , ), 1610743809, (1610743809, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'SaveTo' , 'fileName' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 1610743811, (1610743811, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

IPhotoshopApplication_vtables_dispatch_ = 1
IPhotoshopApplication_vtables_ = [
	(( 'FullName' , 'retval' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Quit' , ), 1610743809, (1610743809, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Open' , 'fileName' , 'retval' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{9077D1E1-8959-11CF-86B4-444553540000}')") , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'PlayAction' , 'fileName' , 'retval' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Actions' , 'retval' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{90CED625-8D78-11CF-86B4-444553540000}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'MakeControlObject' , 'retval' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{38FB4290-9DF6-11D1-B032-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'MakeDescriptor' , 'retval' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'MakeList' , 'retval' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{B249C0B0-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MakeReference' , 'retval' , ), 1610743816, (1610743816, (), [ (16393, 10, None, "IID('{B249C0B1-A004-11D1-B036-00C04FD7EC47}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'isVisible' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'isVisible' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{38FB4290-9DF6-11D1-B032-00C04FD7EC47}' : IActionControl,
	'{6DECC242-87EF-11CF-86B4-444553540000}' : PhotoshopApplication,
	'{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}' : IActionDescriptor,
	'{9077D1E1-8959-11CF-86B4-444553540000}' : IAutoPSDoc,
	'{B249C0B1-A004-11D1-B036-00C04FD7EC47}' : IActionReference,
	'{B249C0B0-A004-11D1-B036-00C04FD7EC47}' : IActionList,
	'{90CED625-8D78-11CF-86B4-444553540000}' : IActions,
	'{90CED626-8D78-11CF-86B4-444553540000}' : IAction,
	'{9414F179-C905-11D1-92CC-00600808FC44}' : IPhotoshopApplication,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{38FB4290-9DF6-11D1-B032-00C04FD7EC47}' : 'IActionControl',
	'{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}' : 'IActionDescriptor',
	'{9077D1E1-8959-11CF-86B4-444553540000}' : 'IAutoPSDoc',
	'{B249C0B1-A004-11D1-B036-00C04FD7EC47}' : 'IActionReference',
	'{B249C0B0-A004-11D1-B036-00C04FD7EC47}' : 'IActionList',
	'{90CED625-8D78-11CF-86B4-444553540000}' : 'IActions',
	'{90CED626-8D78-11CF-86B4-444553540000}' : 'IAction',
	'{9414F179-C905-11D1-92CC-00600808FC44}' : 'IPhotoshopApplication',
}


NamesToIIDMap = {
	'IActionReference' : '{B249C0B1-A004-11D1-B036-00C04FD7EC47}',
	'IActionControl' : '{38FB4290-9DF6-11D1-B032-00C04FD7EC47}',
	'IActionList' : '{B249C0B0-A004-11D1-B036-00C04FD7EC47}',
	'IActions' : '{90CED625-8D78-11CF-86B4-444553540000}',
	'IActionDescriptor' : '{7CA9DE40-9EB3-11D1-B033-00C04FD7EC47}',
	'IAutoPSDoc' : '{9077D1E1-8959-11CF-86B4-444553540000}',
	'IAction' : '{90CED626-8D78-11CF-86B4-444553540000}',
	'IPhotoshopApplication' : '{9414F179-C905-11D1-92CC-00600808FC44}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

