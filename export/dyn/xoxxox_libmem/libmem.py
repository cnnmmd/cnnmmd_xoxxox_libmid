#---------------------------------------------------------------------------
# 参照

from xoxxox.libmid import LibMid

#---------------------------------------------------------------------------
# 処理：操作：メモリ

class OpeMem:

  # 機能：データを、メモリに書き込む
  @staticmethod
  def setmem(target, keymem, memory):
    memory[keymem] = target
    return ""

  # 機能：メモリからデータを読み出す
  @staticmethod
  def getmem(target, keymem, memory):
    try:
      return memory[keymem]
    except Exception as e:
      return target

LibMid.dicprc["xoxxox.OpeMem.setmem"] = {"frm": "xoxxox_libmem.OpeMem.setmem", "arg": ["keydat"], "mem": ["keymem"], "syn": True}
LibMid.dicprc["xoxxox.OpeMem.getmem"] = {"frm": "xoxxox_libmem.OpeMem.getmem", "arg": ["keydat"], "mem": ["keymem"], "syn": True}
