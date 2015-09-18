import re;
from dxBugIdConfig import dxBugIdConfig;

def cCdbWrapper_fasReadOutput(oCdbWrapper):
  sLine = "";
  asLines = [];
  while 1:
    sChar = oCdbWrapper.oCdbProcess.stdout.read(1);
    if sChar == "\r":
      pass; # ignored.
    elif sChar in ("\n", ""):
      if sChar == "\n" or sLine:
        if dxBugIdConfig["bOutputStdIO"]:
          print "cdb>%s" % repr(sLine)[1:-1];
        oCdbWrapper.asCdbStdIO.append(sLine);
        asLines.append(sLine);
      if sChar == "":
        break;
      sLine = "";
    else:
      sLine += sChar;
      # Detect the prompt.
      oPromptMatch = re.match("^\d+:\d+(:x86)?> $", sLine);
      if oPromptMatch:
        oCdbWrapper.sCurrentISA = oPromptMatch.group(1) and "x86" or oCdbWrapper.sCdbISA;
        if dxBugIdConfig["bOutputStdIO"]:
          print "cdb>%s" % repr(sLine)[1:-1];
        oCdbWrapper.asCdbStdIO.append(sLine);
        return asLines;
  oCdbWrapper.bCdbRunning = False;
  return None;
