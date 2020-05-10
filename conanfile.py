from conans import ConanFile, tools
import os

class FASTBuildInstallerConan(ConanFile):
    name = "fastbuild-installer"
    version = "0.99"
    license = "http://fastbuild.org/docs/license.html"
    description = "FASTBuild is a high performance, open-source build system supporting highly scalable compilation, caching and network distribution."
    url = "http://fastbuild.org/docs/home.html"

    settings = "os"

    # Get the sources from lua.org
    def source(self):
        if self.settings.os == 'Windows':
            zip_name = "FASTBuild-Windows-x64-v{}.zip".format(self.version)
            tools.download("http://fastbuild.org/downloads/v{}/{}".format(self.version, zip_name), zip_name)
            tools.unzip(zip_name)
            os.unlink(zip_name)

        else:
            self.error("Unsupported system: {}".format(self.settings.os))
        pass

    # Export the files available in the package
    def package(self):
        self.copy("LICENSE.TXT", dst="LICENSE")

        # Lua and Moonscript files
        self.copy("FBuild.exe", dst="{}".format(self.settings.os), keep_path=False)


    def package_info(self):
        # Enviroment info
        self.env_info.path.append(os.path.join(self.package_folder, "{}".format(self.settings.os)))
