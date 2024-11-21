// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0-only

import QtQuick 6.7
import UntitledProject

Window {
    id: mainWindow
    visible: true
    title: "Level Editor"

    // In case you have some wonky monitor
    width: mainScreen.width > 0 ? mainScreen.width : 1024
    height: mainScreen.height > 0 ? mainScreen.height : 768

    Screen01 {
        id: mainScreen
        anchors.fill: parent // You get full screen
    }
}