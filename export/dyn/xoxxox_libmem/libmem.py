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

LibMid.dicprc.append({"key": "xoxxox.OpeMem.setmem", "frm": "LibMid.plugin['xoxxox_libmem'].OpeMem.setmem(values[dicreq['keydat']], dicreq['keymem'], memory)", "syn": True})
LibMid.dicprc.append({"key": "xoxxox.OpeMem.getmem", "frm": "LibMid.plugin['xoxxox_libmem'].OpeMem.getmem(values[dicreq['keydat']], dicreq['keymem'], memory)", "syn": True})
