__author__ = 'designerror'

import os
import subprocess

class CertificateImporter:

    def __init__(self, storage_path, storage_password):

        self.storage_path = storage_path
        self.storage_password = storage_password

    def list(self, location_directory):

        certificates = list()

        if not os.path.isdir(location_directory):

                return certificates

        for filename in os.listdir(location_directory):

            file_path = os.path.join(location_directory, filename)

            extension = os.path.splitext(filename)[1][1:].strip()

            if extension == "crt":

                certificates.append(file_path)

        return certificates

    def install(self, certificate_path):

        subprocess.call(["keytool", "-importcert", "-noprompt", "-trustcacerts", "-file", certificate_path, "-keystore", self.storage_path, "-storepass", self.storage_password])

if __name__ == "__main__":

    storage_path = os.environ.get("STORAGE_PATH")
    mount_directory = os.environ.get("MOUNT_DIRECTORY")
    storage_password = os.environ.get("STORAGE_PASSWORD")

    importer = CertificateImporter(storage_path, storage_password)

    for certificate_path in importer.list(mount_directory):

        importer.install(certificate_path)
