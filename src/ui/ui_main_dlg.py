# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/ui_main_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 499)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layMessage = QtWidgets.QHBoxLayout()
        self.layMessage.setContentsMargins(0, -1, -1, 0)
        self.layMessage.setSpacing(0)
        self.layMessage.setObjectName("layMessage")
        self.lblMessage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMessage.sizePolicy().hasHeightForWidth())
        self.lblMessage.setSizePolicy(sizePolicy)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setOpenExternalLinks(False)
        self.lblMessage.setObjectName("lblMessage")
        self.layMessage.addWidget(self.lblMessage)
        self.verticalLayout.addLayout(self.layMessage)
        self.gbMain = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gbMain.sizePolicy().hasHeightForWidth())
        self.gbMain.setSizePolicy(sizePolicy)
        self.gbMain.setTitle("")
        self.gbMain.setObjectName("gbMain")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbMain)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layMasternodesControl = QtWidgets.QHBoxLayout()
        self.layMasternodesControl.setContentsMargins(12, 0, 0, 0)
        self.layMasternodesControl.setSpacing(8)
        self.layMasternodesControl.setObjectName("layMasternodesControl")
        self.label_5 = QtWidgets.QLabel(self.gbMain)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.layMasternodesControl.addWidget(self.label_5)
        self.cboMasternodes = QtWidgets.QComboBox(self.gbMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboMasternodes.sizePolicy().hasHeightForWidth())
        self.cboMasternodes.setSizePolicy(sizePolicy)
        self.cboMasternodes.setMinimumSize(QtCore.QSize(140, 0))
        self.cboMasternodes.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cboMasternodes.setEditable(False)
        self.cboMasternodes.setObjectName("cboMasternodes")
        self.layMasternodesControl.addWidget(self.cboMasternodes)
        self.btnMoveMnUp = QtWidgets.QPushButton(self.gbMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMoveMnUp.sizePolicy().hasHeightForWidth())
        self.btnMoveMnUp.setSizePolicy(sizePolicy)
        self.btnMoveMnUp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnMoveMnUp.setStyleSheet("padding-left: 0px;\n"
"padding-right: 0px;")
        self.btnMoveMnUp.setText("")
        self.btnMoveMnUp.setFlat(False)
        self.btnMoveMnUp.setObjectName("btnMoveMnUp")
        self.layMasternodesControl.addWidget(self.btnMoveMnUp)
        self.btnMoveMnDown = QtWidgets.QPushButton(self.gbMain)
        self.btnMoveMnDown.setStyleSheet("padding-left: 0px;\n"
"padding-right: 0px;")
        self.btnMoveMnDown.setText("")
        self.btnMoveMnDown.setObjectName("btnMoveMnDown")
        self.layMasternodesControl.addWidget(self.btnMoveMnDown)
        self.btnNewMn = QtWidgets.QPushButton(self.gbMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNewMn.sizePolicy().hasHeightForWidth())
        self.btnNewMn.setSizePolicy(sizePolicy)
        self.btnNewMn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnNewMn.setObjectName("btnNewMn")
        self.layMasternodesControl.addWidget(self.btnNewMn)
        self.btnDuplicateMn = QtWidgets.QPushButton(self.gbMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDuplicateMn.sizePolicy().hasHeightForWidth())
        self.btnDuplicateMn.setSizePolicy(sizePolicy)
        self.btnDuplicateMn.setObjectName("btnDuplicateMn")
        self.layMasternodesControl.addWidget(self.btnDuplicateMn)
        self.btnDeleteMn = QtWidgets.QPushButton(self.gbMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteMn.sizePolicy().hasHeightForWidth())
        self.btnDeleteMn.setSizePolicy(sizePolicy)
        self.btnDeleteMn.setObjectName("btnDeleteMn")
        self.layMasternodesControl.addWidget(self.btnDeleteMn)
        self.btnEditMn = QtWidgets.QPushButton(self.gbMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEditMn.sizePolicy().hasHeightForWidth())
        self.btnEditMn.setSizePolicy(sizePolicy)
        self.btnEditMn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnEditMn.setObjectName("btnEditMn")
        self.layMasternodesControl.addWidget(self.btnEditMn)
        self.btnCancelEditingMn = QtWidgets.QPushButton(self.gbMain)
        self.btnCancelEditingMn.setObjectName("btnCancelEditingMn")
        self.layMasternodesControl.addWidget(self.btnCancelEditingMn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layMasternodesControl.addItem(spacerItem)
        self.layMasternodesControl.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.layMasternodesControl)
        self.frmMasternodeDetails = QtWidgets.QFrame(self.gbMain)
        self.frmMasternodeDetails.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmMasternodeDetails.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmMasternodeDetails.setObjectName("frmMasternodeDetails")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frmMasternodeDetails)
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblMasternodeStatus = QtWidgets.QLabel(self.frmMasternodeDetails)
        self.lblMasternodeStatus.setMinimumSize(QtCore.QSize(0, 0))
        self.lblMasternodeStatus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblMasternodeStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMasternodeStatus.setObjectName("lblMasternodeStatus")
        self.horizontalLayout.addWidget(self.lblMasternodeStatus)
        self.lblMnStatus = QtWidgets.QLabel(self.frmMasternodeDetails)
        self.lblMnStatus.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblMnStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblMnStatus.setText("")
        self.lblMnStatus.setWordWrap(True)
        self.lblMnStatus.setOpenExternalLinks(True)
        self.lblMnStatus.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblMnStatus.setObjectName("lblMnStatus")
        self.horizontalLayout.addWidget(self.lblMnStatus)
        self.btnRefreshMnStatus = QtWidgets.QPushButton(self.frmMasternodeDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRefreshMnStatus.sizePolicy().hasHeightForWidth())
        self.btnRefreshMnStatus.setSizePolicy(sizePolicy)
        self.btnRefreshMnStatus.setObjectName("btnRefreshMnStatus")
        self.horizontalLayout.addWidget(self.btnRefreshMnStatus)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnRegisterDmn = QtWidgets.QPushButton(self.frmMasternodeDetails)
        self.btnRegisterDmn.setObjectName("btnRegisterDmn")
        self.horizontalLayout_2.addWidget(self.btnRegisterDmn)
        self.btnUpdMnPayoutAddr = QtWidgets.QPushButton(self.frmMasternodeDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUpdMnPayoutAddr.sizePolicy().hasHeightForWidth())
        self.btnUpdMnPayoutAddr.setSizePolicy(sizePolicy)
        self.btnUpdMnPayoutAddr.setMinimumSize(QtCore.QSize(0, 0))
        self.btnUpdMnPayoutAddr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnUpdMnPayoutAddr.setStyleSheet("")
        self.btnUpdMnPayoutAddr.setObjectName("btnUpdMnPayoutAddr")
        self.horizontalLayout_2.addWidget(self.btnUpdMnPayoutAddr)
        self.btnUpdMnOperatorKey = QtWidgets.QPushButton(self.frmMasternodeDetails)
        self.btnUpdMnOperatorKey.setObjectName("btnUpdMnOperatorKey")
        self.horizontalLayout_2.addWidget(self.btnUpdMnOperatorKey)
        self.btnUpdMnVotingKey = QtWidgets.QPushButton(self.frmMasternodeDetails)
        self.btnUpdMnVotingKey.setObjectName("btnUpdMnVotingKey")
        self.horizontalLayout_2.addWidget(self.btnUpdMnVotingKey)
        self.btnUpdMnService = QtWidgets.QPushButton(self.frmMasternodeDetails)
        self.btnUpdMnService.setObjectName("btnUpdMnService")
        self.horizontalLayout_2.addWidget(self.btnUpdMnService)
        self.btnRevokeMn = QtWidgets.QPushButton(self.frmMasternodeDetails)
        self.btnRevokeMn.setObjectName("btnRevokeMn")
        self.horizontalLayout_2.addWidget(self.btnRevokeMn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frmMasternodeDetails)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.gbMain)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1027, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuClear = QtWidgets.QMenu(self.menuTools)
        self.menuClear.setObjectName("menuClear")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.action_open_recent_files = QtWidgets.QMenu(self.menuFile)
        self.action_open_recent_files.setObjectName("action_open_recent_files")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_transfer_funds_for_cur_mn = QtWidgets.QAction(MainWindow)
        self.action_transfer_funds_for_cur_mn.setObjectName("action_transfer_funds_for_cur_mn")
        self.action_transfer_funds_for_all_mns = QtWidgets.QAction(MainWindow)
        self.action_transfer_funds_for_all_mns.setObjectName("action_transfer_funds_for_all_mns")
        self.action_transfer_funds_for_any_address = QtWidgets.QAction(MainWindow)
        self.action_transfer_funds_for_any_address.setObjectName("action_transfer_funds_for_any_address")
        self.action_sign_message_with_collateral_addr = QtWidgets.QAction(MainWindow)
        self.action_sign_message_with_collateral_addr.setObjectName("action_sign_message_with_collateral_addr")
        self.action_hw_configuration = QtWidgets.QAction(MainWindow)
        self.action_hw_configuration.setObjectName("action_hw_configuration")
        self.action_load_config_file = QtWidgets.QAction(MainWindow)
        self.action_load_config_file.setObjectName("action_load_config_file")
        self.action_save_config_file_as = QtWidgets.QAction(MainWindow)
        self.action_save_config_file_as.setObjectName("action_save_config_file_as")
        self.action_save_config_file = QtWidgets.QAction(MainWindow)
        self.action_save_config_file.setObjectName("action_save_config_file")
        self.action_check_network_connection = QtWidgets.QAction(MainWindow)
        self.action_check_network_connection.setObjectName("action_check_network_connection")
        self.action_open_settings_window = QtWidgets.QAction(MainWindow)
        self.action_open_settings_window.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.action_open_settings_window.setObjectName("action_open_settings_window")
        self.action_test_hw_connection = QtWidgets.QAction(MainWindow)
        self.action_test_hw_connection.setObjectName("action_test_hw_connection")
        self.action_disconnect_hw = QtWidgets.QAction(MainWindow)
        self.action_disconnect_hw.setObjectName("action_disconnect_hw")
        self.action_hw_initialization_recovery = QtWidgets.QAction(MainWindow)
        self.action_hw_initialization_recovery.setObjectName("action_hw_initialization_recovery")
        self.action_check_for_updates = QtWidgets.QAction(MainWindow)
        self.action_check_for_updates.setObjectName("action_check_for_updates")
        self.action_open_log_file = QtWidgets.QAction(MainWindow)
        self.action_open_log_file.setObjectName("action_open_log_file")
        self.action_about_app = QtWidgets.QAction(MainWindow)
        self.action_about_app.setMenuRole(QtWidgets.QAction.AboutRole)
        self.action_about_app.setObjectName("action_about_app")
        self.action_about_qt = QtWidgets.QAction(MainWindow)
        self.action_about_qt.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_gen_mn_priv_key_compressed = QtWidgets.QAction(MainWindow)
        self.action_gen_mn_priv_key_compressed.setObjectName("action_gen_mn_priv_key_compressed")
        self.action_gen_mn_priv_key_uncompressed = QtWidgets.QAction(MainWindow)
        self.action_gen_mn_priv_key_uncompressed.setObjectName("action_gen_mn_priv_key_uncompressed")
        self.action_command_console = QtWidgets.QAction(MainWindow)
        self.action_command_console.setObjectName("action_command_console")
        self.action_run_trezor_emulator = QtWidgets.QAction(MainWindow)
        self.action_run_trezor_emulator.setObjectName("action_run_trezor_emulator")
        self.action_open_data_folder = QtWidgets.QAction(MainWindow)
        self.action_open_data_folder.setObjectName("action_open_data_folder")
        self.action_clear_wallet_cache = QtWidgets.QAction(MainWindow)
        self.action_clear_wallet_cache.setObjectName("action_clear_wallet_cache")
        self.action_clear_proposals_cache = QtWidgets.QAction(MainWindow)
        self.action_clear_proposals_cache.setObjectName("action_clear_proposals_cache")
        self.action_restore_config_from_backup = QtWidgets.QAction(MainWindow)
        self.action_restore_config_from_backup.setObjectName("action_restore_config_from_backup")
        self.action_sign_message_with_owner_key = QtWidgets.QAction(MainWindow)
        self.action_sign_message_with_owner_key.setObjectName("action_sign_message_with_owner_key")
        self.action_sign_message_with_voting_key = QtWidgets.QAction(MainWindow)
        self.action_sign_message_with_voting_key.setObjectName("action_sign_message_with_voting_key")
        self.action_export_configuration = QtWidgets.QAction(MainWindow)
        self.action_export_configuration.setObjectName("action_export_configuration")
        self.action_import_configuration = QtWidgets.QAction(MainWindow)
        self.action_import_configuration.setObjectName("action_import_configuration")
        self.menuClear.addAction(self.action_clear_wallet_cache)
        self.menuClear.addAction(self.action_clear_proposals_cache)
        self.menuTools.addAction(self.action_transfer_funds_for_any_address)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_sign_message_with_collateral_addr)
        self.menuTools.addAction(self.action_sign_message_with_owner_key)
        self.menuTools.addAction(self.action_sign_message_with_voting_key)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_hw_configuration)
        self.menuTools.addAction(self.action_hw_initialization_recovery)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_check_for_updates)
        self.menuTools.addAction(self.action_command_console)
        self.menuTools.addAction(self.action_open_log_file)
        self.menuTools.addAction(self.action_open_data_folder)
        self.menuTools.addAction(self.menuClear.menuAction())
        self.menuFile.addAction(self.action_load_config_file)
        self.menuFile.addAction(self.action_open_recent_files.menuAction())
        self.menuFile.addAction(self.action_restore_config_from_backup)
        self.menuFile.addAction(self.action_save_config_file)
        self.menuFile.addAction(self.action_save_config_file_as)
        self.menuFile.addAction(self.action_export_configuration)
        self.menuFile.addAction(self.action_import_configuration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_open_settings_window)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_about_app)
        self.menuFile.addAction(self.action_about_qt)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.toolBar.addAction(self.action_open_settings_window)
        self.toolBar.addAction(self.action_save_config_file)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_check_network_connection)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_run_trezor_emulator)
        self.toolBar.addAction(self.action_test_hw_connection)
        self.toolBar.addAction(self.action_disconnect_hw)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_transfer_funds_for_any_address)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cboMasternodes, self.btnNewMn)
        MainWindow.setTabOrder(self.btnNewMn, self.btnEditMn)
        MainWindow.setTabOrder(self.btnEditMn, self.btnDeleteMn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Masternode"))
        self.cboMasternodes.setToolTip(_translate("MainWindow", "List of configured Masternode"))
        self.btnMoveMnUp.setToolTip(_translate("MainWindow", "Move up in the Masternode list"))
        self.btnMoveMnDown.setToolTip(_translate("MainWindow", "Move down in the Masternode list"))
        self.btnNewMn.setToolTip(_translate("MainWindow", "Create a new Masternode configuration"))
        self.btnNewMn.setText(_translate("MainWindow", "New"))
        self.btnDuplicateMn.setToolTip(_translate("MainWindow", "Duplicate Masternode entry"))
        self.btnDuplicateMn.setText(_translate("MainWindow", "Duplicate"))
        self.btnDeleteMn.setToolTip(_translate("MainWindow", "Delete current Masternode configuration"))
        self.btnDeleteMn.setText(_translate("MainWindow", "Delete"))
        self.btnEditMn.setToolTip(_translate("MainWindow", "Enable editing"))
        self.btnEditMn.setText(_translate("MainWindow", "Edit"))
        self.btnCancelEditingMn.setText(_translate("MainWindow", "Cancel editing"))
        self.lblMasternodeStatus.setText(_translate("MainWindow", "Masternode status"))
        self.btnRefreshMnStatus.setToolTip(_translate("MainWindow", "Get Masternode\'s status"))
        self.btnRefreshMnStatus.setText(_translate("MainWindow", "Get status"))
        self.btnRegisterDmn.setToolTip(_translate("MainWindow", "Register new/update existing Masternode by sending a ProRegTx transaction."))
        self.btnRegisterDmn.setText(_translate("MainWindow", "Register Masternode"))
        self.btnUpdMnPayoutAddr.setToolTip(_translate("MainWindow", "Update the Masternode payout address on the network."))
        self.btnUpdMnPayoutAddr.setText(_translate("MainWindow", "Update payout addr."))
        self.btnUpdMnOperatorKey.setToolTip(_translate("MainWindow", "Update the Masternode operator key on the network."))
        self.btnUpdMnOperatorKey.setText(_translate("MainWindow", "Update operator key"))
        self.btnUpdMnVotingKey.setToolTip(_translate("MainWindow", "Update the Masternode voting key on the network."))
        self.btnUpdMnVotingKey.setText(_translate("MainWindow", "Update voting key"))
        self.btnUpdMnService.setToolTip(_translate("MainWindow", "Update the Masternode IP:port and/or the operator reward Zcoin address."))
        self.btnUpdMnService.setText(_translate("MainWindow", "Update service"))
        self.btnRevokeMn.setToolTip(_translate("MainWindow", "Revoke the Masternode operator key."))
        self.btnRevokeMn.setText(_translate("MainWindow", "Revoke operator"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_open_recent_files.setTitle(_translate("MainWindow", "Recent Configuration Files"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_transfer_funds_for_cur_mn.setText(_translate("MainWindow", "Transfer Funds for Current Masternode..."))
        self.action_transfer_funds_for_all_mns.setText(_translate("MainWindow", "Transfer Funds for All Masternodes"))
        self.action_transfer_funds_for_any_address.setText(_translate("MainWindow", "Transfer Funds / Wallet"))
        self.action_sign_message_with_collateral_addr.setText(_translate("MainWindow", "Sign Message with Collateral Address..."))
        self.action_sign_message_with_collateral_addr.setToolTip(_translate("MainWindow", "Sign message with the collateral address of the current masternode"))
        self.action_hw_configuration.setText(_translate("MainWindow", "Hardware Wallet PIN/passphrase Configuration..."))
        self.action_load_config_file.setText(_translate("MainWindow", "Open Configuration File..."))
        self.action_load_config_file.setToolTip(_translate("MainWindow", "Open configuration file"))
        self.action_load_config_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save_config_file_as.setText(_translate("MainWindow", "Save Configuration As..."))
        self.action_save_config_file_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_save_config_file.setText(_translate("MainWindow", "Save Configuration"))
        self.action_save_config_file.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_check_network_connection.setText(_translate("MainWindow", "Check Zcoin Connection"))
        self.action_check_network_connection.setToolTip(_translate("MainWindow", "Check Zcoin Connection"))
        self.action_open_settings_window.setText(_translate("MainWindow", "Settings..."))
        self.action_open_settings_window.setToolTip(_translate("MainWindow", "Settings"))
        self.action_test_hw_connection.setText(_translate("MainWindow", "Test Hardware Wallet Connection"))
        self.action_disconnect_hw.setText(_translate("MainWindow", "Disconnect Hardware Wallet"))
        self.action_hw_initialization_recovery.setText(_translate("MainWindow", "Hardware Wallet Initialization/Recovery..."))
        self.action_check_for_updates.setText(_translate("MainWindow", "Check For Updates"))
        self.action_open_log_file.setText(_translate("MainWindow", "Open Log File"))
        self.action_open_log_file.setShortcut(_translate("MainWindow", "Meta+Alt+L"))
        self.action_about_app.setText(_translate("MainWindow", "About Masternode Tool..."))
        self.action_about_qt.setText(_translate("MainWindow", "About Qt..."))
        self.action_about_qt.setToolTip(_translate("MainWindow", "About Qt"))
        self.action_gen_mn_priv_key_compressed.setText(_translate("MainWindow", "Generate masternode private key (compressed)"))
        self.action_gen_mn_priv_key_compressed.setShortcut(_translate("MainWindow", "Ctrl+Alt+C"))
        self.action_gen_mn_priv_key_uncompressed.setText(_translate("MainWindow", "Generate masternode private key (uncompressed)"))
        self.action_gen_mn_priv_key_uncompressed.setToolTip(_translate("MainWindow", "Generate masternode private key (uncompressed)"))
        self.action_gen_mn_priv_key_uncompressed.setShortcut(_translate("MainWindow", "Ctrl+Alt+U"))
        self.action_command_console.setText(_translate("MainWindow", "Command Console"))
        self.action_command_console.setShortcut(_translate("MainWindow", "Meta+Alt+C"))
        self.action_run_trezor_emulator.setText(_translate("MainWindow", "Run Trezor T emulator"))
        self.action_run_trezor_emulator.setToolTip(_translate("MainWindow", "Run Trezor T emulator"))
        self.action_open_data_folder.setText(_translate("MainWindow", "Open Application Data Folder"))
        self.action_clear_wallet_cache.setText(_translate("MainWindow", "Wallet Cache"))
        self.action_clear_proposals_cache.setText(_translate("MainWindow", "Proposals Cache"))
        self.action_restore_config_from_backup.setText(_translate("MainWindow", "Restore Configuration from Backup..."))
        self.action_restore_config_from_backup.setToolTip(_translate("MainWindow", "Restore Configuration from Backup..."))
        self.action_restore_config_from_backup.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_sign_message_with_owner_key.setText(_translate("MainWindow", "Sign Message with Owner Key..."))
        self.action_sign_message_with_owner_key.setToolTip(_translate("MainWindow", "Sign message with the masternode owner key"))
        self.action_sign_message_with_voting_key.setText(_translate("MainWindow", "Sign Message with Voting Key..."))
        self.action_sign_message_with_voting_key.setToolTip(_translate("MainWindow", "Sign message with the masternode voting key"))
        self.action_export_configuration.setText(_translate("MainWindow", "Export Configuration..."))
        self.action_export_configuration.setToolTip(_translate("MainWindow", "Export Configuration"))
        self.action_import_configuration.setText(_translate("MainWindow", "Import Configuration..."))
        self.action_import_configuration.setToolTip(_translate("MainWindow", "Import Configuration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
