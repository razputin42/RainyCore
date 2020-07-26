from PyQt5.QtCore import pyqtSignal, QObject


class SignalNexus(QObject):
    # General signals
    attackSignal = pyqtSignal(str, str, name="attackSignal")
    printSignal = pyqtSignal(str, name="printSignal")
    setWidgetStretch = pyqtSignal(int, int, name="setWidgetStretch")

    # Bookmark and encounter widget signals
    addSpellsSignal = pyqtSignal(list, name="addSpellsSignal")
    addMonstersToEncounter = pyqtSignal(QObject, int, name="addMonstersToEncounter")

    # Select signals
    viewerSelectChanged = pyqtSignal(int, name="viewerSelectChanged")

    # Deselect signals
    encounterDeselectSignal = pyqtSignal(name="encounterDeselctSignal")
    treasureHoardDeselectSignal = pyqtSignal(name="treasureHoardDeselectSignal")

sNexus = SignalNexus()