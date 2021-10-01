from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_exe_options = {'packages': [], 'excludes': []}

bdist_msi_options = {}

base = 'Console'

executables = [
    Executable('main.py', base=base, target_name = 'SpotifyDL',icon="logo.ico")
]

setup(name='Spotify Downloader',
      version = '1.0',
      description = 'Download song/playlist from Spotify',
      options = {'build_exe': build_exe_options,
                 "bdist_msi": bdist_msi_options},
      executables = executables)
