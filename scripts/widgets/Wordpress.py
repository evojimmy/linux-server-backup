from BaseWidget import BaseWidget

class Wordpress(BaseWidget):
    def expand(self):
        import os
        return (self._path+os.sep+'wp-config.php',
                self._path+os.sep+'wp-content',
                self._path+os.sep+'.htaccess'
               )
