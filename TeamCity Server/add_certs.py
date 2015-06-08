__author__ = 'designerror'

import os
import subprocess

class CertificateImporter:

    def __init__(self, storage_directory):

        self.storage_directory = storage_directory

        if not os.path.exists(self.storage_directory):

            os.makedirs(storage_directory)

    def list(self, location_directory):

        certificates = list()

        for filename in os.listdir(location_directory):

            file_path = os.path.join(location_directory, filename)

            if not os.path.isdir(file_path):

                return certificates

            extension = os.path.splitext(filename)[1][1:].strip()

            if extension == ".crt":

                certificates.append(file_path)

        return certificates

    def install(self, certificate_path):

        filename = os.path.split(certificate_path)[:-1]
        new_path = os.path.join(storage_directory, filename)
        os.rename(certificate_path, new_path)

        subprocess.call(["keytool", "-importcert",  "-file", new_path, "-keystore", self.storage_directory])

if __name__ == "__main__":

    storage_directory = os.environ.get("STORAGE_DIRECTORY")
    mount_directory = os.environ.get("MOUNT_DIRECTORY")

    importer = CertificateImporter(storage_directory)

    for certificate_path in importer.list(mount_directory):

        importer.install(certificate_path)

     subprocess.call(["/opt/TeamCity/bin/teamcity-server.sh", "run"])
