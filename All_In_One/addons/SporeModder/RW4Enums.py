# intIdentifier, argType, default value, (range)

D3DBOOLEAN = {
    'FALSE': 0,
    'TRUE': 1
}
D3DZBUFFERTYPE = {
    'D3DZB_FALSE': 0,
    'D3DZB_TRUE': 1,
    'D3DZB_USEW': 2,
    'D3DZB_FORCE_DWORD': 0x7fffffff
}
D3DFILLMODE = {
    'D3DFILL_POINT': 1,
    'D3DFILL_WIREFRAME': 2,
    'D3DFILL_SOLID': 3,
    'D3DFILL_FORCE_DWORD': 0x7fffffff
}
D3DSHADEMODE = {
    'D3DSHADE_FLAT': 1,
    'D3DSHADE_GOURAUD': 2,
    'D3DSHADE_PHONG': 3,
    'D3DSHADE_FORCE_DWORD': 0x7fffffff
}
D3DBLEND = {
    'D3DBLEND_ZERO': 1,
    'D3DBLEND_ONE': 2,
    'D3DBLEND_SRCCOLOR': 3,
    'D3DBLEND_INVSRCCOLOR': 4,
    'D3DBLEND_SRCALPHA': 5,
    'D3DBLEND_INVSRCALPHA': 6,
    'D3DBLEND_DESTALPHA': 7,
    'D3DBLEND_INVDESTALPHA': 8,
    'D3DBLEND_DESTCOLOR': 9,
    'D3DBLEND_INVDESTCOLOR': 10,
    'D3DBLEND_SRCALPHASAT': 11,
    'D3DBLEND_BOTHSRCALPHA': 12,
    'D3DBLEND_BOTHINVSRCALPHA': 13,
    'D3DBLEND_BLENDFACTOR': 14,
    'D3DBLEND_INVBLENDFACTOR': 15,
    'D3DBLEND_SRCCOLOR2': 16,
    'D3DBLEND_INVSRCCOLOR2': 17,
    'D3DBLEND_FORCE_DWORD': 0x7fffffff
}
D3DCULL = {
  'D3DCULL_NONE'         : 1,
  'D3DCULL_CW'           : 2,
  'D3DCULL_CCW'          : 3,
  'D3DCULL_FORCE_DWORD'  : 0x7fffffff
}
D3DCMPFUNC = {
    'D3DCMP_NEVER': 1,
    'D3DCMP_LESS': 2,
    'D3DCMP_EQUAL': 3,
    'D3DCMP_LESSEQUAL': 4,
    'D3DCMP_GREATER': 5,
    'D3DCMP_NOTEQUAL': 6,
    'D3DCMP_GREATEREQUAL': 7,
    'D3DCMP_ALWAYS': 8,
    'D3DCMP_FORCE_DWORD': 0x7fffffff
}
D3DFOGMODE = {
  'D3DFOG_NONE'         : 0,
  'D3DFOG_EXP'          : 1,
  'D3DFOG_EXP2'         : 2,
  'D3DFOG_LINEAR'       : 3,
  'D3DFOG_FORCE_DWORD'  : 0x7fffffff
}
D3DSTENCILOP = {
  'D3DSTENCILOP_KEEP'         : 1,
  'D3DSTENCILOP_ZERO'         : 2,
  'D3DSTENCILOP_REPLACE'      : 3,
  'D3DSTENCILOP_INCRSAT'      : 4,
  'D3DSTENCILOP_DECRSAT'      : 5,
  'D3DSTENCILOP_INVERT'       : 6,
  'D3DSTENCILOP_INCR'         : 7,
  'D3DSTENCILOP_DECR'         : 8,
  'D3DSTENCILOP_FORCE_DWORD'  : 0x7fffffff
}
D3DWRAPCOORD = {
    'NONE': 0,
    'D3DWRAPCOORD_0': 1,
    'D3DWRAPCOORD_1': 2,
    'D3DWRAPCOORD_2': 4,
    'D3DWRAPCOORD_3': 8,
}
D3DMATERIALCOLORSOURCE = {
  'D3DMCS_MATERIAL'     : 0,
  'D3DMCS_COLOR1'       : 1,
  'D3DMCS_COLOR2'       : 2,
  'D3DMCS_FORCE_DWORD'  : 0x7fffffff
}
D3DVERTEXBLENDFLAGS = {
  'D3DVBF_DISABLE'   : 0,
  'D3DVBF_1WEIGHTS'  : 1,
  'D3DVBF_2WEIGHTS'  : 2,
  'D3DVBF_3WEIGHTS'  : 3,
  'D3DVBF_TWEENING'  : 255,
  'D3DVBF_0WEIGHTS'  : 256
}
D3DPATCHEDGESTYLE = {
  'D3DPATCHEDGE_DISCRETE'     : 0,
  'D3DPATCHEDGE_CONTINUOUS'   : 1,
  'D3DPATCHEDGE_FORCE_DWORD'  : 0x7fffffff
}
D3DDEBUGMONITORTOKENS = {
  'D3DDMT_ENABLE'       : 0,
  'D3DDMT_DISABLE'      : 1,
  'D3DDMT_FORCE_DWORD'  : 0x7fffffff
}
D3DBLENDOP = {
  'D3DBLENDOP_ADD'          : 1,
  'D3DBLENDOP_SUBTRACT'     : 2,
  'D3DBLENDOP_REVSUBTRACT'  : 3,
  'D3DBLENDOP_MIN'          : 4,
  'D3DBLENDOP_MAX'          : 5,
  'D3DBLENDOP_FORCE_DWORD'  : 0x7fffffff
}
D3DDEGREETYPE = {
  'D3DDEGREE_LINEAR'     : 1,
  'D3DDEGREE_QUADRATIC'  : 2,
  'D3DDEGREE_CUBIC'      : 3,
  'D3DDEGREE_QUINTIC'    : 5,
  'D3DCULL_FORCE_DWORD'  : 0x7fffffff
}

