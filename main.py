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
import imp
from gui.uis.windows import main_window
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
import cv2


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


# 引入神经网络的模块
# ///////////////////////////////////////////////////////////////
from descratch_westfilm.descratch import fix_single, fix_whole
import torch.distributed as dist
os.environ['MASTER_ADDR'] = 'localhost'
os.environ['MASTER_PORT'] = '62237'
dist.init_process_group(backend='gloo', init_method='env://',
                                world_size=1, rank=0)

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
        self.directory = ''

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


            # 添加的按钮逻辑
            # 选择文件
                   


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

    # cv 图片转换成 qt图片    
    def cv2QPix(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    

        qt_img = QImage(img.data,  # 数据源
                                img.shape[1],  # 宽度
                                img.shape[0],  # 高度
                                img.shape[1] * 3,  # 行字节数
                                QImage.Format_RGB888)
        return QPixmap(qt_img)

    def pages_btn_clicked(self, btn_name):
        ''' 
            自定义按钮点击事件 
        '''
        video_form = self.ui.load_pages.comboBox.currentText() # combobox这个名字后面要改一下
        '''1. 优化界面按钮事件 '''
       
        # //////////////////////////////////////////////////////////////////////////////
        # 要记得在这里写完函数后，还需要在setup_main_window中声明这个按钮（236行左右）

        # 选取文件夹的按钮操作，按下按钮后可选择相应文件夹，然后指定显示被选中文件夹的第5张图片
        if btn_name == "select_dir":
            self.directory = QFileDialog.getExistingDirectory(None,"选取文件夹","./")
            files = os.listdir(self.directory)
            files.sort()
            img = cv2.imread(os.path.join(self.directory, files[0]))
            img = self.cv2QPix(img).scaled(960, 540)
            self.ui.load_pages.og_pic.setPixmap(img) # 这里的og_pic是显示图像的窗口的名字

        # 修复单帧文件的按钮操作，按下按钮后对于选中文件夹的第5张图片进行修复，并进行显示
        if btn_name == "fix_single":
           # saving_dir = QFileDialog.getExistingDirectory(None,"选取文件夹","./")
            og_dir = self.directory
            file_saving = fix_single(og_dir, './')
           # img = cv2.imread(file_saving)
            img = self.cv2QPix(file_saving).scaled(960, 540)
            self.ui.load_pages.fix_pic.setPixmap(img)

        if btn_name == "fix_whole":
            saving_dir = QFileDialog.getExistingDirectory(None,"选取文件夹","./")
            og_dir = self.directory
            video_dir = fix_whole(og_dir, saving_dir, video_form)
            # 进度条得在这里加循环，把descratch里的去掉，或者多线程、多进程
            self.ui.load_pages.fix_pic.setText("修复完成！文件在%s" % video_dir)
            

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