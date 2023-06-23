import os

from conans import CMake, ConanFile, tools

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package_multi"
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join("bin", "test_package")
            self.run("{0}".format(bin_path), run_environment=True)
