import unittest
from pathlib import Path

import shapely

from vtpk_reader import Vtpk, VtpkError


class VtpkTestCase(unittest.TestCase):
    test_dir = Path(__file__).resolve().parent
    test_data_dir = test_dir / "test_data"


class TestFileNotFound(VtpkTestCase):
    def test_not_found(self):
        with self.assertRaises(FileNotFoundError):
            Vtpk(self.test_data_dir / "file_not_found.vtpk")


class TestWrongFileFormat(VtpkTestCase):
    def test_wrong_format(self):
        with self.assertRaises(VtpkError):
            Vtpk(self.test_data_dir / "testvtpk.vtpk")


class TestReadingDodgeCityDataset(VtpkTestCase):
    @classmethod
    def setUpClass(cls):
        cls.vtpk = Vtpk(cls.test_data_dir / "dodge_city.vtpk")

    def test_get_tiles_no_box(self):
        self.assertEqual(len(self.vtpk.get_tiles(lods=[0], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[1], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[2], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[3], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[4], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[5], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[6], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[7], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[8], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[9], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[10], bound_box=None)), 1)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[11], bound_box=None)), 2)
        self.assertEqual(len(self.vtpk.get_tiles(lods=[12], bound_box=None)), 0)

    def test_feature_keys(self):
        tiles = self.vtpk.get_tiles(lods=[11], bound_box=None)
        tile = list(tiles)[0]
        features = self.vtpk.tile_features(tile)
        assert set(features.keys()) == {
            "Dodge_city_planet_osm_point_points",
            "Dodge_city_planet_osm_line_lines",
            "Dodge_city_planet_osm_polygon_polygons",
        }

    def test_get_tiles_bounds(self):
        self.assertEqual(len(self.vtpk.get_tiles(lods=[11], bound_box=None)), 2)
        tiles_a = self.vtpk.get_tiles(lods=[11], bound_box=shapely.box(-11131665, 4545941, -11130207, 4546887))
        self.assertEqual(len(tiles_a), 1)
        tiles_b = self.vtpk.get_tiles(lods=[11], bound_box=shapely.box(-11137539, 4545941, -11136248, 4546887))
        self.assertEqual(len(tiles_b), 1)

        self.assertNotEqual(list(tiles_a)[0], list(tiles_b)[0])
