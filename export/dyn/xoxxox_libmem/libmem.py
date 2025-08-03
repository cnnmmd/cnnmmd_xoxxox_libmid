#---------------------------------------------------------------------------
# 参照

from xoxxox.libmid import LibMid

#---------------------------------------------------------------------------
# 処理：操作：メモリ

class OpeMem:

  # 機能：データを、メモリに書き込む
  @staticmethod
  def setmem(target, keymem):
    LibMid.memory[keymem] = target
    return target

  # 機能：メモリからデータを読み出す
  @staticmethod
  def getmem(target, keymem):
    try:
      return LibMid.memory[keymem]
    except Exception:
      return target

LibMid.dicprc["xoxxox.OpeMem.setmem"] = {"frm": "xoxxox_libmem.OpeMem.setmem", "arg": ["keydat"], "cnf": ["keymem"], "syn": True}
LibMid.dicprc["xoxxox.OpeMem.getmem"] = {"frm": "xoxxox_libmem.OpeMem.getmem", "arg": ["keydat"], "cnf": ["keymem"], "syn": True}
