
INPUT_FILE = 'data/vip_ebm_bc_rh_20190502.csv'

OUTPUT_FOLDER = 'output/vip_ebm_purple4_rh'

# either pial (with gyri/sulci) or inflated (smooth)
BRAIN_TYPE = 'pial'

# either cortical or subcortical
IMG_TYPE = 'cortical'

# what colours to use for showing brain pathology
# e.g. if the range of pathology is [0,3],
# then you need four colors (the first one is for pathology 0, i.e. no pathology)
# a pathology at 1.3 will interpolate between the second and third color
COLORS_RGB = [(1,1,1), (0.87,0.63,0.87), (0.58,0.44,0.86), (0.5,0,0.5)] # white -> plum -> medium purple -> purple
#COLORS_RGB = [(1,1,1), (1,1,0), (1,0.4,0), (1,0,0)] # white -> yellow -> orange -> red
# COLORS_RGB = [(1,1,1), (1,0,0), (1,0,0), (1,0,0)] # white -> red -> red -> red

# output image resolution for X,Y in pixels
RESOLUTION = (1200, 900)

# default is white
BACKGROUND_COLOR = (1,1,1)

# to change camera viewing angle and other advanced settings, look into blendHelper.py:setCamera()
# for luminosity settings, look into blendHelper.py:setLamp()

# map the names of each 3D cortical structure to be coloured to the name of the structure you have in your atlas.
# only change the right-hand side values, as the left-hand side are used by blender.
#cortAreasIndexMap = {'superiorfrontal': -1,
#  'posteriorcingulate': -1,
#  'caudalanteriorcingulate': -1,
#  'frontalpole': -1,
#  'rostralanteriorcingulate': -1,
#  'precentral': 'precentral',
#  'lingual': -1,
#  'parsorbitalis': -1,
#  'insula': -1,
#  'transversetemporal': 'planum temporale',
#  'parsopercularis': 'central operculum',
#  'supramarginal': 'supramarginal',
#  'pericalcarine': -1,
#  'lateraloccipital': -1,
#  'unknown': -1,
#  'isthmuscingulate': -1,
#  'cuneus': -1,
#  'paracentral': -1,
#  'medialorbitofrontal': -1,
#  'fusiform': -1,
#  'postcentral': -1,
#  'superiorparietal': 'superior parietal',
#  'inferiortemporal': -1,
#  'lateralorbitofrontal': -1,
#  'precuneus': -1,
#  'rostralmiddlefrontal': -1,
#  'parahippocampal': -1,
#  'caudalmiddlefrontal': -1,
#  'middletemporal': 'middle temporal',
#  'bankssts': -1,
#  'parstriangularis': 'angular',
#  'temporalpole': -1,
#  'superiortemporal': 'superior temporal',
#  'entorhinal': -1,
#  'inferiorparietal': -1}
cortAreasIndexMap = {'bankssts': -1,
 'caudalanteriorcingulate': 'anterior cingulate',
 'caudalmiddlefrontal': -1,
 'cuneus': -1,
 'entorhinal': -1,
 'frontalpole': -1,
 'fusiform': -1,
 'inferiorparietal': -1,
 'inferiortemporal': -1,
 'insula': -1,
 'isthmuscingulate': 'posterior cingulate',
 'lateraloccipital': -1,
 'lateralorbitofrontal': -1,
 'lingual': -1,
 'medialorbitofrontal': -1,
 'middletemporal': 'middle temporal',
 'paracentral': -1,
 'parahippocampal': -1,
 'parsopercularis': -1,
 'parsorbitalis': -1,
 'parstriangularis': 'angular',
 'pericalcarine': -1,
 'postcentral': 'postcentral',
 'posteriorcingulate': -1,
 'precentral': 'precentral',
 'precuneus': -1,
 'rostralanteriorcingulate': -1,
 'rostralmiddlefrontal': -1,
 'superiorfrontal': 'superior frontal',
 'superiorparietal': 'superior parietal',
 'superiortemporal': -1,
 'supramarginal': -1,
 'temporalpole': -1,
 'transversetemporal': -1,
 'unknown': -1}

# do the same map for subcortical
# only change the right-hand side values
subcortAreasIndexMap = {
  'Left-Accumbens-area':'accumbens', # -1 means do not colour this region
  'Left-Caudate':'caudate',
  'Left-Cerebellum-White-Matter':-1,
  'Left-Inf-Lat-Vent':-1,
  'Left-Pallidum':'pallidum',
  'Left-Thalamus-Proper':'thalamus',
  'Left-Amygdala':'amygdala',
  'Left-Cerebellum-Cortex':-1,
  'Left-Hippocampus':'hippocampus',
  'Left-Lateral-Ventricle':-1,
  'Left-Putamen':'putamen',
  'Left-VentralDC':'ventral dc'}
