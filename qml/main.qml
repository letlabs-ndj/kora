import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.2
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    title: qsTr("Test")
    width: 830
    height: 500
    visible: true
    property var temp:"0"
    property var hum:"0"
    property var lum:"0"
    property string air_qual:"00"
    property bool sprinkler:true
    property bool ven:true
    property QtObject gui    
    Material.theme: Material.light
    Material.accent: "#367E18"
    property var datafontSize: 28
    property var controlsfontSize: 15
    property bool pass:false
    property alias actualPage: stack.currentItem
    FontLoader { id: fontello; source: "assets/font/fontello.ttf" }
    
 StackView {
        id: stack
        initialItem: mainView
        anchors.fill: parent
    }
    
    Component{
        id:mainView

        Column{
            Image{
            anchors.fill: parent
            source: "../assets/images/background.png"
            fillMode: Image.PreserveAspectCrop
        }
            
            Row {
                spacing: 180
                leftPadding : 380

                    Text{
                    text: "TIME"
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
                        text:"\uE804"
                        font.family: fontello.font.family
                        color: "white"
                    }

                    Text{
                        id:network
                        text:"\uE801"
                        font.family: fontello.font.family
                        color: "white"
                    }
         

                }
                
                
            }
            
            
            
                    Column{
                        spacing:10
                        leftPadding:380
                        topPadding:50
                        
                        Rectangle{
                            width:100
                            height:100
                            color:"transparent"
                            Image{
                                anchors.fill: parent
                                source: "../assets/images/user.png"
                                fillMode: Image.PreserveAspectCrop
                            }
                        }
                        
                        Text{
                            text:"Ma serre"
                            color: "white"
                            font.pointSize:15
                            leftPadding:10
                        }
                        Column{
                            leftPadding:-50
                              TextField {
                                id:user_pass
                                placeholderText: qsTr("     Entrer password")
                                placeholderTextColor: "white"
                                color:"white"
                                font.pointSize:13
                                echoMode: TextInput.Password  
                                onAccepted:{
                                    pass =  gui.login(user_pass.text)  

                                    if (pass){
                                        stack.push(Qt.resolvedUrl("home.qml"));
                                    }else{
                                        console.log("no");
                                        pass_validator.visible = true
                                    }

                                    
                                }                     
                                background: Rectangle {
                                    radius: 8
                                    width:200
                                    height:40
                                    color:"#0A0A0A"
                                    border.color: "Transparent"
                                    opacity:0.5
                                }
                            
                            } 
                            Text{
                                id: pass_validator
                                text:"Mot de passe incorrecte"
                                color: "#EC5757"
                                font.pointSize:10
                                leftPadding:25
                                topPadding:5
                                visible:false
                        }  
                        }
                       
                     }
           
    }
}
}

