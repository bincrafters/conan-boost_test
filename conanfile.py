#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostTestConan(base.BoostBaseConan):
    name = "boost_test"
    url = "https://github.com/bincrafters/conan-boost_test"
    lib_short_names = ["test"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_algorithm",
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_core",
        "boost_detail",
        "boost_exception",
        "boost_function",
        "boost_io",
        "boost_iterator",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_optional",
        "boost_preprocessor",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_timer",
        "boost_type_traits",
        "boost_utility"
    ]
    b2_build_requires = ["boost_predef"]

    def package_info_additional(self):
        self.cpp_info.libs = [x for x in self.cpp_info.libs if x.find('exec_monitor') < 0]
