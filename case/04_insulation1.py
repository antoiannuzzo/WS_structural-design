from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas.utilities import pairwise
from compas.datastructures import Mesh
from compas.datastructures import mesh_flip_cycles
from compas.geometry import offset_polygon
from  compas.utilities import i_to_rgb

from compas_rhino.artists import MeshArtist


mesh = Mesh.from_json('../cablenet.json')

# ==============================================================================
# Make the concrete extrados
# ==============================================================================

# make a copy of the mesh to create the extrados of the concrete layer
edos = mesh.copy()

# offset the edos compared to the cablenet to the height of the extrados

# ==============================================================================
# Make the blocks
# ==============================================================================

# make a block for every face
# leave a 3cm gap between adjacent blocks
blocks = []
for fkey in edos.faces():
    vertices = edos.face_vertices(fkey)

    if len(vertices) != 4:
        continue

    # normals of the cablenet
    # coordinates of the extrados

    # bottom face coordinates offset from vertex coordinates

    top = []
    for point, normal in zip(bottom, normals):
        x = point[0] + 0.1 * normal[0]
        y = point[1] + 0.1 * normal[1]
        z = point[2] + 0.1 * normal[2]
        top.append([x, y, z])

    # vertices and faces of the block

    block = Mesh.from_vertices_and_faces(vertices, faces)
    block.name = "Block.{}".format(fkey)

    blocks.append(block)

# ==============================================================================
# Visualize the blocks
# ==============================================================================

artist = MeshArtist(None, layer="Blocks")
