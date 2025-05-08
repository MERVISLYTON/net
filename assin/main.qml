import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("client")


    Rectangle{
        id: recta1
        width: 200
        height: 400
        anchors.horizontalCenter: parent.horizontalCenter

        Column{
            anchors.fill: parent
            spacing: 10

            Rectangle{
                width: parent.width
                height: 60

                TextField{
                    id: serverAddress
                    placeholderText: "server ip address"
                    placeholderTextColor: "red"
                }
            }

            Rectangle{
                width: parent.width
                height: 60

                TextField{
                    id: serverPort
                    placeholderText: "server port"
                    placeholderTextColor: "red"
                    validator: IntValidator{bottom: 0}
                }

            }

            Rectangle{
                width: parent.width
                height: 60

                TextField{
                    id: serverMessage
                    placeholderText: "enter the message"
                    placeholderTextColor: "red"
                }

            }

            Rectangle{
                width: 100
                height: 60
                Button{
                    id: connect
                    anchors.fill: parent
                    text: "connect"
                    onClicked: {
                        client_backend.setMessageServerAddress(serverAddress.text)
                        client_backend.setMessageServerPort(serverPort.text)
                        client_backend.setMessageServerMessage(serverMessage.text)
                        client_backend.connect_to_server()
                        label.text = client_backend.getmessageServerFeedback()
                    }
                }

            }


        }

    }

    Label{
        id: label
        anchors.horizontalCenter: recta1.horizontalCenter
        anchors.top: recta1.bottom
        anchors.topMargin: 10
        font.pointSize: 10
    }



}
