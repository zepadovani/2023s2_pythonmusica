import music21 as m21

m21set = m21.environment.UserSettings()
m21set['musicxmlPath'] = 'C:\\Program Files\\MuseScore 4\\bin\\MuseScore4.exe'
m21set['musescoreDirectPNGPath'] = 'C:\\Program Files\\MuseScore 4\\bin\\MuseScore4.exe'
m21set['musicxmlPath']



n = m21.note.Note("F5")
n.show()