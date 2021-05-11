"""
Для компиляции программы
"""

from cx_Freeze import setup, Executable


executables = [Executable("old_Library.py", targetName="old_Library.exe", base="Win32GUI", icon='helmet.ico')]
includes = ['json', 'pickle', 'csv', 'os', 'tkinter', 'abc', 'typing']
zip_include_packages = ['json', 'pickle', 'csv', 'os', 'tkinter', 'abc', 'typing']
include_files = ['Drivers.py', 'linkedlist.py', '05.json']
options = {'build_exe': {'include_msvcr': True, 'includes': includes, 'zip_include_packages': zip_include_packages,
                         'build_exe': 'build_windows', 'include_files': include_files}}
setup(name='old_Library', version='0.0.22', description='My app', executables=executables, options=options)

# setup(name='old_Library', version='0.22', description='My_app', executables=[Executable('old_Library.py')])
ё
