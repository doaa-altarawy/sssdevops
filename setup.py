import setuptools
import versioneer


if __name__ == "__main__":
    setuptools.setup(
        name='sssdevops',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        description='Project for the MolSSI summer school in RTP, NC',
        author='Doaa Altarawy',
        url="https://github.com/doaa_altarawy/sssdevops",
        license='BSD 3-C',
        packages=setuptools.find_packages(),
        install_requires=[

        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
            ],
            'develop': [   # extra
                'yapf',
                'versioneer'
            ]
        },

        tests_require=[
            'pytest',
        ],
        zip_safe=True,
    )