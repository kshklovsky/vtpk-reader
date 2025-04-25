# vtpk-reader

[![CI](https://github.com/kshklovsky/vtpk-reader/actions/workflows/ci.yml/badge.svg)](https://github.com/kshklovsky/vtpk-reader/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/kshklovsky/vtpk-reader/badge.svg?branch=main)](https://coveralls.io/github/kshklovsky/vtpk-reader?branch=main)

A library to read ESRI Vector Tile Package (.vtpk) files

### Installation
```
pip install vtpk_reader
```

### Get started
Read vtpk file and extract some features

```Python
from vtpk_reader import Vtpk

vtpk = Vtpk("path/to/your/vtpk/file.vtpk")
# Get all tiles at LOD (level of detail) zero, there should only be one tiles
tiles = vtpk.get_tiles(0, None)  
# Get the one of the tiles
first_tile = list(tiles)[0]
# Extract the tile features
features = vtpk.tile_features(first_tile)
# Look at the keys in the data
print(f"{features.keys()})
```

