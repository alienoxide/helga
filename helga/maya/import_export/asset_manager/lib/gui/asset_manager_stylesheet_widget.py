
"""
asset_manager_stylesheet_widget
==========================================

Subclass of QWidget that is just a plain QWidget with a set_stylesheet method
and a normal and active color.
"""









#Import
#------------------------------------------------------------------
#python
import logging
#PySide
from PySide import QtGui
from PySide import QtCore





#Import variable
do_reload = True


#asset_manager

#asset_manager_globals
from lib import asset_manager_globals
if(do_reload):reload(asset_manager_globals)






#Globals
#------------------------------------------------------------------

#AssetManager colors
BRIGHT_ORANGE = asset_manager_globals.BRIGHT_ORANGE
DARK_ORANGE = asset_manager_globals.DARK_ORANGE
BRIGHT_GREY = asset_manager_globals.BRIGHT_GREY
GREY = asset_manager_globals.GREY
DARK_GREY = asset_manager_globals.DARK_GREY










#AssetManagerStylesheetWidget class
#------------------------------------------------------------------
class AssetManagerStylesheetWidget(QtGui.QWidget):
    """
    Subclass of QWidget to allow for custom styling
    """

    def __new__(cls, *args, **kwargs):
        """
        AssetManagerStylesheetWidget instance factory.
        """

        #asset_manager_stylesheet_widget_instance
        asset_manager_stylesheet_widget_instance = super(AssetManagerStylesheetWidget, cls).__new__(cls, args, kwargs)

        return asset_manager_stylesheet_widget_instance

    
    def __init__(self, 
                logging_level = logging.DEBUG,
                background_color_normal = GREY,
                background_color_active = BRIGHT_ORANGE,
                fixed_width = None,
                fixed_height = None,
                parent=None):
        """
        AssetManagerStylesheetWidget instance customization.
        """

        #parent_class
        self.parent_class = super(AssetManagerStylesheetWidget, self)
        self.parent_class.__init__(parent)
        
        #instance variables
        #------------------------------------------------------------------
        self.background_color_normal = background_color_normal
        self.background_color_active = background_color_active
        self.fixed_width = fixed_width
        self.fixed_height = fixed_height
        

        #logger
        #------------------------------------------------------------------
        #logger
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logging_level = logging_level
        self.logger.setLevel(self.logging_level)


        
        #stylesheets
        #------------------------------------------------------------------

        
        
        


        
        #Init procedure
        #------------------------------------------------------------------

        #setup_additional_ui
        self.setup_additional_ui()

        #connect_ui
        self.connect_ui()









    #UI setup methods
    #------------------------------------------------------------------
    
    def setup_additional_ui(self):
        """
        Setup additional UI.
        """

        #styled_background
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        
        #set_stylesheet
        self.set_stylesheet()

        #set_size_policy
        self.set_size_policy(self.fixed_width, self.fixed_height)


    def connect_ui(self):
        """
        Connect UI widgets with slots or functions.
        """
        
        pass




    #Getter & Setter
    #------------------------------------------------------------------

    def set_background_color_normal(self, color):
        """
        Set self.background_color_normal
        """
        
        self.background_color_normal = color


    def set_background_color_active(self, color):
        """
        Set self.background_color_active
        """
        
        self.background_color_active = color
    


    #UI Methods
    #------------------------------------------------------------------

    def set_stylesheet(self, role = 'normal'):
        """
        Set stylesheet for this widget based on role.
        """

        #log
        self.logger.debug('Set stylesheet for role: {0}'.format(role))

        #stylesheet_str
        stylesheet_str = self.get_stylesheet(role)
        #set stylesheet
        self.setStyleSheet(stylesheet_str)


    def get_stylesheet(self, role = 'normal'):
        """
        Get stylesheet for a certain role.
        """

        #normal
        if (role == 'normal'):
            return self.get_stylesheet_normal()

        #active
        elif (role == 'active'):
            return self.get_stylesheet_active()
            

    def get_stylesheet_normal(self):
        """
        Get stylesheet for role "normal".
        """

        #ss_dict
        ss_dict = {'background_color_normal' : self.background_color_normal.name(),
                        'background_color_active' : self.background_color_active.name()}
        
        #ss_normal
        ss_normal = " \
\
\
/* AssetManagerStylesheetWidget - normal */\
AssetManagerStylesheetWidget { background-color: %(background_color_normal)s; } \
\
\
"%ss_dict
        
        return ss_normal


    def get_stylesheet_active(self):
        """
        Get stylesheet for role "active".
        """

        #ss_dict
        ss_dict = {'background_color_normal' : self.background_color_normal.name(),
                        'background_color_active' : self.background_color_active.name()}
        
        #ss_active
        ss_active = " \
\
\
/* AssetManagerStylesheetWidget - active */\
AssetManagerStylesheetWidget { background-color: %(background_color_active)s; } \
\
\
"%ss_dict
        
        return ss_active

    
    def set_size_policy(self, width, height):
        """
        Set size policy for self.
        """

        #fixed width and height
        if (width and height):
            self.setFixedSize(width, height)

        #else
        else:

            #set expanding
            expanding_size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
            self.setSizePolicy(expanding_size_policy)

            #fixed width
            if(width):
                self.setFixedWidth(width)

            #fixed height
            elif(height):
                self.setFixedHeight(height)




