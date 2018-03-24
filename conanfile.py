#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostTestConan(ConanFile):
    name = "boost_test"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost_test"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["test"]
    is_header_only = False

    options = {"shared": [True, False]}
    default_options = "shared=False"

    requires = (
        "boost_package_tools/1.65.1@bincrafters/stable",
        "boost_algorithm/1.65.1@bincrafters/stable",
        "boost_assert/1.65.1@bincrafters/stable",
        "boost_bind/1.65.1@bincrafters/stable",
        "boost_config/1.65.1@bincrafters/stable",
        "boost_core/1.65.1@bincrafters/stable",
        "boost_detail/1.65.1@bincrafters/stable",
        "boost_exception/1.65.1@bincrafters/stable",
        "boost_function/1.65.1@bincrafters/stable",
        "boost_io/1.65.1@bincrafters/stable",
        "boost_iterator/1.65.1@bincrafters/stable",
        "boost_mpl/1.65.1@bincrafters/stable",
        "boost_numeric_conversion/1.65.1@bincrafters/stable",
        "boost_optional/1.65.1@bincrafters/stable",
        "boost_preprocessor/1.65.1@bincrafters/stable",
        "boost_range/1.65.1@bincrafters/stable",
        "boost_smart_ptr/1.65.1@bincrafters/stable",
        "boost_static_assert/1.65.1@bincrafters/stable",
        "boost_timer/1.65.1@bincrafters/stable",
        "boost_type_traits/1.65.1@bincrafters/stable",
        "boost_utility/1.65.1@bincrafters/stable"
    )

    def package_id_additional(self):
        boost_deps_only = [dep_name for dep_name in self.info.requires.pkg_names if dep_name.startswith("boost_")]

        for dep_name in boost_deps_only:
            self.info.requires[dep_name].full_version_mode()

    def package_info_additional(self):
        self.cpp_info.libs = [x for x in self.cpp_info.libs if x.find('exec_monitor') < 0]

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.65.1@bincrafters/stable"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
