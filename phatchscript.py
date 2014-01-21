import os


class PhatchScript():
    """PhatchScript"""
    def __init__(self, c):
        self.c = c
        self.thumb = 't.phatch'
        self.gal = 'g.phatch'
        self.p = 'phatch'
        self.v = '-v'

    def generar_files(self):
        """ Genera files phatch
        """
        self.l("Creating phatch files")
        self.write_file(self.gal)
        self.write_file(self.thumb)

    def write_file(self, name):
        """ Genera file
        """
        dw = self.c.dir_web
        tp = self.c.tipus
        ta = self.c.tag
        with open("%s/%s" % (self.p, name), "r") as f:
            g = f.read().replace('\n', '')
            with open("%s" % name, 'w') as f:
                f.write(g % (dw, tp, ta))

    def crear(self):
        """ Crea tag folder
        """
        self.l("Creating tag folder")
        dw = self.c.dir_web
        tp = self.c.tipus
        ta = self.c.tag
        if not os.path.exists("%s/%s/%s" % (dw, tp, ta)):
            os.makedirs("%s/%s/%s" % (dw, tp, ta))

    def borrar(self):
        """ borra phatch files
        """
        self.l("Remove phatch files")
        dt = self.c.dir_treball
        os.remove("%s/%s" % (dt, self.thumb))
        os.remove("%s/%s" % (dt, self.gal))

    def run_phatch(self):
        """ Run phatch process
        """
        self.l("Run phatch")
        df = self.c.dir_fotos
        os.system("%s %s %s %s" % (self.p, self.v, self.gal, df))
        os.system("%s %s %s %s" % (self.p, self.v, self.thumb, df))

    def l(self, l):
        print "%s ..." % l

    def run(self):
        """ Run phatch process
        """
        self.generar_files()
        self.crear()
        self.run_phatch()
        self.borrar()
