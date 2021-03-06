from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist


mesh = Mesh.from_json('cablenet.json')

fabric = mesh.copy()
fabric.name = 'fabric'

# make a lookup dict for the vertex normals of the mesh vertices


for key, attr in fabric.vertices(True):
    nx, ny, nz = key_normal[key]

    # update the attributes of the fabric vertices
    # to be offset in the normal direction by 2cm

fabric.to_json('fabric.json')

artist = MeshArtist(fabric, layer="Fabric")

# clear the "Fabric" layer
# draw the fabric as a mesh
# specify a color for the mesh
