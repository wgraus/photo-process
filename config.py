from ConfigParser import ConfigParser


class Config():
    ''' Configuration file
    '''
    def __init__(self):
        self.cfg_par = ConfigParser()
        self.cfg_set = ConfigParser()
        self.load_par()
        self.load_setup()

    def load_par(self):
        ''' Load parameter file
        '''
        if not self.cfg_par.read(["par/par.ini"]):
            print "No existe el archivo"

        r = "Ruta"
        self.c = self.cfg_par.get(r, "Carpeta")
        self.tag = self.cfg_par.get(r, "Tag")
        self.tipus = self.cfg_par.get(r, "Tipus")
        self.original = "%s (Original)" % (self.c)
        self.edit = "%s (Edit)" % (self.c)

        b = "Backup"
        self.bck_nom = self.cfg_par.get(b, "nom")
        self.bck_folders = self.cfg_par.get(b, "folder_list")
        self.bck_destination = self.cfg_par.get(b, "destination")

    def load_setup(self):
        ''' Load setup file
        '''
        if not self.cfg_set.read(["par/setup.ini"]):
            print "No existe el archivo"

        s = "Setup"
        self.dir_fotos = self.cfg_set.get(s, "dir_fotos")
        self.dir_original = self.cfg_set.get(s, "dir_original")
        self.dir_fotografies = self.cfg_set.get(s, "dir_fotografies")
        self.dir_web = self.cfg_set.get(s, "dir_web")



        i = 'Image'
        self.quality = int(self.cfg_set.get(i, 'quality'))
        self.thumb_whith = int(self.cfg_set.get(i, 'thumb_whith'))
        self.thumb_height = int(self.cfg_set.get(i, 'thumb_height'))
        self.orig_whith = int(self.cfg_set.get(i, 'orig_whith'))
        self.orig_height = int(self.cfg_set.get(i, 'orig_height'))
        self.pattern = self.cfg_set.get(i, 'pattern')
        self.thumb_pattern = self.cfg_set.get(i, 'thumb_pattern')

    def guardar_par(self):
        ''' Save parameter file
        '''
        r = "Ruta"
        with open("par/par.ini", 'w') as f:
            self.cfg_par.set(r, "Carpeta", self.c)
            self.cfg_par.set(r, "Tag", self.tag)
            self.cfg_par.set(r, "Tipus", self.tipus)
            self.cfg_par.write(f)
