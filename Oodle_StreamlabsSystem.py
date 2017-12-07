import sys
import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
import datetime
import re

ScriptName = "Oodle"
Website = "https://willeccles.me"
Description = "!oodle <message> does funny things."
Creator = "Will Eccles"
Version = "69.4.20"

m_Command = "!oodle"
m_CooldownSeconds = 10
m_CommandPermission = "everyone"
m_CommandIndo = "Replaces vowels with 'oodle'"

def Init():
    # nothing to do here
    return

def Tick():
    # also nothing to do here
    return

def Oodle(msg):
    # just gonna use the i flag and make everything 'oodle' regardless of case
    return re.sub(r'[aeiou]', r'oodle', msg, flags=re.IGNORECASE)

def Execute(data):
    if data.IsChatMessage():
        if data.GetParam(0).lower() == m_Command and not Parent.IsOnCooldown(ScriptName, m_Command) and data.GetParamCount() >= 2:
            Parent.SendTwitchMessage(Oodle(re.sub(r'!oodle', r'', data.Message, count=1, flags=re.IGNORECASE)))
            Parent.AddCooldown(ScriptName, m_Command, m_CooldownSeconds)
    return
