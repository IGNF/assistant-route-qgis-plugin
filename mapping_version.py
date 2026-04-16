from qgis.PyQt.QtCore import Qt,QT_VERSION_STR
from qgis.PyQt.QtWidgets import QTextEdit

# Détection version Qt)
QT6 = QT_VERSION_STR.startswith("6")

if QT6:
    from qgis.PyQt.QtCore import QRegularExpression
    from qgis.PyQt.QtGui import QRegularExpressionValidator, QValidator
else:
    from qgis.PyQt.QtCore import QRegExp
    from qgis.PyQt.QtGui import QRegExpValidator, QValidator

# Fenêtres
Dialog = Qt.WindowType.Dialog if QT6 else Qt.Dialog
WindowCloseButtonHint = Qt.WindowType.WindowCloseButtonHint if QT6 else Qt.WindowCloseButtonHint
WindowTitleHint = Qt.WindowType.WindowTitleHint if QT6 else Qt.WindowTitleHint
WindowStaysOnTopHint = Qt.WindowType.WindowStaysOnTopHint if QT6 else Qt.WindowStaysOnTopHint

# Alignment
AlignCenter = Qt.AlignmentFlag.AlignCenter if QT6 else Qt.AlignCenter

# Text wrapping
NoWrap = QTextEdit.LineWrapMode.NoWrap if QT6 else QTextEdit.NoWrap

# regex
Acceptable = QValidator.State.Acceptable if QT6 else QValidator.Acceptable

# REGEX
def make_regex(pattern):
    """Retourne un objet regex compatible Qt5 / Qt6"""
    if QT6:
        return QRegularExpression(pattern)
    return QRegExp(pattern)


def make_validator(pattern, parent=None):
    """Retourne un validator compatible Qt5 / Qt6"""
    if QT6:
        return QRegularExpressionValidator(QRegularExpression(pattern), parent)
    return QRegExpValidator(QRegExp(pattern), parent)


def regex_has_match(pattern, text):
    """Test simple de match regex compatible"""
    if QT6:
        return QRegularExpression(pattern).match(text).hasMatch()
    else:
        return QRegExp(pattern).indexIn(text) != -1

# # QT6
# try :
#     from qgis.PyQt.QtCore import QRegularExpression
#     from qgis.PyQt.QtGui import QRegularExpressionValidator, QValidator
#     Dialog = Qt.WindowType.Dialog
#     WindowCloseButtonHint = Qt.WindowType.WindowCloseButtonHint
#     WindowTitleHint = Qt.WindowType.WindowTitleHint
#     WindowStaysOnTopHint = Qt.WindowType.WindowStaysOnTopHint
#     Checked = Qt.CheckState.Checked
#     Unchecked = Qt.CheckState.Unchecked
#     ItemIsEnabled = Qt.ItemFlag.ItemIsEnabled
#     ItemIsUserCheckable = Qt.ItemFlag.ItemIsUserCheckable
#     MatchExactly = Qt.MatchFlag.MatchExactly
#     RightSide = QTabBar.ButtonPosition.RightSide
#     LeftSide = QTabBar.ButtonPosition.LeftSide
#     Warning = QMessageBox.Icon.Warning
#     YesRole = QMessageBox.ButtonRole.YesRole
#     AcceptRole = QMessageBox.ButtonRole.AcceptRole
#     NoSelection = QAbstractItemView.SelectionMode.NoSelection
# # QT5
# except :
#     from qgis.PyQt.QtCore import QRegExp
#     from qgis.PyQt.QtGui import QRegExpValidator, QValidator
#     Dialog = Qt.Dialog
#     WindowCloseButtonHint = Qt.WindowCloseButtonHint
#     WindowTitleHint = Qt.WindowTitleHint
#     WindowStaysOnTopHint = Qt.WindowStaysOnTopHint
#     Checked = Qt.Checked
#     Unchecked = Qt.Unchecked
#     ItemIsEnabled = Qt.ItemIsEnabled
#     ItemIsUserCheckable = Qt.ItemIsUserCheckable
#     MatchExactly = Qt.MatchFlag.MatchExactly
#     RightSide = QTabBar.RightSide
#     LeftSide = QTabBar.LeftSide
#     Warning = QMessageBox.Warning
#     YesRole = QMessageBox.YesRole
#     AcceptRole = QMessageBox.AcceptRole
#     NoSelection = QListWidget.NoSelection