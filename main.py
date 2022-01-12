# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows import main_window
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)


        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        # 打开home界面
        if btn.objectName() == "btn_home":
            # 选中左边栏
            self.ui.left_menu.select_only_one(btn.objectName())
            # 加载界面
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # 打开第二个界面
        if btn.objectName() == "btn_page_2":
            # 选中左边栏
            self.ui.left_menu.select_only_one(btn.objectName())
            # 加载界面
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        
        
        # 打开第三个界面
        if btn.objectName() == "btn_page_3":
            # 选中左边栏
            self.ui.left_menu.select_only_one(btn.objectName())
            # 加载界面
            MainFunctions.set_page(self, self.ui.load_pages.page_3)


        # 界面顶端设置按钮
        top_btn_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")

         # 打开info界面
        if btn.objectName() == "btn_info" or btn.objectName() == "btn_close_left_column":
            # 取消顶部按钮选中
            top_btn_settings.set_active(False)
            
            if not MainFunctions.left_column_is_visible(self):
                # 显示/隐藏
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    # 取消选中
                    self.ui.left_menu.deselect_all_tab()

                    # 显示/隐藏
                    MainFunctions.toggle_left_column(self)
                    # 选中tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu = self.ui.left_column.menus.menu_1, # 这个menu是在left_column里面的，有单独的界面，点开info和settings可以弹出来不同的页面
                    title = "Info tab",
                    icon_path = Functions.set_svg_icon("icon_info.svg")
                )


        # 打开设置界面
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # 取消顶部按钮选中
            top_btn_settings.set_active(False)
            
            if not MainFunctions.left_column_is_visible(self):
                # 显示/隐藏
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    # 取消选中
                    self.ui.left_menu.deselect_all_tab()

                    # 显示/隐藏
                    MainFunctions.toggle_left_column(self)
                    # 选中tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu = self.ui.left_column.menus.menu_2,
                    title = "Settings",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )



            # # 选中左边栏
            # self.ui.left_menu.select_only_one(btn.objectName())
            # # 加载界面
            # MainFunctions.set_page(self, self.ui.load_pages.page_4)



        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Settings            
            btn_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            btn_settings.set_active_tab(False)            

            # Get Left Menu Info            
            btn_info = MainFunctions.get_left_menu_btn(self, "btn_info")
            btn_info.set_active_tab(False)
       


        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())