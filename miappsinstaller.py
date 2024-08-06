#!/usr/bin/env python3

# Copyright (C) 2004-2024 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Organização: Mestre da Info
# Site: https://www.mestredainfo.com.br

import sys
import os
import shutil
from zipfile import ZipFile

print('')
print('Instalador do MIApps')
print('')
print('Aguarde enquanto a instalação é realizada. Ao concluir essa janela será fechada!')
print('')
print('Desinstalando a versão anterior...')
try:
	shutil.rmtree('C:\\\\mestredainfo\\\\miapps\\\\')
	print('')
except OSError as e:
	print('')

print('Extraindo arquivos em "C:\\mestredainfo\\miapps\\"...')
zf = ZipFile(os.path.dirname(sys.executable) + '/miapps-win32-x64.zip', 'r')
zf.extractall('C:\\\\mestredainfo\\\\')
zf.close()

print('')
print("Instalação concluída com sucesso!")
print('')
sys.exit()