D3DRENDERSTATETYPE = {
    'D3DRS_ZENABLE': (7, D3DZBUFFERTYPE, 'D3DZB_FALSE'),
    'D3DRS_FILLMODE': (8, D3DFILLMODE, 'D3DFILL_SOLID'),
    'D3DRS_SHADEMODE': (9, D3DSHADEMODE, 'D3DSHADE_GOURAUD'),
    'D3DRS_ZWRITEENABLE': (14, D3DBOOLEAN, 'TRUE'),
    'D3DRS_ALPHATESTENABLE': (15, D3DBOOLEAN, 'FALSE'),
    'D3DRS_LASTPIXEL': (16, D3DBOOLEAN, 'TRUE'),
    'D3DRS_SRCBLEND': (19, D3DBLEND, 'D3DBLEND_ONE'),
    'D3DRS_DESTBLEND': (20, D3DBLEND, 'D3DBLEND_ZERO'),
    'D3DRS_CULLMODE': (22, D3DCULL, 'D3DCULL_CCW'),
    'D3DRS_ZFUNC': (23, D3DCMPFUNC, 'D3DCMP_LESSEQUAL'),
    'D3DRS_ALPHAREF': (24, int, 0, (0, 0xff)),
    'D3DRS_ALPHAFUNC': (25, D3DCMPFUNC, 'D3DCMP_ALWAYS'),
    'D3DRS_DITHERENABLE': (26, D3DBOOLEAN, 'FALSE'),
    'D3DRS_ALPHABLENDENABLE': (27, D3DBOOLEAN, 'FALSE'),
    'D3DRS_FOGENABLE': (28, D3DBOOLEAN, 'FALSE'),
    'D3DRS_SPECULARENABLE': (29, D3DBOOLEAN, 'FALSE'),
    'D3DRS_FOGCOLOR': (34, 'COLOR', 0),
    'D3DRS_FOGTABLEMODE': (35, D3DFOGMODE, 'D3DFOG_NONE'),
    'D3DRS_FOGSTART': (36, float, 0.0, (0.0, 1.0)),  # range
    'D3DRS_FOGEND': (37, float, 1.0, (0.0, 1.0)),  # range
    'D3DRS_FOGDENSITY': (38, float, 1.0, (0.0, 1.0)),
    'D3DRS_RANGEFOGENABLE': (48, D3DBOOLEAN, 'FALSE'),
    'D3DRS_STENCILENABLE': (52, D3DBOOLEAN, 'FALSE'),
    'D3DRS_STENCILFAIL': (53, D3DSTENCILOP, 'D3DSTENCILOP_KEEP'),
    'D3DRS_STENCILZFAIL': (54, D3DSTENCILOP, 'D3DSTENCILOP_KEEP'),
    'D3DRS_STENCILPASS': (55, D3DSTENCILOP, 'D3DSTENCILOP_KEEP'),
    'D3DRS_STENCILFUNC': (56, D3DCMPFUNC, 'D3DCMP_ALWAYS'),
    'D3DRS_STENCILREF': (57, int, 0),
    'D3DRS_STENCILMASK': (58, int, 0xFFFFFFFF),
    'D3DRS_STENCILWRITEMASK': (59, int, 0xFFFFFFFF),
    'D3DRS_TEXTUREFACTOR': (60, 'COLOR', 0xFFFFFFFF),
    'D3DRS_WRAP0': (128, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP1': (129, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP2': (130, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP3': (131, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP4': (132, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP5': (133, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP6': (134, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP7': (135, D3DWRAPCOORD, 'NONE'),
    'D3DRS_CLIPPING': (136, D3DBOOLEAN, 'TRUE'),
    'D3DRS_LIGHTING': (137, D3DBOOLEAN, 'TRUE'),
    'D3DRS_AMBIENT': (139, 'COLOR', 0),
    'D3DRS_FOGVERTEXMODE': (140, D3DFOGMODE, 'D3DFOG_NONE'),
    'D3DRS_COLORVERTEX': (141, D3DBOOLEAN, 'TRUE'),
    'D3DRS_LOCALVIEWER': (142, D3DBOOLEAN, 'TRUE'),
    'D3DRS_NORMALIZENORMALS': (143, D3DBOOLEAN, 'FALSE'),
    'D3DRS_DIFFUSEMATERIALSOURCE': (145, D3DMATERIALCOLORSOURCE, 'D3DMCS_COLOR1'),
    'D3DRS_SPECULARMATERIALSOURCE': (146, D3DMATERIALCOLORSOURCE, 'D3DMCS_COLOR2'),
    'D3DRS_AMBIENTMATERIALSOURCE': (147, D3DMATERIALCOLORSOURCE, 'D3DMCS_MATERIAL'),
    'D3DRS_EMISSIVEMATERIALSOURCE': (148, D3DMATERIALCOLORSOURCE, 'D3DMCS_MATERIAL'),
    'D3DRS_VERTEXBLEND': (151, D3DVERTEXBLENDFLAGS, 'D3DVBF_DISABLE'),
    'D3DRS_CLIPPLANEENABLE': (152, int, 0),  # bit mask
    'D3DRS_POINTSIZE': (154, float, 0),
    'D3DRS_POINTSIZE_MIN': (155, float, 1.0),
    'D3DRS_POINTSPRITEENABLE': (156, D3DBOOLEAN, 'FALSE'),
    'D3DRS_POINTSCALEENABLE': (157, D3DBOOLEAN, 'FALSE'),
    'D3DRS_POINTSCALE_A': (158, float, 1.0),
    'D3DRS_POINTSCALE_B': (159, float, 0.0),
    'D3DRS_POINTSCALE_C': (160, float, 0.0),
    'D3DRS_MULTISAMPLEANTIALIAS': (161, D3DBOOLEAN, 'TRUE'),
    'D3DRS_MULTISAMPLEMASK': (162, int, 0xFFFFFFFF),
    'D3DRS_PATCHEDGESTYLE': (163, D3DPATCHEDGESTYLE, 'D3DPATCHEDGE_DISCRETE'),
    'D3DRS_DEBUGMONITORTOKEN': (165, D3DDEBUGMONITORTOKENS, 'D3DDMT_ENABLE'),
    'D3DRS_POINTSIZE_MAX': (166, float, 64.0),
    'D3DRS_INDEXEDVERTEXBLENDENABLE': (167, D3DBOOLEAN, 'FALSE'),
    'D3DRS_COLORWRITEENABLE': (168, int, 0x0000000F),
    'D3DRS_TWEENFACTOR': (170, float, 0.0),
    'D3DRS_BLENDOP': (171, D3DBLENDOP, 'D3DBLENDOP_ADD'),
    'D3DRS_POSITIONDEGREE': (172, D3DDEGREETYPE, 'D3DDEGREE_CUBIC'),
    'D3DRS_NORMALDEGREE': (173, D3DDEGREETYPE, 'D3DDEGREE_LINEAR'),
    'D3DRS_SCISSORTESTENABLE': (174, D3DBOOLEAN, 'FALSE'),
    'D3DRS_SLOPESCALEDEPTHBIAS': (175, float, 0.0),
    'D3DRS_ANTIALIASEDLINEENABLE': (176, D3DBOOLEAN, 'FALSE'),
    'D3DRS_MINTESSELLATIONLEVEL': (178, float, 1.0),
    'D3DRS_MAXTESSELLATIONLEVEL': (179, float, 1.0),
    'D3DRS_ADAPTIVETESS_X': (180, float, 0.0),
    'D3DRS_ADAPTIVETESS_Y': (181, float, 0.0),
    'D3DRS_ADAPTIVETESS_Z': (182, float, 1.0),
    'D3DRS_ADAPTIVETESS_W': (183, float, 0.0),
    'D3DRS_ENABLEADAPTIVETESSELLATION': (184, D3DBOOLEAN, 'FALSE'),
    'D3DRS_TWOSIDEDSTENCILMODE': (185, D3DBOOLEAN, 'FALSE'),
    'D3DRS_CCW_STENCILFAIL': (186, D3DSTENCILOP, 'D3DSTENCILOP_KEEP'),
    'D3DRS_CCW_STENCILZFAIL': (187, D3DSTENCILOP, 'D3DSTENCILOP_KEEP'),
    'D3DRS_CCW_STENCILPASS': (188, D3DSTENCILOP, 'D3DSTENCILOP_KEEP'),
    'D3DRS_CCW_STENCILFUNC': (189, D3DCMPFUNC, 'D3DCMP_ALWAYS'),
    'D3DRS_COLORWRITEENABLE1': (190, int, 0x0000000f),
    'D3DRS_COLORWRITEENABLE2': (191, int, 0x0000000f),
    'D3DRS_COLORWRITEENABLE3': (192, int, 0x0000000f),
    'D3DRS_BLENDFACTOR': (193, 'COLOR', 0xffffffff),
    'D3DRS_SRGBWRITEENABLE': (194, int, 0),  # ?
    'D3DRS_DEPTHBIAS': (195, float, 0.0),
    'D3DRS_WRAP8': (198, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP9': (199, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP10': (200, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP11': (201, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP12': (202, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP13': (203, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP14': (204, D3DWRAPCOORD, 'NONE'),
    'D3DRS_WRAP15': (205, D3DWRAPCOORD, 'NONE'),
    'D3DRS_SEPARATEALPHABLENDENABLE': (206, D3DBOOLEAN, 'FALSE'),
    'D3DRS_SRCBLENDALPHA': (207, D3DBLEND, 'D3DBLEND_ONE'),
    'D3DRS_DESTBLENDALPHA': (208, D3DBLEND, 'D3DBLEND_ZERO'),
    'D3DRS_BLENDOPALPHA': (209, D3DBLENDOP, 'D3DBLENDOP_ADD'),
    # 'D3DRS_FORCE_DWORD': 0x7fffffff
}


D3DTEXTUREOP = {
    'D3DTOP_DISABLE': 1,
    'D3DTOP_SELECTARG1': 2,
    'D3DTOP_SELECTARG2': 3,
    'D3DTOP_MODULATE': 4,
    'D3DTOP_MODULATE2X': 5,
    'D3DTOP_MODULATE4X': 6,
    'D3DTOP_ADD': 7,
    'D3DTOP_ADDSIGNED': 8,
    'D3DTOP_ADDSIGNED2X': 9,
    'D3DTOP_SUBTRACT': 10,
    'D3DTOP_ADDSMOOTH': 11,
    'D3DTOP_BLENDDIFFUSEALPHA': 12,
    'D3DTOP_BLENDTEXTUREALPHA': 13,
    'D3DTOP_BLENDFACTORALPHA': 14,
    'D3DTOP_BLENDTEXTUREALPHAPM': 15,
    'D3DTOP_BLENDCURRENTALPHA': 16,
    'D3DTOP_PREMODULATE': 17,
    'D3DTOP_MODULATEALPHA_ADDCOLOR': 18,
    'D3DTOP_MODULATECOLOR_ADDALPHA': 19,
    'D3DTOP_MODULATEINVALPHA_ADDCOLOR': 20,
    'D3DTOP_MODULATEINVCOLOR_ADDALPHA': 21,
    'D3DTOP_BUMPENVMAP': 22,
    'D3DTOP_BUMPENVMAPLUMINANCE': 23,
    'D3DTOP_DOTPRODUCT3': 24,
    'D3DTOP_MULTIPLYADD': 25,
    'D3DTOP_LERP': 26,
    'D3DTOP_FORCE_DWORD': 0x7fffffff
}
D3DTA = {
    'D3DTA_SELECTMASK'        : 0x0000000f,  # mask for arg selector
    'D3DTA_DIFFUSE'           : 0x00000000,  # select diffuse color (read only)
    'D3DTA_CURRENT'           : 0x00000001,  # select stage destination register (read/write)
    'D3DTA_TEXTURE'           : 0x00000002,  # select texture color (read only)
    'D3DTA_TFACTOR'           : 0x00000003,  # select D3DRS_TEXTUREFACTOR (read only)
    'D3DTA_SPECULAR'          : 0x00000004,  # select specular color (read only)
    'D3DTA_TEMP'              : 0x00000005,  # select temporary register color (read/write)
    'D3DTA_CONSTANT'          : 0x00000006,  # select texture stage constant
    'D3DTA_COMPLEMENT'        : 0x00000010,  # take 1.0 - x (read modifier)
    'D3DTA_ALPHAREPLICATE'    : 0x00000020  # replicate alpha to color components (read modifier)
}
D3DTEXTURETRANSFORMFLAGS = {
    'D3DTTFF_DISABLE'      : 0,
    'D3DTTFF_COUNT1'       : 1,
    'D3DTTFF_COUNT2'       : 2,
    'D3DTTFF_COUNT3'       : 3,
    'D3DTTFF_COUNT4'       : 4,
    'D3DTTFF_PROJECTED'    : 256,
    'D3DTTFF_FORCE_DWORD'  : 0x7fffffff
}

D3DTEXTURESTAGESTATETYPE = {
    'D3DTSS_COLOROP': (1, D3DTEXTUREOP, 'D3DTOP_DISABLE'),
    'D3DTSS_COLORARG1': (2, D3DTA, 'D3DTA_TEXTURE'),
    'D3DTSS_COLORARG2': (3, D3DTA, 'D3DTA_CURRENT'),
    'D3DTSS_ALPHAOP': (4, D3DTEXTUREOP, 'D3DTOP_DISABLE'),
    'D3DTSS_ALPHAARG1': (5, D3DTA, 'D3DTA_TEXTURE'),
    'D3DTSS_ALPHAARG2': (6, D3DTA, 'D3DTA_CURRENT'),
    'D3DTSS_BUMPENVMAT00': (7, float, 0.0),
    'D3DTSS_BUMPENVMAT01': (8, float, 0.0),
    'D3DTSS_BUMPENVMAT10': (9, float, 0.0),
    'D3DTSS_BUMPENVMAT11': (10, float, 0.0),
    'D3DTSS_TEXCOORDINDEX': (11, int, 0),
    'D3DTSS_BUMPENVLSCALE': (22, float, 0.0),
    'D3DTSS_BUMPENVLOFFSET': (23, float, 0.0),
    'D3DTSS_TEXTURETRANSFORMFLAGS': (24, D3DTEXTURETRANSFORMFLAGS, 'D3DTTFF_DISABLE'),
    'D3DTSS_COLORARG0': (26, D3DTA, 'D3DTA_CURRENT'),
    'D3DTSS_ALPHAARG0': (27, D3DTA, 'D3DTA_CURRENT'),
    'D3DTSS_RESULTARG': (28, D3DTA, 'D3DTA_CURRENT'),
    'D3DTSS_CONSTANT': (32, D3DTA, 'D3DTA_CONSTANT'),
    #'D3DTSS_FORCE_DWORD': 0x7fffffff
}

D3DTEXTUREADDRESS = {
    'D3DTADDRESS_WRAP'         : 1,
    'D3DTADDRESS_MIRROR'       : 2,
    'D3DTADDRESS_CLAMP'        : 3,
    'D3DTADDRESS_BORDER'       : 4,
    'D3DTADDRESS_MIRRORONCE'   : 5,
    'D3DTADDRESS_FORCE_DWORD'  : 0x7fffffff
}
D3DTEXTUREFILTERTYPE = {
    'D3DTEXF_NONE'             : 0,
    'D3DTEXF_POINT'            : 1,
    'D3DTEXF_LINEAR'           : 2,
    'D3DTEXF_ANISOTROPIC'      : 3,
    'D3DTEXF_PYRAMIDALQUAD'    : 6,
    'D3DTEXF_GAUSSIANQUAD'     : 7,
    'D3DTEXF_CONVOLUTIONMONO'  : 8,
    'D3DTEXF_FORCE_DWORD'      : 0x7fffffff
}

D3DSAMPLERSTATETYPE = {
    'D3DSAMP_ADDRESSU'       : (1, D3DTEXTUREADDRESS, 'D3DTADDRESS_WRAP'),
    'D3DSAMP_ADDRESSV'       : (2, D3DTEXTUREADDRESS, 'D3DTADDRESS_WRAP'),
    'D3DSAMP_ADDRESSW'       : (3, D3DTEXTUREADDRESS, 'D3DTADDRESS_WRAP'),
    'D3DSAMP_BORDERCOLOR'    : (4, 'COLOR', 0),
    'D3DSAMP_MAGFILTER'      : (5, D3DTEXTUREFILTERTYPE, 'D3DTEXF_POINT'),
    'D3DSAMP_MINFILTER'      : (6, D3DTEXTUREFILTERTYPE, 'D3DTEXF_POINT'),
    'D3DSAMP_MIPFILTER'      : (7, D3DTEXTUREFILTERTYPE, 'D3DTEXF_NONE'),
    'D3DSAMP_MIPMAPLODBIAS'  : (8, int, 0),
    'D3DSAMP_MAXMIPLEVEL'    : (9, int, 0),
    'D3DSAMP_MAXANISOTROPY'  : (10, int, 1),
    'D3DSAMP_SRGBTEXTURE'    : (11, int, 0),
    'D3DSAMP_ELEMENTINDEX'   : (12, int, 0),
    'D3DSAMP_DMAPOFFSET'     : (13, int, 0),
    #'D3DSAMP_FORCE_DWORD'    : 0x7fffffff
}

DefaultMaterialRender_NoAlpha = [
    ('D3DRS_ZWRITEENABLE', 'TRUE'),
    ('D3DRS_ALPHATESTENABLE', 'FALSE'),
    ('D3DRS_CULLMODE', 'D3DCULL_CW'),
    ('D3DRS_ZFUNC', 'D3DCMP_LESSEQUAL'),
    ('D3DRS_ALPHABLENDENABLE', 'FALSE')
]
DefaultMaterialRender_Alpha = [
    ('D3DRS_ZWRITEENABLE', 'TRUE'),
    ('D3DRS_ALPHATESTENABLE', 'TRUE'),
    ('D3DRS_SRCBLEND', 'D3DBLEND_SRCALPHA'),
    ('D3DRS_DESTBLEND', 'D3DBLEND_INVSRCALPHA'),
    ('D3DRS_CULLMODE', 'D3DCULL_CW'),
    ('D3DRS_ZFUNC', 'D3DCMP_LESSEQUAL'),
    ('D3DRS_ALPHAREF', 0),
    ('D3DRS_ALPHAFUNC', 'D3DCMP_GREATER'),
    ('D3DRS_ALPHABLENDENABLE', 'TRUE'),
]
DefaultMaterialRender_ExcludingAlpha = [
    ('D3DRS_ZWRITEENABLE', 'TRUE'),
    ('D3DRS_ALPHATESTENABLE', 'TRUE'),
    ('D3DRS_CULLMODE', 'D3DCULL_CW'),
    ('D3DRS_ZFUNC', 'D3DCMP_LESSEQUAL'),
    ('D3DRS_ALPHAREF', 127),
    ('D3DRS_ALPHAFUNC', 'D3DCMP_GREATER'),
    ('D3DRS_ALPHABLENDENABLE', 'FALSE'),
    ('D3DRS_FOGENABLE', 'FALSE')
]

# Are we going to use this?
DefaultMaterialsRenderStates = {
    'SKINPAINT': DefaultMaterialRender_NoAlpha,
    'BUILDDYN': DefaultMaterialRender_NoAlpha,
    'GAMEMODEL_ALPHA': DefaultMaterialRender_Alpha,
    'GAMEMODEL': DefaultMaterialRender_NoAlpha,
    'NO_MATERIAL': DefaultMaterialRender_Alpha,
}

DefaultTextureStageStates = [
    ('D3DTSS_COLOROP', 'D3DTOP_MODULATE'),
    ('D3DTSS_COLORARG1', 'D3DTA_TEXTURE'),
    ('D3DTSS_COLORARG2', 'D3DTA_DIFFUSE'),
    ('D3DTSS_ALPHAOP', 'D3DTOP_MODULATE'),
    ('D3DTSS_ALPHAARG1', 'D3DTA_TEXTURE'),
    ('D3DTSS_ALPHAARG2', 'D3DTA_DIFFUSE')
]
DefaultSamplerStates = [
    ('D3DSAMP_ADDRESSU', 'D3DTADDRESS_WRAP'),
    ('D3DSAMP_ADDRESSV', 'D3DTADDRESS_WRAP'),
    ('D3DSAMP_MAGFILTER', 'D3DTEXF_LINEAR'),
    ('D3DSAMP_MINFILTER', 'D3DTEXF_LINEAR'),
    ('D3DSAMP_MIPFILTER', 'D3DTEXF_POINT')
]


def setStateValue(prop, state, stateEnum):
    prop.PropertyName = state[0]
    # print(stateEnum)
    if stateEnum[1] == int:
        # print(state[1])
        prop.PropertyValueInt = state[1]
    elif stateEnum[1] == float:
        prop.PropertyValueFloat = state[1]
    elif stateEnum[1] == 'COLOR':
        prop.PropertyValueColor = state[1]
    else:
        prop.PropertyValueEnum = state[1]
        # prop.EnumPropertyToSet = state[1]


def generateDefaultStates(material, stateType, generateType=None):
    if stateType == "RENDER":
        material.RenderStateProperties.clear()
        if generateType == "ALPHA":
            states = DefaultMaterialRender_Alpha
        elif generateType == "EXCLUDING":
            states = DefaultMaterialRender_ExcludingAlpha
        else:
            states = DefaultMaterialRender_NoAlpha

        for s in states:
            setStateValue(material.RenderStateProperties.add(), s, D3DRENDERSTATETYPE[s[0]])

    elif stateType == 'TEXTURE':
        material.TextureStateProperties.clear()
        for s in DefaultTextureStageStates:
            setStateValue(material.TextureStateProperties.add(), s,
                          D3DTEXTURESTAGESTATETYPE[s[0]])
    else:
        material.SamplerStateProperties.clear()
        for s in DefaultSamplerStates:
            setStateValue(material.SamplerStateProperties.add(), s,
                          D3DSAMPLERSTATETYPE[s[0]])