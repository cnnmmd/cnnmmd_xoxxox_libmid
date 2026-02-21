#---------------------------------------------------------------------------
# 参照

import subprocess
from xoxxox.libmid import LibMid
from xoxxox.params import Medium

#---------------------------------------------------------------------------
# 処理：変換：サウンド

class CnvVce:

  # 変換：ウェブブラウザ向け
  # 入力：WebM
  # 出力：WAV
  @staticmethod
  def webwav(datraw):
    prccmd = [
      'ffmpeg', 
      '-i', 'pipe:0',
      '-ar', str(Medium.ratsmp),
      '-f', 'wav',
      'pipe:1'
    ]
    prcsub = subprocess.Popen(prccmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    datwav, e = prcsub.communicate(input=datraw)
    if prcsub.returncode != 0:
      raise Exception(f"err: {e.decode('utf-8')}")
    return datwav

  # 変換：ゲームエンジン向け
  # 入力：WAV
  # 出力：PCM ... 浮動小数点型／３２ビット／リトルエンディアン
  @staticmethod
  def wavpcm(datwav):
    prccmd = [
      'ffmpeg', 
      '-i', 'pipe:0',
      '-ac', '1',
      '-ar', str(Medium.ratsmp),
      '-f', 'f32le',
      'pipe:1'
    ]
    prcsub = subprocess.Popen(prccmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    datraw, e = prcsub.communicate(input=datwav)
    if prcsub.returncode != 0:
      raise Exception(f"err: {e.decode('utf-8')}")
    return datraw

  # 変換：ゲームエンジン向け
  # 入力：PCM ... 浮動小数点型／３２ビット／リトルエンディアン
  # 出力：WAV
  @staticmethod
  def pcmwav(datraw):
    prccmd = [
      'ffmpeg', 
      '-ac', '1',
      '-ar', str(Medium.ratsmp),
      '-f', 'f32le',
      '-i', 'pipe:0',
      '-f', 'wav',
      'pipe:1'
    ]
    prcsub = subprocess.Popen(prccmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    datwav, e = prcsub.communicate(input=datraw)
    if prcsub.returncode != 0:
      raise Exception(f"err: {e.decode('utf-8')}")
    return datwav

  # 変換：マイコン向け
  # 入力：WAV
  # 出力：PCM ... 符号アリ整数型／３２ビット／リトルエンディアン
  @staticmethod
  def wavpcl(datwav):
    prccmd = [
      'ffmpeg', 
      '-i', 'pipe:0',
      '-ac', '1',
      '-ar', str(Medium.ratsmp),
      '-f', 's32le',
      'pipe:1'
    ]
    prcsub = subprocess.Popen(prccmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    datraw, e = prcsub.communicate(input=datwav)
    if prcsub.returncode != 0:
      raise Exception(f"err: {e.decode('utf-8')}")
    return datraw
  
  # 変換：マイコン向け
  # 入力：PCM ... 符号アリ整数型／１６ビット／リトルエンディアン
  # 出力：WAV  
  @staticmethod
  def pclwav(datraw):
    prccmd = [
      'ffmpeg', 
      '-ac', '1',
      '-ar', str(Medium.ratsmp),
      '-f', 's16le',
      '-i', 'pipe:0',
      '-af', 'volume=4.0',
      '-f', 'wav',
      'pipe:1'
    ]
    prcsub = subprocess.Popen(prccmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    datwav, e = prcsub.communicate(input=datraw)
    if prcsub.returncode != 0:
      raise Exception(f"err: {e.decode('utf-8')}")
    return datwav

LibMid.dicprc["xoxxox.CnvVce.webwav"] = {"frm": "xoxxox_libcnv.CnvVce.webwav", "arg": ["keymmd"], "syn": True}
LibMid.dicprc["xoxxox.CnvVce.wavpcm"] = {"frm": "xoxxox_libcnv.CnvVce.wavpcm", "arg": ["keymmd"], "syn": True}
LibMid.dicprc["xoxxox.CnvVce.pcmwav"] = {"frm": "xoxxox_libcnv.CnvVce.pcmwav", "arg": ["keymmd"], "syn": True}
LibMid.dicprc["xoxxox.CnvVce.wavpcl"] = {"frm": "xoxxox_libcnv.CnvVce.wavpcl", "arg": ["keymmd"], "syn": True}
LibMid.dicprc["xoxxox.CnvVce.pclwav"] = {"frm": "xoxxox_libcnv.CnvVce.pclwav", "arg": ["keymmd"], "syn": True}

#---------------------------------------------------------------------------
# 処理：変換：イメージ

class CnvImg:

# 入力：PNG
# 出力：JPG
  @staticmethod
  def pngjpg(datorg):
    prccmd = [
      'convert', 
      '-resize', 'x240',
      '-interlace', 'none',
      '-quality', '25',
      'png:-',
      'jpg:-'
    ]
    prcsub = subprocess.Popen(prccmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    datimg, e = prcsub.communicate(input=datorg)
    if prcsub.returncode != 0:
      raise Exception(f"err: {e.decode('utf-8')}")
    return datimg

LibMid.dicprc["xoxxox.CnvImg.pngjpg"] = {"frm": "xoxxox_libcnv.CnvImg.pngjpg", "arg": ["keymmd"], "syn": True}
