from win32com.client import constants
import os
import win32com.client
import pythoncom
import win32con
import win32api
import time

class SpeechRecognition:
    def __init__(self,wordsToAdd):
        self.spesker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule", constants.SRAToplevel + constants.SRADynamic,0)
        self.wordsRule.Clear()
        [self.wordsRule.InitiaState.AddWordTransition(None,word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule",1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self,phrase):
        self.spesker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self,StreamNumber,StreamPosition,RecognitionType,Result):
        newResult = win32com.client.Dispatch(Result)
        print("说：",newResult.PhraseInfo.GetText())
        s = newResult.PhraseInfo.GetText()
        if s == "上":
            win32api.keybd_event(38, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(38, 0, win32con.KEYEVENTF_KEYUP, 0)
        if s == "下":
            win32api.keybd_event(40, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
        if s == "左":
            win32api.keybd_event(37, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
        if s == "右":
            win32api.keybd_event(39, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == '__main__':
    wordsToAdd = ["上", "下", "左", "右"]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()




