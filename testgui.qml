import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.2
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    title: qsTr("Test")
    width: 900
    height: 450
    visible: true
    property int temp:0
    property int hum:0
    property int lum:0
    property int air_qual:0
    property bool sprinkler:true
    property bool ven:true
    property QtObject gui    
    Material.theme: Material.light
    Material.accent: "#367E18"
    property var datafontSize: 30
    property var controlsfontSize: 13
    FontLoader { id: nunito; source: "assets/font/nunito.ttf" }
    FontLoader { id: fontawesome; source: "assets/font/fontello.ttf" }
    FontLoader { id: mamakilo; source: "assets/font/MamaKiloBlack.ttf" }
    
    StackView {
        id: stack
        initialItem: mainView
        anchors.fill: parent
    }
    
    Component{
        id:mainView

        Column{
            
            Row {
                spacing: 180
                leftPadding : 50
                topPadding : 10

                    Text{
                    text: "KORA DASHBOARD"
                    topPadding : 15
                    font.pointSize:20
                    color:"#367E18"
                }

                Rectangle {
                    width: 50; height: 50
                    color:"Transparent"

                    Image {
                        anchors.fill: parent
                        source: "assets/images/user.png"
                        fillMode: Image.PreserveAspectCrop
                    }

                    Text{
                    text: "LETLABS"
                    leftPadding : 60
                    topPadding : 15
                    color:"#367E18"
                }

                }
                
            }
            
            
            Row{
                spacing:80

                Column{
                    leftPadding : 50
                    topPadding : 50
                    spacing:30

                    Row{
                        spacing:60

                        Column{
                            spacing:5
                            Row{
                                spacing:10
                                Text{
                                    text: "\uF2C8"
                                    font.family: fontawesome.font.family
                                    font.pointSize: datafontSize
                                    color:"#850000"
                                }

                                Text{
                                id: tem
                                text: temp+" °C"
                                font.pointSize: datafontSize
                                }
                                
                            }
                            
                        Text{
                            text: "Temperature"
                        }
                        }
                        Column{
                            spacing:5

                            Row{
                                spacing:10
                                Text{
                                    text: "\uE803"
                                    font.family: fontawesome.font.family
                                    font.pointSize: datafontSize
                                    color:"#2B3467"
                                }
                                Text{
                                    id: humidity
                                    text: hum+" %"
                                    font.pointSize: datafontSize
                                }
                            }
                            
                        Text{
                            text: "Humidity"
                        }
                        }
                        
                    }

                    Row{
                        spacing:80

                        Column{
                            spacing:5

                            Row{
                                spacing:10
                                Text{
                                    text: "\uE801"
                                    font.family: fontawesome.font.family
                                    font.pointSize: datafontSize
                                    color:"#F2CD5C"
                                }
                                Text{
                                    id: light
                                    text: lum
                                    font.pointSize: datafontSize
                                }
                            }
                            
                        Text{
                            text: "Luminosity"
                        }
                        }
                        Column{
                            spacing:5

                            Row{
                                spacing:10
                                Text{
                                    text: "\uE800"
                                    font.family: fontawesome.font.family
                                    font.pointSize: datafontSize
                                    color:"#90A17D"
                                }
                                Text{
                                    id: air
                                    text: air_qual+" PPM"
                                    font.pointSize: datafontSize
                                }
                            }
                            
                        Text{
                            text: "Taux CO2"
                        }
                        }
                        
                    }
                    
                }
                Column{
                    topPadding : 40
                    spacing:30
                    Row{
                        spacing:20
                        Text{
                            text: "Ventilateur"
                            topPadding : 15
                            font.pointSize: controlsfontSize
                        }
                        Switch {
                            id:venti
                            checked:ven
                            onCheckedChanged: {
                                if (checked) {
                                    gui.ventilage(true)
                                }else{
                                    gui.ventilage(false)
                                }
                            }
                        }
                    }

                    Row{
                        spacing:35
                        Text{
                            text: "Arroseur"
                            topPadding : 15
                            font.pointSize:controlsfontSize
                        }
                        Switch {
                            id:arro
                            checked:sprinkler
                            onCheckedChanged: {
                                if (checked) {
                                    gui.arrosage(true)
                                }else{
                                    gui.arrosage(false)
                                }
                            }                           
                           
                        }
                    }
                    
                    Row{
                        spacing:35
                        Text{
                            text: "Eclairage"
                            topPadding : 15
                            font.pointSize: controlsfontSize
                        }
                        Slider {
                            from: 0
                            value: 0
                            to: 100
                            onPositionChanged:{
                                gui.eclairage(value)
                            } 
                        }
                        
                    }
                }
            }
            
            Row{
                spacing:20
                topPadding:40
                leftPadding:300
                RoundButton {
                    text: "Choisir une \nPlante"
                    radius: 5
                    highlighted: true
                    Material.accent: "#367E18"
                    onClicked:stack.push(mainView)
                } 
                RoundButton {
                    text: "Authentifier \nun appareil"
                    radius: 5
                    highlighted: true
                    Material.accent: "#367E18"
                    onClicked:gui.text("Clicked")

                } 
            }
            
            


        }
    }
}

