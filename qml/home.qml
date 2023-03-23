import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.1
import QtQuick.Controls.Material 2.15
import QtWebSockets 1.0


Item {

    property string currTime:"0"
    Material.theme: Material.light
    Material.accent: "#367E18"
    
 
    StackView {
        id: home
        initialItem: mainView
        anchors.fill: parent
    }
    
    
    Component{
        id:mainView

        Column{
            Image{
            anchors.fill: parent
            source: "../assets/images/background2.png"
            fillMode: Image.PreserveAspectCrop
        }
            
            Rectangle{
                    anchors.left:parent.left
                    anchors.right:parent.right
                    color:"#0A0A0A"
                    height:40
                    border.color:"transparent"
                    opacity:0.5
            Row {
                spacing: 180
                leftPadding : 380

                    Text{
                        id:time_txt
                        text: currTime
                        topPadding : 5
                        font.pointSize:20
                        color: "white"
                }

                Row{
                    spacing: 15
                    leftPadding : 80
                    topPadding: 15


                    Text{
                        id:notif
                        text:"\uF0F3"
                        font.family: fontello.font.family
                        color: "white"
                    }

                    Text{
                        id:signal
                        text:"\uE801"
                        font.family: fontello.font.family
                        color: "white"
                    }

                    Component.onCompleted: {
                        socket.active = !socket.active
                    }
                    WebSocket {
                        id: socket
                        url: "ws://localhost:8765"
                        onTextMessageReceived: {
                            console.log(message)
                            messageDialog.open()
                        }
                        onStatusChanged: if (socket.status == WebSocket.Error) {
                                            console.log("Error: " + socket.errorString)
                                        } else if (socket.status == WebSocket.Open) {
                                            console.log("socket opened")
                                            socket.sendTextMessage("yeah")
                                        } else if (socket.status == WebSocket.Closed) {
                                            messageBox.text += "\nSocket closed"
                                        }
                        active: false
                    }
                    

                    Button{
                        id:qr                        
                        font.family: fontello.font.family
                   
                        Text{                       
                            text:"\uE804"
                            font.family: fontello.font.family
                            color: "white"
                        }
                        background: Rectangle {
                            implicitWidth: 20
                            implicitHeight: 20                            
                            border.color: "transparent"
                            color:"transparent"
                            
                        }
                        onClicked: {
                            qrDialog.open()
                            socket.sendTextMessage("let")
                            }


                        Dialog {
                            id: messageDialog
                            width:400
                            x: -550
                            y: 100


                            background:Rectangle {
                                color: "#100F0F"
                                height:200
                                opacity:0.8
                                radius:10
                                
                                
                            
                            Column{
                                spacing: 15
                                anchors.fill: parent
                                topPadding:10
                                leftPadding:10
                                
                                Row{
                                    spacing:10
                                    Text{
                                        text:"\uF0F3"
                                        font.family: fontello.font.family
                                        color:"white"
                                        font.pointSize:15
                                    }
                                    Text{
                                        text:"Authentification"  
                                        color:"white"  
                                        font.pointSize:15                                    
                                    }

                                }
                                Label {                              
                                    elide: Label.ElideRight
                                    text: "Une demande de connection vient d’etre faites, entrez 
votre mots dde passe pour valider la demande"
                                    color:"white"
                                }
                                
                                TextField {
                                    placeholderText: "Password"
                                    echoMode: TextInput.Password
                                    color:"white"
                                    placeholderTextColor: "white"
                                    width:350
                                    background: Item {
                                        implicitHeight: 40
                                        Rectangle {
                                            color: "white"
                                            height: 3
                                            width: parent.width
                                            anchors.bottom: parent.bottom
                                        }
                                    }
                                    
                                }

                                Row{
                                    spacing:10
                                    leftPadding:170
                                    RoundButton {
                                        radius:10 
                                        width:100                                       
                                        highlighted: true
                                        Material.accent: "white"

                                        Text{
                                            leftPadding:25
                                            topPadding:15
                                            text:"Valider"                                    
                                    }
                                        onClicked:{
                                            socket.sendTextMessage(qsTr("OK"))
                                            messageDialog.close()
                                            }
                                    }
                                    RoundButton {
                                        id:annuler
                                        radius:10  
                                        width:100                                      
                                        highlighted: true
                                        Material.accent: "#BA1313"
                                        Text{
                                            leftPadding:25
                                            topPadding:15
                                            text:"Annuler"  
                                            color:"white"                                  
                                    }
                                    onClicked: messageDialog.close()
                                    }

                                }
                            }
                            }

                          }

                          Dialog{
                            id: qrDialog
                            width:300
                            height:250
                            x: -500
                            y: 80
                            
                            Image{
                                anchors.fill: parent
                                source: "../assets/images/qr-img.jpg"
                                fillMode: Image.PreserveAspectCrop
                            }
                          }
                        
                    }
         
                    
                
                
                }
            }

             Connections{
                target: backend

                function onPrintTime(time){
                    time_txt.text = time
                }
            }
        }


    Rectangle{
        anchors.fill: parent
        anchors.topMargin:100
        anchors.leftMargin:20
        anchors.bottomMargin:100
        anchors.rightMargin:20
        color:"#0A0A0A"
        height:200
        width:400
        radius: 50
        border.color:"transparent"
        opacity:0.7
    Row{
        topPadding:50
        leftPadding:30
        spacing:70
    
    Column{  
        spacing:35      
        Row{
            Row{
                spacing:60

                Column{
                    spacing:15
                    Row{
                        spacing:10
                        Text{
                            text: "\uF2C7"
                            font.family: fontawesome.font.family
                            font.pointSize: datafontSize
                            color:"#850000"
                        }

                        Text{
                        id: tem
                        text: temp+" °C"
                        font.pointSize: datafontSize
                        color:"white"
                        }
                        
                    }
                    
                Text{
                    text: "Temperature"
                    font.pointSize:15
                    color:"white"
                }
                }
                Column{
                    spacing:15

                    Row{
                        spacing:10
                        Text{
                            text: "\uE800"
                            font.family: fontellone.font.family
                            font.pointSize: datafontSize
                            color:"#2B3467"
                        }
                        Text{
                            id: humidity
                            text: hum+" %"
                            font.pointSize: datafontSize
                            color:"white"
                        }
                    }
                    
                Text{
                    text: "Humidity"
                    font.pointSize:15
                    color:"white"
                }
                }
                
            }
        }   

        Row{
            spacing:80

            Column{
                spacing:15

                Row{
                    spacing:10
                    Text{
                        text: "\uE801"
                        font.family: fontellone.font.family
                        font.pointSize: datafontSize
                        color:"#F2CD5C"
                    }
                    Text{
                        id: light
                        text: lum
                        font.pointSize: datafontSize
                        color:"white"
                    }
                }
                
            Text{
                text: "Luminosity"
                font.pointSize:15
                color:"white"
            }
            }
            Column{
                spacing:15

                Row{
                    spacing:10
                    Text{
                        text: "\uE802"
                        font.family: fontello.font.family
                        font.pointSize: datafontSize
                        color:"#90A17D"
                    }
                    Text{
                        id: air
                        text: air_qual+" PPM"
                        font.pointSize: datafontSize
                        color:"white"
                    }
                }
                
            Text{
                text: "Taux CO2"
                font.pointSize:15
                color:"white"
            }
            }
            
        }
     }  

     Column{
        topPadding:15
        spacing:10
        Row{
            spacing:20
            Text{
                text: "Ventilateur"
                topPadding : 15
                font.pointSize: controlsfontSize
                color:"white"
            }
            Switch {
                checked:ven
                onClicked:gui.ventilage(checked)
            }
        }

        Row{
            spacing:35
            Text{
                text: "Arroseur"
                topPadding : 15
                font.pointSize:controlsfontSize
                color:"white"
            }
            Switch {
                checked:sprinkler
                onClicked:gui.arrosage(checked)
            }
        }
        
        Row{
            spacing:35
            Text{
                text: "Eclairage"
                topPadding : 10
                font.pointSize: controlsfontSize
                color:"white"
            }
            Slider {
                from: 1
                value: 25
                to: 100
                onPositionChanged:{
                    gui.eclairage(value)
                } 
            }
            
        }
     }
    }
    }
}
    
}
}

