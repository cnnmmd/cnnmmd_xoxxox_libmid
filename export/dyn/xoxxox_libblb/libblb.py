#---------------------------------------------------------------------------
# 参照

import os
import glob
from xoxxox.libmid import LibMid

#---------------------------------------------------------------------------
# 処理：操作：ファイル

class OpeBlb:

  # 変数
  lstdat = []
  posdat = 0
  oldpth = ""

  # 機能：データを、ファイルに書き込む
  @staticmethod
  def setdir(dattgt, target):
    with open(target, "wb") as f:
      f.write(dattgt)
    return ""

  # 機能：ファイルからデータを読み出す
  @staticmethod
  def getdir(target):
    with open(target, "rb") as f:
      dattgt = f.read()
    return dattgt

  # 機能：データを、ファイルに書き込む（キーを元に（重複ナシ））
  @staticmethod
  def setdis(dattgt, keydat, extdat, folder):
    with open(folder + "/" + keydat + extdat, "wb") as f:
      f.write(dattgt)
    return ""

  # 機能：ファイルからデータを読み込む（複数、順次）
  @staticmethod
  def getdis(extdat, folder):
    os.chdir(folder)
    if folder != OpeBlb.oldpth:
      #OpeBlb.lstdat = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
      OpeBlb.lstdat = glob.glob(folder + "/" + "*" + extdat)
      OpeBlb.oldpth = folder
      OpeBlb.posdat = 0
    if OpeBlb.posdat >= len(OpeBlb.lstdat):
      OpeBlb.posdat = 0
    with open(OpeBlb.lstdat[OpeBlb.posdat], "rb") as f:
      dattgt = f.read()
    OpeBlb.posdat = OpeBlb.posdat + 1
    return dattgt

LibMid.dicprc["xoxxox.OpeBlb.setdir"] = {"frm": "xoxxox_libblb.OpeBlb.setdir", "arg": ["keydat"], "cnf": ["target"], "syn": True}
LibMid.dicprc["xoxxox.OpeBlb.getdir"] = {"frm": "xoxxox_libblb.OpeBlb.getdir", "cnf": ["target"], "syn": True}
LibMid.dicprc["xoxxox.OpeBlb.setdis"] = {"frm": "xoxxox_libblb.OpeBlb.setdis", "arg": ["keydat"], "cnf": ["extdat", "folder"], "syn": True}
LibMid.dicprc["xoxxox.OpeBlb.getdis"] = {"frm": "xoxxox_libblb.OpeBlb.getdis", "cnf": ["extdat", "folder"], "syn": True}
