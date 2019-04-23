# -*- mode: python -*-
import os
import sys
import site

sys.path.insert(0, '.')

print('==>>>       \n'*5)
print(*sys.path, sep='\n')
print('\n'*5)
print(os.getcwd())
print(os.listdir())

block_cipher = None

a = Analysis([Path('asammdf') / 'gui' / 'asammdfgui.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'numpy.core._dtype_ctypes'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)
    
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)
    
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='asammdfgui',
    debug=True,
    strip=False,
    upx=True,
    console=True,
    icon='asammdf.ico',
)