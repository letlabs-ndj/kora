import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.2

ApplicationWindow {
    title: qsTr("Test")
    width: 640
    height: 480
    visible: true
    property string temp:"0"
    property string hum:"0"
    property string lum:"0"
    property bool sprinkler:true
    property bool ven:true
    property QtObject gui
    Column{
        Text{
            id: tem
            text: temp
        }
        Text{
            id: humidity
            text: hum
        }
        Text{
            id: light
            text: lum
        }
        Button {
            text: qsTr("Click Me")
            onClicked:gui.text("Clicked")
        } 
        Slider {
    from: 1
    value: 25
    to: 100
    onPositionChanged: gui.text(value)

    
}
Switch {
        text: qsTr("Wi-Fi")
        checked:sprinkler
    }
    Switch {
        text: qsTr("Bluetooth")
        checked :ven
    }


    }
}

