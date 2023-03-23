import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.1
import QtQuick.Controls.Material 2.15
import QtWebSockets 1.0

Column{
        id: mainLayout
        anchors.fill: parent
        anchors.margins: appWindow.margin
        GroupBox {
            id: rowBox
            title: "Row layout"
            Layout.fillWidth: true
            Layout.minimumWidth: rowLayout.Layout.minimumWidth + 30

            Row {
                id: rowLayout
                anchors.fill: parent
                TextField {
                    placeholderText: "This wants to grow horizontally"
                    Layout.fillWidth: true
                }
                Button {
                    text: "Button"
                }
            }
        }

}