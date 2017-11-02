from conans import ConanFile, tools
import os


class BoostTestConan(ConanFile):
    name = "Boost.Test"
    version = "1.65.1"
    generators = "boost" 
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-test"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["test"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing" 
    requires =  "Boost.Algorithm/1.65.1@bincrafters/testing", \
                      "Boost.Assert/1.65.1@bincrafters/testing", \
                      "Boost.Bind/1.65.1@bincrafters/testing", \
                      "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Core/1.65.1@bincrafters/testing", \
                      "Boost.Detail/1.65.1@bincrafters/testing", \
                      "Boost.Exception/1.65.1@bincrafters/testing", \
                      "Boost.Function/1.65.1@bincrafters/testing", \
                      "Boost.Io/1.65.1@bincrafters/testing", \
                      "Boost.Iterator/1.65.1@bincrafters/testing", \
                      "Boost.Mpl/1.65.1@bincrafters/testing", \
                      "Boost.Numeric_Conversion/1.65.1@bincrafters/testing", \
                      "Boost.Optional/1.65.1@bincrafters/testing", \
                      "Boost.Preprocessor/1.65.1@bincrafters/testing", \
                      "Boost.Range/1.65.1@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
                      "Boost.Static_Assert/1.65.1@bincrafters/testing", \
                      "Boost.Timer/1.65.1@bincrafters/testing", \
                      "Boost.Type_Traits/1.65.1@bincrafters/testing", \
                      "Boost.Utility/1.65.1@bincrafters/testing"

                      #algorithm9 assert1 bind3 config0 core2 detail5 exception5 function5 io1 iterator5 mpl5 numeric~conversion6 optional5 preprocessor0 range7 smart_ptr4 static_assert1 timer4 type_traits3 utility5

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def build(self):
        self.run(self.deps_user_info['Boost.Generator'].b2_command)

    def package(self):
        self.copy(pattern="*", dst="lib", src="stage/lib")
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_info(self):
        self.user_info.lib_short_names = ",".join(self.lib_short_names)
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.defines.append("BOOST_ALL_NO_LIB=1")

