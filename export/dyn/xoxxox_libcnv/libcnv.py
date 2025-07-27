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

LibMid.dicprc.append({"key": "xoxxox.CnvVce.webwav", "frm": "LibMid.plugin['xoxxox_libcnv'].CnvVce.webwav(values[dicreq['keydat']])", "syn": True})
LibMid.dicprc.append({"key": "xoxxox.CnvVce.wavpcm", "frm": "LibMid.plugin['xoxxox_libcnv'].CnvVce.wavpcm(values[dicreq['keydat']])", "syn": True})
LibMid.dicprc.append({"key": "xoxxox.CnvVce.pcmwav", "frm": "LibMid.plugin['xoxxox_libcnv'].CnvVce.pcmwav(values[dicreq['keydat']])", "syn": True})
LibMid.dicprc.append({"key": "xoxxox.CnvVce.wavpcl", "frm": "LibMid.plugin['xoxxox_libcnv'].CnvVce.wavpcl(values[dicreq['keydat']])", "syn": True})
LibMid.dicprc.append({"key": "xoxxox.CnvVce.pclwav", "frm": "LibMid.plugin['xoxxox_libcnv'].CnvVce.pclwav(values[dicreq['keydat']])", "syn": True})

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

LibMid.dicprc.append({"key": "xoxxox.CnvImg.pngjpg", "frm": "LibMid.plugin['xoxxox_libcnv'].CnvImg.pngjpg(values[dicreq['keydat']])", "syn": True})
