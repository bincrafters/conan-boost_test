#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostTestConan(base.BoostBaseConan):
    name = "boost_test"
    version = "1.70.0"

    @property
    def boost_build_requires(self):
        return ["predef"]

    def package_info(self):
        super(BoostTestConan, self).package_info()
        self.cpp_info.libs = [
            x
            for x in self.cpp_info.libs
            if x.find('exec_monitor') < 0]
